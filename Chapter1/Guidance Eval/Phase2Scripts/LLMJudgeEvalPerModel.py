import numpy as np
import pandas as pd
from scipy.stats import binom, chi2
from math import log, sqrt

# --- CONSTANTS ---
Z_SCORE_95 = 1.96 # For 95% Confidence Intervals

def calculate_basic_counts(df):
    """
    1) Calculates C_i, N_i, n^i_10, and n^i_01 for each model (i).

    Args:
        df (pd.DataFrame): DataFrame with columns 'model_id', 'LLM_choice', 'Human_choice'.
                           LLM_choice and Human_choice must be 0 or 1.

    Returns:
        pd.DataFrame: A table containing the calculated counts per model.
    """
    
    # 1. Calculate agreement (C_i) and total consistent pairs (N_i)
    df['Agreement'] = (df['LLM_choice'] == df['Human_choice']).astype(int)
    counts = df.groupby('model_id').agg(
        C_i=('Agreement', 'sum'),
        N_i=('model_id', 'count')
    ).reset_index()

    # 2. Calculate discordant pairs (n^i_10 and n^i_01)
    
    # n^i_10: LLM=1 (IF) and Human=0 (Base) - LLM over-calls IF
    n_10_df = df[(df['LLM_choice'] == 1) & (df['Human_choice'] == 0)].groupby('model_id').size().reset_index(name='n_10')
    
    # n^i_01: LLM=0 (Base) and Human=1 (IF) - LLM under-calls IF
    n_01_df = df[(df['LLM_choice'] == 0) & (df['Human_choice'] == 1)].groupby('model_id').size().reset_index(name='n_01')

    # Merge results
    results = counts.merge(n_10_df, on='model_id', how='left').merge(n_01_df, on='model_id', how='left').fillna(0)
    
    # Ensure counts are integers
    results[['C_i', 'N_i', 'n_10', 'n_01']] = results[['C_i', 'N_i', 'n_10', 'n_01']].astype(int)
    
    return results

def calculate_accuracy_metrics(row):
    """
    2) Calculates Accuracy, Wilson CI, and Exact One-Sided Binomial P-value for a single model (row).
    """
    C_i = row['C_i']
    N_i = row['N_i']
    
    if N_i == 0:
        return pd.Series([0.0, (0.0, 0.0), 1.0], 
                         index=['Accuracy', 'Wilson_CI', 'Binomial_P'])
    
    # --- 1. Accuracy ---
    Acc_i = C_i / N_i
    
    # --- 2. Wilson 95% CI (z = 1.96) ---
    z_sq = Z_SCORE_95**2
    p_hat = Acc_i
    
    # Numerator calculation (shared component)
    num_core = p_hat + (z_sq / (2 * N_i))
    
    # Error term calculation (the sqrt part)
    err_term = Z_SCORE_95 * sqrt( (p_hat * (1 - p_hat) / N_i) + (z_sq / (4 * N_i**2)) )
    
    # Denominator
    den = 1 + (z_sq / N_i)
    
    ci_lower = (num_core - err_term) / den
    ci_upper = (num_core + err_term) / den
    
    # Ensure CIs are capped at [0, 1]
    ci_lower = max(0.0, ci_lower)
    ci_upper = min(1.0, ci_upper)

    Wilson_CI = (ci_lower, ci_upper)
    
    # --- 3. Exact One-Sided Binomial P-value (P(X >= C_i) under H0: p=0.5) ---
    # binom.sf(k, n, p) gives P(X > k) -> we need P(X >= C_i), so we use k = C_i - 1
    Binomial_P = binom.sf(C_i - 1, N_i, 0.5)
    
    return pd.Series([Acc_i, Wilson_CI, Binomial_P], 
                     index=['Accuracy', 'Wilson_CI', 'Binomial_P'])

def calculate_mcnemar_metrics(row):
    """
    3) Calculates McNemar's exact p-value, Chi-squared, and Discordant Odds Ratio (OR) + CI.
    """
    n_10 = row['n_10']
    n_01 = row['n_01']
    
    m = n_10 + n_01
    
    if m == 0:
        # If no discordant pairs, cannot assess bias
        return pd.Series([1.0, 0.0, 1.0, (1.0, 1.0), 'N/A'], 
                         index=['McNemar_P', 'McNemar_Chi2', 'OR', 'OR_CI', 'Bias_Direction'])
    
    # --- 1. Exact McNemar (Two-Sided Binomial Test on m) ---
    # We test H0: n_10 ~ Binom(m, 0.5).
    # The p-value is the probability of observing a result as extreme or more extreme
    # than the observed n_10 (or n_01).
    
    # The observed number of successes is the lower of the two discordant counts
    # and the complement (total m) is the other.
    k_obs = min(n_10, n_01)
    
    # Calculate the two-sided p-value: P(X <= k_obs) + P(X >= m - k_obs)
    # The cumulative distribution function (cdf) and survival function (sf) are used.
    # Note: P(X >= m - k_obs) is P(X > m - k_obs - 1)
    p_val_one_side = binom.cdf(k_obs, m, 0.5)
    McNemar_P = 2 * p_val_one_side 
    # Max p-value is 1.0
    McNemar_P = min(1.0, McNemar_P)
    
    # --- 2. Continuity-Corrected McNemar Chi-Squared ---
    if m >= 5: # Chi-square approximation is generally okay for m >= 5
        chi2_stat = (abs(n_10 - n_01) - 1)**2 / m
    else:
        chi2_stat = np.nan # Not reliable for small m
    
    # --- 3. Discordant Odds Ratio (OR) and CI ---
    # Use continuity correction (+0.5) for CI if any cell is zero
    n_10_corr = n_10 + 0.5 if n_10 == 0 or n_01 == 0 else n_10
    n_01_corr = n_01 + 0.5 if n_10 == 0 or n_01 == 0 else n_01
    
    OR = n_10_corr / n_01_corr
    
    # 95% CI on log scale
    log_OR = log(OR)
    SE_log_OR = sqrt((1 / n_10_corr) + (1 / n_01_corr))
    
    log_ci_lower = log_OR - Z_SCORE_95 * SE_log_OR
    log_ci_upper = log_OR + Z_SCORE_95 * SE_log_OR
    
    # Exponentiate back to original scale
    OR_CI = (np.exp(log_ci_lower), np.exp(log_ci_upper))
    
    # --- 4. Bias Direction ---
    if McNemar_P < 0.05:
        if n_10 > n_01:
            Bias_Direction = 'Bias: Over-calls IF (n10 > n01)'
        else:
            Bias_Direction = 'Bias: Under-calls IF (n01 > n10)'
    else:
        Bias_Direction = 'No significant bias (p>=0.05)'
    
    return pd.Series([McNemar_P, chi2_stat, OR, OR_CI, Bias_Direction], 
                     index=['McNemar_P', 'McNemar_Chi2', 'OR', 'OR_CI', 'Bias_Direction'])


def run_validation_analysis(df_input):
    """
    Orchestrates the three analysis steps and combines results.
    """
    print("--- 1. Calculating Basic Counts ---")
    counts_df = calculate_basic_counts(df_input)
    print("Counts Calculated.")

    # Apply Accuracy Metrics (Step 2)
    print("--- 2. Calculating Accuracy Metrics (Wilson CI & Binomial P) ---")
    accuracy_metrics = counts_df.apply(calculate_accuracy_metrics, axis=1)
    
    # Apply McNemar Metrics (Step 3)
    print("--- 3. Calculating Bias Metrics (McNemar & Odds Ratio) ---")
    mcnemar_metrics = counts_df.apply(calculate_mcnemar_metrics, axis=1)
    
    # Combine all results
    final_report = pd.concat([counts_df, accuracy_metrics, mcnemar_metrics], axis=1)
    
    # Add McNemar m (m = n10 + n01) for completeness
    final_report['m'] = final_report['n_10'] + final_report['n_01']
    
    # Formatting for final display
    final_report['Accuracy'] = final_report['Accuracy'].round(3)
    final_report['Binomial_P'] = final_report['Binomial_P'].round(4)
    final_report['McNemar_P'] = final_report['McNemar_P'].round(4)
    final_report['McNemar_Chi2'] = final_report['McNemar_Chi2'].round(2)
    final_report['OR'] = final_report['OR'].round(3)
    
    return final_report.set_index('model_id')

# =====================================================================
# --- DEMO DATA GENERATION AND EXECUTION ---
# =====================================================================

# Create dummy data simulating 5 models, each with ~100 consistent pairs (N_i)
# J(P)=LLM_choice, h(P)=Human_choice
np.random.seed(42)
NUM_PAIRS = 500

# Model 1: High Accuracy (0.80), Balanced Errors (Good Judge)
df1 = pd.DataFrame({
    'model_id': 'Model_A',
    'LLM_choice': np.random.choice([0, 1], size=100, p=[0.5, 0.5]),
    'Human_choice': np.random.choice([0, 1], size=100, p=[0.1, 0.9])
})
# Simulate 80% agreement: C_i approx 80

# Model 2: Moderate Accuracy (0.65), Strong Bias (Over-calls IF: n10 >> n01)
df2 = pd.DataFrame({
    'model_id': 'Model_B',
    'LLM_choice': np.random.choice([0, 1], size=100, p=[0.1, 0.9]), # Tends to say 1 (IF)
    'Human_choice': np.random.choice([0, 1], size=100, p=[0.35, 0.65]) # Humans prefer IF less strongly
})
# Simulate 65% agreement: C_i approx 65

# Model 3: Random Accuracy (0.50), No predictive power
df3 = pd.DataFrame({
    'model_id': 'Model_C',
    'LLM_choice': np.random.choice([0, 1], size=100, p=[0.5, 0.5]),
    'Human_choice': np.random.choice([0, 1], size=100, p=[0.5, 0.5])
})

# Model 4: High Accuracy (0.75), Under-calls IF (n01 > n10)
df4 = pd.DataFrame({
    'model_id': 'Model_D',
    'LLM_choice': np.random.choice([0, 1], size=100, p=[0.4, 0.6]), 
    'Human_choice': np.random.choice([0, 1], size=100, p=[0.25, 0.75]) 
})


# Combine data
df_combined = pd.concat([df1, df2, df3, df4]).reset_index(drop=True)

# Run the analysis
report_table = run_validation_analysis(df_combined)

print("\n" + "="*80)
print("             LLM JUDGE AGREEMENT VALIDATION REPORT (Per-Model)")
print("="*80)
print(report_table[['N_i', 'C_i', 'Accuracy', 'Wilson_CI', 'Binomial_P', 
                    'n_10', 'n_01', 'm', 'McNemar_P', 'OR', 'OR_CI', 'Bias_Direction']])

# --- Example Conclusion Interpretation ---
print("\n" + "="*80)
print("INTERPRETATION NOTES")
print("="*80)
print("Model_A: Likely a good judge. High Accuracy, low Binomial P, and no significant McNemar bias.")
print("Model_B: Predictive (high Accuracy, low Binomial P), but has a significant bias (low McNemar P).")
print("Model_C: Not predictive (Accuracy near 0.5, high Binomial P). Cannot be used.")
print("Model_D: Predictive, and if McNemar P is low, the bias is toward under-calling IF (n01 > n10).")
print("Note: Binomial P < 0.05 indicates the judge is significantly better than chance (0.5).")
print("Note: McNemar P < 0.05 indicates the judge has a significant systematic bias in its errors.")