import numpy as np
import pandas as pd
import pymc as pm
import arviz as az

# --- 1. Expected Input Format and Shape ---

# Total number of model pairs (i=1..5) and conversations (k=1..20)
NUM_MODELS = 5
NUM_CONVERSATIONS = 20
TOTAL_OBSERVATIONS = NUM_MODELS * NUM_CONVERSATIONS # 100 total judgments

# --- 2. Simulating Data for Example ---

# A) Model Indices (0 to 4, repeated 20 times)
# [0, 0, ..., 0,  1, 1, ..., 1,  ..., 4, 4, ..., 4]
model_indices = np.repeat(np.arange(NUM_MODELS), NUM_CONVERSATIONS)

# B) Conversation Indices (0 to 19, repeated 5 times)
# [0, 1, ..., 19, 0, 1, ..., 19, ..., 0, 1, ..., 19]
conversation_indices = np.tile(np.arange(NUM_CONVERSATIONS), NUM_MODELS)

# C) Preference Data (Simulated y_i,k)
# We simulate a moderate overall mean effect (mu=0.5) with some noise
# This uses the logit link: p = 1 / (1 + exp(-(alpha + beta)))
np.random.seed(8675309)
# True effects (Hypothetical):
true_mu = 0.5
true_alpha_i = np.random.normal(loc=true_mu, scale=0.3, size=NUM_MODELS)
true_beta_k = np.random.normal(loc=0.0, scale=0.8, size=NUM_CONVERSATIONS) # High conversation variance

# Linear predictor (alpha_i + beta_k)
linear_predictor = true_alpha_i[model_indices] + true_beta_k[conversation_indices]
p_true = 1 / (1 + np.exp(-linear_predictor))

# Observed preference data
preference_data = np.random.binomial(n=1, p=p_true, size=TOTAL_OBSERVATIONS)

# Define coordinates for easy reading of results
coords = {
    'model': np.arange(NUM_MODELS),
    'conversation': np.arange(NUM_CONVERSATIONS)
}

# --- 3. PyMC Model Definition and Sampling ---

with pm.Model(coords=coords) as cross_classified_bt_model:
    
    # ---------------------------------------------
    # 5.3 Hierarchical Priors (Hyperpriors)
    # ---------------------------------------------
    
    # Model-level hyperparameters:
    mu = pm.Normal("mu", mu=0.0, sigma=1.0)        # Overall mean effect of IF enhancement
    sigma = pm.HalfNormal("sigma", sigma=1.0)      # Variance of alpha_i across models (cross-model heterogeneity)
    
    # Conversation-level hyperparameter (NEW):
    tau = pm.HalfNormal("tau", sigma=1.0)          # Variance of beta_k across conversations (cross-conversation heterogeneity)

    # ---------------------------------------------
    # 5.3 Hierarchical Priors (Random Effects)
    # ---------------------------------------------
    
    # Model-specific effects (alpha_i): alpha_i ~ N(mu, sigma^2)
    alpha_i = pm.Normal("alpha_i", mu=mu, sigma=sigma, dims="model")

    # Conversation-specific effects (beta_k) (NEW): beta_k ~ N(0, tau^2)
    beta_k = pm.Normal("beta_k", mu=0.0, sigma=tau, dims="conversation")

    # ---------------------------------------------
    # 5.2 Model Formulation (Linear Predictor and Likelihood)
    # ---------------------------------------------
    
    # The linear predictor: alpha_i + beta_k
    # We index alpha_i and beta_k to match the observations
    linear_predictor = alpha_i[model_indices] + beta_k[conversation_indices]
    
    # BT Probability: p = logit^{-1}(alpha_i + beta_k)
    p = pm.Deterministic("p", pm.math.invlogit(linear_predictor), dims="observation")

    # The likelihood: y_i,k ~ Bernoulli(p)
    likelihood = pm.Bernoulli("likelihood", p=p, observed=preference_data)

    # --- 4. Posterior Inference (HMC/NUTS) ---
    
    # Sample the posterior distribution
    # PyMC uses NUTS by default
    idata = pm.sample(
        draws=1000, 
        tune=1000, 
        target_accept=0.9,
        chains=4,
        random_seed=42
    )

# --- 5. Posterior Summaries (5.6) ---

print("\n### Posterior Summaries (5.6) ###")
az.summary(
    idata, 
    var_names=['mu', 'sigma', 'tau', 'alpha_i'], 
    filter_vars="top", # Filters out the full beta_k list if too long
    kind="stats"
)