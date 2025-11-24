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

## Experimental Setup
### Step 1: Improving IF
* We will experiment on 5 models: ranging from large to small model
* REQUIRED: what dataset will we use, and what evaluation do we need to test for IF?

### Step 2: Testing to guage Guidance improvement
* Same inputs for all 5 models 
-> Prompts will be drawn from BRIDGE paper: https://aclanthology.org/2024.naacl-long.120/
-> Datasets will be the Unifying AI Tutor Eval: https://github.com/kaushal0494/UnifyingAITutorEvaluation/tree/main/BEA_Shared_Task_2025_Datasets with 192 dialogues

For each of the dialogue, each model will produce one response, using the strategy identified in the BRIDGE paper

* Evaluation:
1) MT Bench or similar setup using LLM as a Judge
2) To avoid bias, we then sample at random for human annotation
-> Sample 100 of response pairs from each model, totalling 500 samples
-> Recruit student annotators, each student is responsible for annotating which they prefer on 100 samples
-> To have at least 3 annotators, for aggreeemnt analysis, each response is sampled 3 times across the 15 different students

### Methods:
1) Given one instance of input, feed that to two models (same base model, one is with IF enhanced, one doesn't)
2) The output is a sample pair, with identical inputs, but two different responses

We then create a set of dialogue pairs to be judged (C_h + base model, C_h + IF_enhanced)

Here is the **clean, GitHub-ready markdown version** of your *Experimental Setup & Methods* section.
All formulas are rendered in markdown/LaTeX (GitHub supports inline and block math via MathJax).

You can paste this **directly into README.md**.

---

# Experimental Setup and Methods

## 1. Overview

This study evaluates whether improving a model’s **Instruction-Following (IF)** ability leads to improved **Guidance** in AI tutoring. The pipeline includes two phases:

1. **Phase 1 — IF Enhancement:**
   Train five base language models and five IF-enhanced versions on instruction-following datasets and evaluate IF improvement.

2. **Phase 2 — Guidance Evaluation:**
   For each tutoring input, generate controlled response pairs from both versions of each model and evaluate them using both LLM-as-judge and human annotations.

---

## 2. Phase 1: Improving Instruction Following

Let:

[
\mathcal{M}={M_1,\ldots,M_5}
]

be the set of five base models, and let:

[
M_i^{\text{IF}}
]

denote the instruction-following–enhanced variant of model (M_i).

### 2.1 Instruction-Following Training

Each (M_i^{\text{IF}}) is trained using:

* An instruction-following dataset: (\mathcal{D}_{\text{IF}})
* Chain-of-thought augmentation
* Step-adherence reinforcement signals (if applicable)

### 2.2 Instruction-Following Evaluation

We evaluate IF capability using a benchmark (\mathcal{B}_{\text{IF}}) with scoring function (f):

[
\mathrm{IFScore}(M) = \frac{1}{|\mathcal{B}*{\text{IF}}|} \sum*{x \in \mathcal{B}_{\text{IF}}} f(M(x), y_x)
]

where:

* (y_x) is the gold instruction output
* (f) checks constraint satisfaction or correctness

A model improves IF if:

[
\mathrm{IFScore}(M_i^{\text{IF}}) > \mathrm{IFScore}(M_i)
]

---

## 3. Phase 2: Evaluating Tutoring Guidance

We use 192 tutoring inputs from:

* **BRIDGE** (strategy-driven tutoring prompts)
* **Unifying AI Tutor Evaluation (BEA 2025)**

Let the tutoring set be:

[
\mathcal{D}*{\text{tutor}} = {d_1,\ldots,d*{192}}
]

### 3.1 Response Pair Generation

For each input (d_j), we generate:

[
r_{i,j} = M_i(d_j), \qquad r^{\text{IF}}_{i,j} = M_i^{\text{IF}}(d_j)
]

The pair for model (i) and input (j) is:

[
p_{i,j} = (r_{i,j}, r^{\text{IF}}_{i,j})
]

Total pairs:

[
|\mathcal{P}| = 5 \times 192 = 960
]

---

## 4. LLM-as-Judge Evaluation

Each pair is evaluated by an LLM-judge (J):

[
\mathrm{LLMPreference}(p_{i,j}) \in {0, 1}
]

* **1 = IF-enhanced response preferred**
* **0 = base model preferred**

Model-level preference score:

[
\mathrm{LLMScore}(M_i) = \frac{1}{192}\sum_{j=1}^{192} \mathrm{LLMPreference}(p_{i,j})
]

---

## 5. Human Evaluation (with Stratified Sampling)

Because human annotation is costly, we sample:

* **100 response pairs per model**
* **500 pairs total**

Let:

[
|\mathcal{P}_{i}^{\text{sample}}| = 100
]

and:

[
|\mathcal{P}_{\text{human}}| = 500
]

### 5.1 Goals of the Stratified Strategy

The sampling must enforce:

* **(A) No annotator sees the same pair twice**
* **(B) No annotator sees pairs from only one model**
* **(C) Each model contributes equally to the evaluation**
* **(D) Each pair receives 3 independent judgments**

### 5.2 Annotator Setup

Let:

* (A={a_1,\ldots,a_{15}}) = 15 annotators
* Each annotator labels (K = 100) pairs
* Each pair is labeled by (R = 3) annotators

### 5.3 Constraint: No Annotator Sees Both Sides Separately

Annotators always evaluate the *pair*, meaning:

[
(r_{i,j}, r^{\text{IF}}_{i,j})
]

is shown together as one unit.
Annotators **never** see a response individually in other contexts.

### 5.4 Equal Exposure Across Models

Let:

[
\mathcal{P}^{(a_k)} = \text{pairs given to annotator } a_k
]

Each annotator receives a balanced subset:

[
|\mathcal{P}_{i}^{(a_k)}| \approx \frac{K}{5} = 20
]

Thus every annotator sees a mix of all 5 model families.

### 5.5 Redundant Coverage (3× per pair)

Each pair is annotated by **exactly 3 annotators**:

[
|{ a_k : p \in \mathcal{P}^{(a_k)} }| = 3
]

Additionally, no two annotators receive identical sets:

[
\mathcal{P}^{(a_m)} \cap \mathcal{P}^{(a_n)} \neq \mathcal{P}^{(a_m)}
]

This prevents correlated bias.

---

## 6. Human Preference Score

A pair-level human decision:

[
h(p) =
\begin{cases}
1 & \text{IF-enhanced preferred} \
0 & \text{otherwise}
\end{cases}
]

Model-level human preference score:

[
\mathrm{HumanScore}(M_i) =
\frac{1}{|\mathcal{P}*{i}^{\text{sample}}|}
\sum*{p\in\mathcal{P}_{i}^{\text{sample}}} h(p)
]

We compute inter-rater agreement (e.g., Fleiss’ κ) across the 3 judgments for each pair.

---

## 7. Outcome Interpretation

A model exhibits improved **Guidance** if both:

[
\mathrm{LLMScore}(M_i^{\text{IF}}) > \mathrm{LLMScore}(M_i)
]

and

[
\mathrm{HumanScore}(M_i^{\text{IF}}) > \mathrm{HumanScore}(M_i)
]

across multiple models (i).


