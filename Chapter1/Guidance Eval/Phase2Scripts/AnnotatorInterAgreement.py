import numpy as np
import pandas as pd

def fleiss_kappa(ratings_df, R=3, C=2):
    """
    Computes Fleiss' Kappa statistic based on the provided mathematical definitions.

    Args:
        ratings_df (pd.DataFrame): DataFrame where each row is an item (J)
                                   and columns are raters (R). Values must be
                                   category labels (0 or 1 for C=2).
        R (int): Number of raters (R=3 in your study).
        C (int): Number of categories (C=2 in your study: 0=Base, 1=IF-enhanced).

    Returns:
        float: Fleiss' Kappa (κ) value.
    """
    J = len(ratings_df) # Number of items (500 pairs)

    # 1. Construct the item-by-category count matrix (n_jc)
    # The matrix N should have J rows (items) and C columns (categories 0, 1)
    
    # Calculate n_j,c: the number of raters who assigned item j to category c
    # We use pd.crosstab to count the occurrences of 0 and 1 for each row (item)
    # We must reset the index to ensure the output is only the counts
    
    # Check if all ratings are within the expected categories (0 or 1)
    unique_ratings = ratings_df.stack().unique()
    if not all(c in [0, 1] for c in unique_ratings):
        raise ValueError("Ratings must be either 0 (Base) or 1 (IF-enhanced).")

    # The use of pd.Series.value_counts applies to each row
    n_jc = ratings_df.apply(lambda row: row.value_counts(normalize=False), axis=1).fillna(0)
    
    # Ensure the matrix has exactly C columns, even if a category got 0 counts
    if 0 not in n_jc.columns:
        n_jc[0] = 0
    if 1 not in n_jc.columns:
        n_jc[1] = 0
    n_jc = n_jc[[0, 1]].astype(int)
    
    # 2. Category proportions across all items (p_c)
    # Sum of counts in each category divided by total number of assignments (J * R)
    p_c = n_jc.sum(axis=0) / (J * R)
    
    # 3. Item-level agreement (P_j)
    # Calculate the numerator: sum_c [n_j,c * (n_j,c - 1)]
    # This is the sum of pairs of raters agreeing on category c for item j
    numerator = (n_jc * (n_jc - 1)).sum(axis=1)
    
    # Calculate the denominator: R * (R - 1)
    denominator = R * (R - 1)
    
    # This is the item-wise agreement
    P_j = numerator / denominator

    # 4. Mean observed agreement (P_bar)
    # P_bar = (1 / J) * sum_j P_j
    P_bar = P_j.mean()

    # 5. Expected agreement under random rating (P_e_bar)
    # P_e_bar = sum_c (p_c)^2
    P_e_bar = np.sum(p_c ** 2)

    # 6. Fleiss' Kappa (κ)
    # κ = (P_bar - P_e_bar) / (1 - P_e_bar)
    if P_e_bar == 1:
        # Avoid division by zero if all proportions are 0 (e.g., empty data)
        return 1.0
        
    kappa = (P_bar - P_e_bar) / (1 - P_e_bar)

    return kappa

# --- Example Usage ---

# J=5 items, R=3 raters. Categories: 0 (Base), 1 (IF-enhanced)
# Example data simulating 5 response pairs rated by 3 annotators
# Rater 1, Rater 2, Rater 3
dummy_data = {
    'Rater_A': [1, 0, 1, 0, 1],  # Item 1: 3/3 agree on 1
    'Rater_B': [1, 0, 1, 1, 0],  # Item 2: 2/3 agree on 0 (1 disagrees)
    'Rater_C': [1, 0, 0, 0, 1]   # Item 3: 1/3 agree on 1 (2 disagree)
}
ratings_df_example = pd.DataFrame(dummy_data)

# Assume your actual data (500 pairs x 3 raters) looks like this:
# ratings_df_actual = pd.read_csv('your_ratings_file.csv')

kappa_value = fleiss_kappa(ratings_df_example, R=3, C=2)

print(f"--- Fleiss' Kappa Calculation ---")
print(f"Number of items (J): {len(ratings_df_example)}")
print(f"Number of raters (R): 3")
print(f"Calculated Kappa (κ): {kappa_value:.4f}")

# Example Interpretation:
# κ > 0.80 = Excellent Agreement
# 0.60 < κ < 0.80 = Substantial Agreement
# 0.40 < κ < 0.60 = Moderate Agreement
# 0.20 < κ < 0.40 = Fair Agreement
# κ < 0.20 = Poor/Slight Agreement