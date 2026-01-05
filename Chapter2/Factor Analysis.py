# pip install pandas numpy factor_analyzer semopy

import pandas as pd
import numpy as np
from factor_analyzer import FactorAnalyzer
from semopy import Model, Optimizer

# =========================
# Step 0: Load Survey Data
# =========================
# Assumes CSV file where columns are survey items
# Example: 'A1_Remember', 'A2_Understand', ..., 'B1_Planning', 'B2_Reflection', 'B5_Dependency', etc.

data = pd.read_csv('survey_data.csv')

# =========================
# Step 2a: Exploratory Factor Analysis (EFA)
# =========================

# Step 2a1: Check suitability
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity, calculate_kmo

chi_square_value, p_value = calculate_bartlett_sphericity(data)
kmo_all, kmo_model = calculate_kmo(data)

print(f"Bartlett's test p-value: {p_value}")
print(f"KMO overall: {kmo_model}")

# Step 2a2: Run EFA
# Choose number of factors based on theory (e.g., 4: LowerCog, HigherCog, Learner, Dependency)
fa = FactorAnalyzer(n_factors=4, rotation='oblimin')
fa.fit(data)

# Factor loadings
loadings = pd.DataFrame(fa.loadings_, index=data.columns)
print("Factor Loadings (EFA):")
print(loadings)

# Eigenvalues
ev, v = fa.get_eigenvalues()
print("Eigenvalues:")
print(ev)

# =========================
# Step 2b: Confirmatory Factor Analysis (CFA) using semopy
# =========================
# Define CFA model
# Example latent factors:
# F1: Lower-order cognition (Remember, Understand, Apply)
# F2: Higher-order cognition (Analyze, Evaluate, Create)
# F3: Learner-oriented (Planning, Reflection, Innovation, Self-efficacy)
# F4: Dependency (reverse-coded)

model_desc = """
LowerCog =~ A1_Remember + A2_Understand + A3_Apply
HigherCog =~ A4_Analyze + A5_Evaluate + A6_Create
Learner =~ B1_Planning + B2_Reflection + B6_Innovation + B4_SelfEfficacy
Dependency =~ B5_Dependency
"""

# Create SEM model
model = Model(model_desc)
opt = Optimizer(model)
res = opt.optimize(data)

# Print model fit
print(model.inspect())
print(model.fit())

# =========================
# Step 3: Compute Factor Scores
# =========================

# semopy can compute factor scores
factor_scores = model.predict_factors(data)
factor_scores.to_csv('factor_scores.csv', index=False)
print("Factor scores saved to 'factor_scores.csv'")

# Now each respondent has scores for:
# LowerCog, HigherCog, Learner, Dependency

# =========================
# Optional: Quick visualization
# =========================
import seaborn as sns
import matplotlib.pyplot as plt

sns.pairplot(factor_scores)
plt.suptitle("Pairwise Distribution of Factor Scores")
plt.show()
