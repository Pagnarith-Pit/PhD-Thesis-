# Motivation
Guidance is one of the most important concepts of an AI tutor. After extensive work of unifying AI tutor desired behaviours, BEA 2025 landed on a few dimensions and "Providing Guidance" is one of them"

Lack definition and extremely hard to measure. So we begin by contributing to advancing the evaluation of this critical behavior. 

### Past work
Here, we mention how we created and ran our experiments to come up with the CODE framework short paper
* Datasets
* Training scripts
* Results in tables

### Future Work
Now, we set out to improve the guidance itself
-> Shows that average conversation is short
-> Better guidance would not only mean more effective pedagogical response but perhaps better engagement and more learning opportunities 

However, we've established well that "Guidance" is inherently a human trait, difficult to define, lacking operational/formal defitnition that can capture accurately what it is in a neat formula. Instead, instructors rely solely on prompts or model instructions, defining instead the tasks and desired outputs, with as much steps and explanations as possible - such as MathDIAL, Bridge, Instruct Not Assist, and all others. 

### The Hypothesis
With "Guidance" being guided by instructions in mind, it is a natural hypothesis that a model that can be more faithful and follow instructions better can provide better guidance. So the mission is two fold:

1) Experiment on methods that would help enhance instruction following
2) Test that on a tutoring dataset, to see that given the exact same input and the same model, the one that has its IF capabilities enhanced would provide superior guidance


# Experimental Setup and Methods

This document describes the experimental setup and methodology for evaluating whether improving a model's **Instruction-Following (IF)** ability leads to improved **Guidance** in AI tutoring.

---

## 1. Overview

The study consists of two phases:

1. **Phase 1 — IF Enhancement**
   Train five base language models and five IF-enhanced variants on instruction-following datasets and verify improvements.

2. **Phase 2 — Guidance Evaluation**
   For each tutoring input, generate **paired responses** from both versions of each model. Evaluate the pairs using **LLM-as-judge** and **human annotations**.

---

## 2. Phase 1: Improving Instruction Following

Let

$$
\mathcal{M} = \{ M_1, M_2, M_3, M_4, M_5 \}
$$


be the set of five base models. For each model $M_i$, we define an instruction-following–enhanced variant:


$$
M_i^{\text{IF}}
$$


Each model therefore has two versions:

* Base model: $M_i$
* IF-enhanced model: $M_i^{\text{IF}}$

---

### 2.1 Instruction-Following Training

Each $M_i^{\text{IF}}$ is trained with:

* Instruction-following dataset: $\mathcal{D}_{\text{IF}}$
* Chain-of-thought (CoT) augmentation
* Step-adherence reinforcement signals (if applicable)

---

### 2.2 Instruction-Following Evaluation

We evaluate IF performance using a benchmark $\mathcal{B}_{\text{IF}}$:


$$
\mathrm{IFScore}(M) = \frac{1}{|\mathcal{B}_{\text{IF}}|} \sum_{x \in \mathcal{B}_{\text{IF}}} f(M(x), y_x)
$$


where:

* $y_x$ = gold instruction output for input $x$
* $f(\cdot)$ = scoring function (e.g., exact match, constraint satisfaction, or LLM-judge score)

A model is considered improved if:

$$
\mathrm{IFScore}(M_i^{\text{IF}}) > \mathrm{IFScore}(M_i)
$$


---

## 3. Phase 2: Evaluating Tutoring Guidance

We use **192 tutoring dialogue prompts** from:

* **BRIDGE** (strategy-driven tutoring prompts)
* **Unifying AI Tutor Evaluation (BEA 2025)**

Let the tutoring dataset be:


$$
\mathcal{D}_{\text{tutor}} = \{d_1, \dots, d_{192}\}
$$


### 3.1 Response Pair Generation

For each dialogue $d_j$, each model generates two responses:


$$
r_{i,j}^{\text{base}} = M_i(d_j), \qquad
r_{i,j}^{\text{IF}} = M_i^{\text{IF}}(d_j)
$$


We define a paired comparison:


$$
P_{i,j} = \big(r_{i,j}^{\text{base}}, r_{i,j}^{\text{IF}}\big)
$$


Total pairs:


$$
|\mathcal{P}| = 5 \times 192 = 960
$$


---

## 4. LLM-as-Judge Evaluation
**The test must be run twice, with each pair in reverse order to prevent positional bias, keeping only samples that is consistent**
**That is, only keep sample if A is better than B, when a judge moodel is shown Instruction + A,B vs Instruction + B,A**

For each pair $P_{i,j}$, an LLM judge $J$ outputs:


$$
\mathrm{LLMPreference}(P_{i,j}) \in \{0, 1\}
$$


* 1 → IF-enhanced response preferred
* 0 → base response preferred

Model-level LLM preference:


$$
\mathrm{LLMScore}(M_i) = \frac{1}{192} \sum_{j=1}^{192} \mathrm{LLMPreference}(P_{i,j})
$$

Currently, the best model might be Gemini 3, as it has LearnLM merged into it, with their paper claiming that evaluating pedagogical is easier than implementing it, suggesting a good performance. Needs to be tested on the data to confirm. That is, we rerun Gemini 3 with the Guidance Test Set (as it has ground truth label), and see which is a good judge

---

## 5. Human Evaluation with Stratified Sampling

We sample **100 pairs per model**, giving a total of **500 pairs** for human annotation:


$$
\mathcal{P}_{\text{human}} = \bigcup_{i=1}^{5} \mathcal{P}_i^{\text{sample}}, \quad |\mathcal{P}_i^{\text{sample}}| = 100
$$


### 5.1 Stratified Sampling Goals

The human evaluation ensures:

1. **No annotator sees the same pair twice**
2. **No annotator sees pairs from only one model**
3. **Equal representation of all models across annotators**
4. **Each pair is annotated by 3 independent annotators**
5. **Each pair must be seen in a reverse order by at least one annotator to account for positional bias**

---

### 5.2 Annotator Allocation

Let:

* $A = { a_1, \dots, a_{15} }$ = annotators
* Each annotator labels $K = 100$ pairs
* Each pair is annotated by $R = 3$ annotators

For annotator $a_k$, the batch:


$$
B_k = \{ P_{i,j} \}_{100}
$$


satisfies:


$$
|\mathcal{P}_i \cap B_k| \approx \frac{K}{5} = 20
$$


---

### 5.3 Pair-Level Constraints

1. **No annotator sees both sides separately**:


$$
A(P_{i,j}) \in \{ r_{i,j}^{\text{base}}, r_{i,j}^{\text{IF}} \}
$$


2. **Each pair has exactly 3 independent annotations**:


$$
|\{ a_k : P_{i,j} \in B_k \}| = 3
$$

---

## 6. Human Preference Score

For each pair $P_{i,j}$:


$$
h(P_{i,j}) =
\begin{cases}
1 & \text{IF-enhanced preferred} \\
0 & \text{otherwise}
\end{cases}
$$


Model-level human preference:


$$
\mathrm{HumanScore}(M_i) = \frac{1}{|\mathcal{P}_i^{\text{sample}}|} \sum_{P \in \mathcal{P}_i^{\text{sample}}} h(P)
$$


### Inter-rater agreement

Inter-rater agreement (R = 3 raters) is computed using Fleiss’ κ.

We have C = 2 categories: IF-enhanced (1) and base (0). For each pair (item) j,
let $n_{j,1}$ be the number of raters who chose 1, and $n_{j,0}$ = R - $n_{j,1}$.

Construct the item-by-category count matrix $N = [n_{j,c}]$ for j = 1..J and c ∈ {0,1} where $J = |\mathcal{P}_{\text{human}}|$ (500 pairs).

Category proportions across all items:

$$
p_c = \frac{1}{J R} \sum_{j=1}^{J} n_{j,c}, \quad c \in \{0,1\}, \quad \sum_{c} p_c = 1.
$$

Item-wise agreement:

$$
P_j = \frac{1}{R(R-1)} \sum_{c \in \{0,1\}} n_{j,c}(n_{j,c} - 1).
$$

Mean observed agreement:

$$
\bar{P} = \frac{1}{J} \sum_{j=1}^{J} P_j.
$$

Expected agreement under random rating with fixed category proportions:

$$
\bar{P}_e = \sum_{c \in \{0,1\}} p_c^2.
$$

Fleiss' kappa:

$$
\kappa = \frac{\bar{P} - \bar{P}_e}{1 - \bar{P}_e}.
$$

Optional: report per-model κ by restricting J to items in \mathcal{P}_i^{\text{sample}}.
Also report bootstrap CIs by resampling items j and recomputing κ.

---

### LLM Agreement

1) Basic Count for each model

For each pair $P \in \mathcal{P}_i^{\text{cons}}$, where $\mathcal{P}_i^{\text{cons}}$ is the consistent result of position swapping in LLM as a judge:

$$
J(P)\in{0,1}\quad\text{: LLM judge choice (1 if LLM prefers IF-enhanced; 0 if LLM prefers Base).}
$$

$$
h(P)\in{0,1}\quad\text{: human majority choice (1 if humans prefer IF-enhanced).}
$$

Aggregate (for model (i)):

$$
C_i = \sum_{P\in\mathcal{P}_i^{\text{cons}}} \mathbf{1}{{J(P)=h(P)}}
$$

$$
N_i = \lvert \mathcal{P}_i^{\text{cons}} \rvert
$$

$$
(n_{10})^i = \sum_{P\in\mathcal{P}_i^{\text{cons}}} \mathbf{1} \{J(P)=1; h(P)=0\}
$$

LLM says IF but humans say Base.

$$
(n_{01})^i = \sum_{P\in\mathcal{P}_i^{\text{cons}}} \mathbf{1} \{J(P)=0; h(P)=1\}
$$

LLM says Base but humans say IF.

* Report
Table with one row per model:

|    Model (i) | $N_i$ | C_i) | (n_{10,i}) | (n_{01,i}) |
| -----------: | ----: | ----: | ---------: | ---------: |
| `model-name` | `N_i` | `C_i` | `n_{10,i}` | `n_{01,i}` |
|          ... |   ... |   ... |        ... |        ... |

---
2) Accuracy and confidence interval (Is LLM better than chance?)

Statistic
•	Accuracy: (\widehat{\mathrm{Acc}}_i = C_i / N_i).
CI
•	Use Wilson 95% CI for a proportion (better than normal approx):
[
\text{Wilson CI: } \widehat{p}=\frac{C_i}{N_i},\quad
\mathrm{CI}_{\text{Wilson}} = \frac{\widehat{p} + \frac{z^2}{2N_i} \pm z\sqrt{\frac{\widehat{p}(1-\widehat{p})}{N_i} + \frac{z^2}{4N_i^2}}}{1 + \frac{z^2}{N_i}},\quad z=1.96.
]
Hypothesis test
•	Null (H_0:) Acc = 0.5 (random). Alternative (H_1:) Acc > 0.5.
•	Exact one-sided binomial test (compute (P(X \ge C_i)) under (X\sim\mathrm{Binom}(N_i,0.5))):
[
p_i = \sum_{k=C_i}^{N_i} \binom{N_i}{k} 0.5^{N_i}.
]
Decision rule
•	Declare predictive if (p_i < 0.05) and (\widehat{\mathrm{Acc}}_i > 0.5).
What to report
•	(\widehat{\mathrm{Acc}}_i), Wilson 95% CI, exact binomial one-sided p-value, and raw counts (C_i,N_i).

--- 

3) Positional-bias / asymmetry check (Is LLM systematically biased?)

Why
•	An LLM could be "biased" toward preferring IF-enhanced (or Base) even when humans don't.
Data used
•	Only discordant pairs where LLM and humans disagree: (n_{10}^i) and (n_{01}^i). Let (m = n_{10}^i + n_{01}^i).
Exact McNemar (binomial) test
•	Under (H_0), (n_{10}^i \sim \mathrm{Binom}(m, 0.5)).
•	Two-sided exact p-value: probability of seeing an imbalance at least as extreme as observed. (Compute by summing binomial probabilities.)
•	If (m) is large, you may report continuity-corrected McNemar chi-square:
[
\chi^2 = \frac{(|n_{10}-n_{01}|-1)^2}{n_{10}+n_{01}},
]
with 1 d.f. — but prefer the exact test when (m < 25\text{–}30).
Discordant odds ratio
•	(\widehat{\mathrm{OR}} = n_{10}^i / n_{01}^i). If either cell is 0, add 0.5 to both (continuity correction).
•	Approximate 95% CI on log scale:
[
\log(\widehat{\mathrm{OR}}) \pm 1.96\sqrt{1/n_{10} + 1/n_{01}}.
]
Decision rule
•	If exact McNemar p < 0.05 and (n_{10}^i < n_{01}^i) (i.e., LLM under-calls IF less than it over-calls Base) — you may interpret that LLM is not unfairly overcalling IF. If (n_{10} > n_{01}) and p < 0.05, that is evidence the LLM overcalls IF (bias toward IF).
What to report
•	(n_{10}^i, n_{01}^i, m), exact McNemar p-value, (\widehat{\mathrm{OR}}) + 95% CI. State direction (which error is larger).

---

4) Multiple models: pooled inference across models

Why
•	You have multiple models (M_1,\dots,M_5). You may want an overall p-value.
Fisher’s method
•	Combine one-sided binomial p-values ({p_i}):
[
\chi^2_{\text{Fisher}} = -2\sum_{i=1}^5 \ln(p_i),\quad \chi^2_{\text{Fisher}}\sim \chi^2_{10}.
]
•	Compute combined p-value from (\chi^2_{\text{Fisher}}).
Caveat
•	Fisher assumes independent p-values. If the same human labels or items are reused across models, p-values may be correlated → Fisher can be anticonservative.
Alternative (dependence-robust)
•	Use permutation or bootstrap across items/human labels to get an empirical pooled p-value if dependence is suspected.
Multiple-testing control for per-model claims
•	If you make claims per model, correct the per-model p-value threshold for 5 tests (options):
o	Bonferroni: threshold = 0.05/5 = 0.01 (strict).
o	Benjamini–Hochberg (FDR): if you want discovery control, apply BH at q=0.05.
What to report
•	For pooled test: Fisher statistic, df, combined p-value, and note independence caveat. For per-model: raw p-values and corrected p-values (Bonferroni or FDR).


---

### Results of LLM-Human Agreement Experiments
For each model (M_i), conclude LLM-as-judge is predictive if either:

•	(A) Exact one-sided binomial p-value (p_i < 0.05) and (\widehat{\mathrm{Acc}}_i > 0.5) (report Wilson CI); or
•	(B) McNemar’s exact test p < 0.05 and (n_{10}^i < n_{01}^i) (i.e., LLM does not systematically overcall IF).
For overall pooled claim across models:
•	Use Fisher’s method for a combined p-value, but explicitly state the independence caveat; if dependence is likely, present a permutation-based pooled p-value.

In other words:
•	High accuracy (e.g., 0.75) + significant binomial p → LLM matches humans well.
•	Acc ≈ 0.5 + non-significant → LLM is no better than random.
•	Significant McNemar with (n_{10} > n_{01}) → LLM tends to prefer IF even when humans don't (an overcall bias).
•	Low inter-rater agreement among humans → humans disagree among themselves; be cautious interpreting LLM agreement with majority.



## 7. Outcome Interpretation

A model demonstrates improved **Guidance** if:

$$
\mathrm{LLMScore}(M_i^{\text{IF}}) > \mathrm{LLMScore}(M_i)
$$


and


$$
\mathrm{HumanScore}(M_i^{\text{IF}}) > \mathrm{HumanScore}(M_i)
$$


for multiple models $i = 1 \dots 5$.

---

### 8. Bayeian Sampling For Effect Estimation
If the model's output agrees with human rater's outputs (i.e., 5.4 is statistically significant):
- replace the 500 samples of the bot with ground label, keep the rest synthetic
If not:
- only use the 500 samples obtained from the human raters

Implement Bradley-Terry Model on the ranked sample:
- Using Non-conjugate prior distribution N~(0,1)
- Using 4000 simulations with Hamiltonian Monte Carlo sampling
- using NUTS (No-U-Turn Sampler) algorithm

Key goal: generate an alpha that is the latent parameter predicting whether the enhanced-IF AI utor is more preferred than the base AI tutor
