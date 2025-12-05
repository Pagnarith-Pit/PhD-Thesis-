# **Motivation**

The rapid advancement of Large Language Models (LLMs) has introduced new possibilities for scalable, personalised, and interactive learning support. Among these, one of the most widely anticipated applications is the use of LLMs as AI tutors capable of providing immediate feedback and adaptive guidance to learners. Despite this promise, current LLMs still fall short of achieving the depth and consistency of effective human tutoring. While these models excel at surface-level language tasks—largely due to their extensive exposure to linguistic patterns during pre-training—they often lack the deeper pedagogical reasoning required for high-quality tutoring.

A key challenge stems from the fact that *effective tutoring is not merely a linguistic task but a pedagogical one*. Human tutors draw on principles such as scaffolding, contingent feedback, and adjustment to a learner’s zone of proximal development. These practices involve strategic choices—varying the specificity of hints, diagnosing misconceptions, guiding the learner through intermediate steps—that cannot be reduced to token-level pattern reproduction. Although pre-training corpora may contain examples of tutoring dialogues, LLMs do not inherently internalize the instructional principles that underlie them.

Compounding this issue is the absence of a unified, operational definition of what constitutes a “good” AI tutor. Recent work has begun to identify desirable behaviours—such as providing relevant hints, maintaining supportive tone, and preserving coherence across turns—but these dimensions remain fragmented, often drawing selectively from tutoring, conversational AI, and general NLP evaluation literature. Importantly, several behavioural traits (e.g., tone, coherence) overlap with established NLP metrics and often improve automatically with model size. In contrast, the ability to *provide pedagogical guidance*—helping learners progress without revelaing answers or solutions immediately—remains uniquely tied to educational theory and substantially under-explored. Improving this behaviour is not only central to effective learning but also essential for closing the gap between human tutors and artificial tutoring systems.

Given its pedagogical significance and the limited methodological tools available to study it, this chapter focuses on the dimension of **Providing Guidance**. To make progress, two challenges must be addressed: (1) evaluating guidance reliably, and (2) improving it meaningfully.

### **1. Need for Better Evaluation: Addressing Construct Validity in LLM-as-a-Judge**

Evaluating an AI tutor’s ability to provide guidance remains a methodological bottleneck. Although the field has widely adopted LLM-as-a-Judge frameworks for assessing model outputs, these approaches raise concerns beyond transparency and bias: **they lack construct validity**. That is, it is unclear whether the judging model is actually measuring the underlying pedagogical behaviour of *guidance*, or whether it is simply responding to surface-level textual cues correlated with “helpfulness.”

Because these judge models were not trained to recognise tutoring strategies, they may reward answers that look helpful but are pedagogically ineffective—for example, responses that provide direct solutions rather than fostering learner thinking. Moreover, proprietary judge models embed unknown preferences, stylistic norms, and training distributions that may not align with educational theory. As a result, existing LLM-as-a-Judge scores risk conflating *linguistic fluency* with *instructional quality*, creating a systematic mismatch between what researchers intend to measure and what is actually being measured.

Human expert evaluation remains the gold standard for assessing pedagogical behaviours, but it is slow, expensive, and difficult to scale. Therefore, there is a clear need for an automatic evaluation method that is transparent, reproducible, theoretically grounded, and explicitly aligned with the pedagogical construct of *guidance*. Study 1 addresses this gap.

### **2. Improving Guidance: Examining Generalization from Instruction Following**

Beyond evaluation, a central scientific question is whether a model’s ability to provide pedagogical guidance can be improved *indirectly* through enhanced instruction-following capabilities. Instruction following underpins many structured reasoning tasks, and improvements here often yield broad performance gains across domains. This raises a plausible hypothesis:
**If guidance can be decomposed into a sequence of contingent instructional steps, then improving instruction following may enable the model to apply those steps more effectively in tutoring contexts.**

There are several theoretical reasons this link might hold:

* Many forms of guidance (e.g., offering hints, prompting self-explanation, breaking problems into subgoals) resemble structured, stepwise instructions.
* Better instruction following may help models adhere more closely to tutor-style directives such as “don’t give the solution,” “ask the learner questions,” or “provide progressively more specific hints.”
* Instruction-following finetuning often improves the model’s ability to handle sequential, multi-step reasoning—an essential component of pedagogical guidance.

However, it is equally plausible that this transfer **may not** occur. Guidance is a fundamentally pedagogical construct: it requires diagnosing learner intent, adapting support contingent on errors, and knowing *when* and *how much* to reveal. These behaviours may involve deeper social-cognitive and pedagogical reasoning that cannot be acquired through generic instruction-following data. If improving instruction following fails to improve guidance, this would indicate that guidance is a *latent pedagogical skill*—one that requires dedicated datasets, targeted finetuning, or specialised training objectives rooted in educational theory.

Study 2 therefore investigates not only whether instruction-following improvements transfer to tutoring behaviour, but also what this reveals about the nature of pedagogical guidance itself. The findings from this investigation will inform whether future AI tutors can be adapted through broad instruction tuning or whether they require **purpose-built pedagogical training** to meaningfully approximate human tutoring strategies.

Accordingly, this chapter is guided by two research questions:

* **How can we automatically and transparently evaluate an AI tutor’s ability to provide pedagogical guidance?**
* **To what extent does improving a model’s instruction-following capabilities enhance its ability to guide learners effectively?**

# Study Design

## Definition
We begin by establishing a more comprehensive working definition of Providing Guidance, which serves as the conceptual foundation for this study. In a tutoring dialogue, or when responding to a student’s question, an effective guiding response does not immediately supply the full answer or solution. Directly providing solutions may prematurely close off valuable learning opportunities. Instead, a guiding response should offer strategic pedagogical support—such as relevant hints, clarifying questions, partial explanations, or conceptual cues—that help the learner progress while still requiring them to engage cognitively with the problem.

Importantly, such guidance enables students to make forward progress without being given the final answer. A well-constructed guiding response therefore preserves productive struggle, nudges the learner toward the correct reasoning pathway, and helps them refine or correct their thinking. Prior literature describes similar concepts using terms such as “helping a student”, “usefulness”, or “actionability”, yet all share the core idea of providing support that is both informative and non-spoiling.

However, as discussed earlier, this tutoring behaviour is deeply human and inherently variable across educators, instructional philosophies, and teaching contexts. As a result, it is not feasible to specify a single, complete operational definition that fully captures the subtlety of guidance in a closed-form equation. Nevertheless, for the purpose of empirical investigation, we attempt to represent and formalize the behaviour of an AI tutor in a structured manner, as follows:

Let:

* $S_t$ denote the **student message** at dialogue turn $t$
* $H_t = {(S_1, R_1), \dots, (S_{t}, R_{t})}$ denote the **dialogue history**
* $R_t$ denote the **tutor (model) response** at turn $t$

The goal of a tutor at turn $t$ is to generate a response $R_t$ that moves the learner closer to the task goal **without fully solving the task for them**.

We define *Guidance* as a mapping from the current dialogue state to a tutor response that optimally balances *support* and *non-disclosure* of the final solution.

$$
\mathcal{Guidance}(H_t, S_t) = R_t^*
$$

where $R_t^*$ maximises:

$$
R_t^* = \arg\max_{R \in \mathcal{R}} \left[\text{Relevance}(R, S_t) + \text{Usefulness}(R, S_t) - \text{Directness}(R, S_t) \right]
$$

with:

* **Relevance**: how directly the response addresses the student’s immediate question
* **Usefulness**: the extent to which the response helps the student make progress
* **Directness**: the extent to which the response *gives away the answer*

A response with **high guidance** is one that has:

* high Relevance
* high Usefulness (e.g., hinting, prompting, scaffolding)
* low Directness (no full solution provided)


## Study 1: Improving Guidance Evaluation (Completed)
In Study 1, we conducted the initial investigation that produced the CODE Framework short paper. This involved constructing and evaluating a set of datasets and experimental protocols designed to isolate behaviours relevant to Providing Guidance. Specifically, Study 1 included:

* Datasets:
Synthetic and real tutoring dialogues designed to probe relevance, indirectness, and scaffolding behaviour.

* Training Scripts:
Procedures for guiding models to exhibit differing levels and types of guidance, enabling systematic comparisons.

* Results:
Quantitative tables and analyses demonstrating that models indeed vary in their ability to provide guidance, and that these behaviours can be meaningfully induced and measured.

Study 1 serves as the empirical and conceptual foundation for the present work by establishing both the feasibility and importance of evaluating guidance in AI tutoring systems.

## Study 2: Investigating the Effect of IF Capabilities on Guidance

Study 2 aims to move beyond evaluation and directly investigate how to *improve* an AI tutor’s Guidance. Given our earlier formalisation, **Guidance** is strongly shaped by a model’s ability to correctly interpret and adhere to high-level tutoring instructions—such as *“do not reveal the answer,” “ask a clarifying question,” “offer a conceptual hint,”* and so on. This leads to the central hypothesis of Study 2:

> **A model with stronger instruction-following (IF) capability will exhibit stronger Guidance, even when the underlying base model remains unchanged.**

To test this hypothesis, Study 2 is organised around two core aims:

1. **Develop and evaluate methods to enhance instruction-following**
   These methods must *not* require parameter updates to the base model, ensuring they remain usable with proprietary LLMs. This includes inference-time or prompt-engineering techniques such as metaprompting, instruction rewriting, chain-of-instructions scaffolding, and lightweight auxiliary checks. The goal of this phase is to create **IF-enhanced variants** of several base models and verify that their instruction-following behaviour improves on standard IF benchmarks.

2. **Test whether IF-enhanced models provide better Guidance on tutoring tasks**
   Using a fixed tutoring dataset, each tutoring prompt will be run through both the **original base model** and its **IF-enhanced counterpart**. This paired-input design ensures that any observed differences in Guidance quality are attributable solely to changes in instruction adherence—not to differences in model architecture, training data, or temperature settings.

---

### **Experimental Setup and Methods**

This section describes the methodology used to test whether improving instruction-following leads to better Guidance in AI tutoring.

### **1. Overview**

Study 2 proceeds in two sequential phases:

### **Phase 1 — Instruction-Following Enhancement**

We apply and evaluate inference-time IF-enhancement techniques on **five base language models**, producing **five corresponding IF-enhanced variants**. Each enhanced variant is validated on instruction-following datasets to confirm measurable improvements in general IF behaviour.

### **Phase 2 — Guidance Evaluation in Tutoring**

For each tutoring input, we generate **paired responses**—one from the base model and one from its IF-enhanced version. These paired outputs are then evaluated for Guidance quality using both:

* **LLM-as-a-Judge protocols**, and
* **human annotations**


## Phase 1: Improving Instruction Following

### Theoretical and Operational Defintion


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

### 1. Instruction-Following Modification

Each $M_i^{\text{IF}}$ is trained with:

* Instruction-following dataset: $\mathcal{D}_{\text{IF}}$
* Chain-of-thought (CoT) augmentation
* Step-adherence reinforcement signals (if applicable)

---

### 2 Instruction-Following Evaluation

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



## Phase 2: Evaluating Tutoring Guidance

We use **192 tutoring dialogue prompts** from:

* **BRIDGE** (strategy-driven tutoring prompts)
* **Unifying AI Tutor Evaluation (BEA 2025)**

Let the tutoring dataset be:


$$
\mathcal{D}_{\text{TUTOR-ORIGINAL}} = \{d_1, \dots, d_{192}\}
$$

Each sample $d_i$ contains:
* Conversation ID $I$ : unique identifier of the conversation sample
* Conversation History $H$ : a problem to solve, plus conversations between a student and a tutor, ending with the student's turn


## 1. Response Pair Generation

Response generation then follows the protocol laid out in **BRIDGE** 

For each sample in ${D}_{\text{TUTOR-ORIGINAL}}$, given a conversation history $H$, we formalize the responses $r$ as being generated from the following computational model:

$$
r \sim p\left(r \mid c_h, \underbrace{e}_{\text{Step 1}}, \underbrace{z_{\text{what}}}_{\text{Step 2}}, \underbrace{z_{\text{why}}}_{\text{Step 2}} \right)
$$

where $e$ is the error, $z_{\text{what}}$ the strategy, and $z_{\text{why}}$ the intention. 

The final response $r$ is generated using 3 steps:

Step 1) Provide a prompt $prompt_{Determine-Error}$, and the conversation history $H$ to a given model to find what the student's error may be -> Finding $e$

Step 2) Provide a different prompt $prompt_{Determine-Strat-Intent}$, and the conversation history $H$ to the same model to find what the best course of action is -> Finding $z_{\text{what}}$ and $z_{\text{why}}$

Step 3) Provide one final prompt $prompt_{Decision-Making}$, and results from Step 1 and Step 2 \( $e$, $z_{\text{what}}$ and $z_{\text{why}}$ \) to produce the response $r$

**All prompts are provided in the repo under GuidanceEval/PromptAndStrat.txt**

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


## 2. Human Evaluation with Stratified Sampling
We want established ground truth label from actual students, but to ensure robustness of the result, we want to have at least 3 annotators so we can filter out any noise of a single annotator. The minimum is 3 to break ties.

However, annotating the entire dataset 3 folds would require extensive time and too much resources. Instead, we do this in two steps, human annotation on samples, then use LLM as a Judge to complete the rest. 

We sample **100 pairs per model**, giving a total of **500 pairs** for human annotation:


$$
\mathcal{P}_{\text{human}} = \bigcup_{i=1}^{5} \mathcal{P}_i^{\text{sample}}, \quad |\mathcal{P}_i^{\text{sample}}| = 100
$$


### 2.1 Stratified Sampling Goals

The human evaluation ensures:

1. **No annotator sees the same pair twice**
2. **No annotator sees pairs from only one model**
3. **Equal representation of all models across annotators**
4. **Each pair is annotated by 3 independent annotators**
5. **Each pair must be seen in a reverse order by at least one annotator to account for positional bias**

### 2.2 Annotator Allocation

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


### 2.3 Pair-Level Constraints

1. **No annotator sees both sides separately**:


$$
A(P_{i,j}) \in \{ r_{i,j}^{\text{base}}, r_{i,j}^{\text{IF}} \}
$$


2. **Each pair has exactly 3 independent annotations**:


$$
|\{ a_k : P_{i,j} \in B_k \}| = 3
$$


### 2.4 Annotator Sourcing and Data Collection

Where to source? Mechanical Turk, Online sourcing, or within University

How to collect? Premade UI or self developed

Compensation? What is the appropriate rate to encourage genuine responses?


### 2.5 Human Preference Score

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


### 2.6 Inter-rater agreement

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

Optional: report per-model κ by restricting J to items in $\mathcal{P}_i^{\text{sample}}$.
Also report bootstrap CIs by resampling items j and recomputing κ.

## 3. Selecting LLM as a Judge of Guidance Preference
To annotate the rest of the dataset, we now pick the best LLM that can function as a judge. Using the data sampled above (N = 500)

### 3.1 Using LLM as a Judge

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

### 3.2 LLM Agreement with Human
Here, we will perform a series of test to see which model can function best as a judge, such that we can use it to annotate the rest of our dataset

#### 1) Basic Count for each model

For each pair $P \in \mathcal{P}_i^{\text{cons}}$, where $\mathcal{P}_i^{\text{cons}}$ is the consistent result of position swapping in LLM as a judge:

$$
J(P)\in\{ 0,1 \}\quad\text{: LLM judge choice (1 if LLM prefers IF-enhanced; 0 if LLM prefers Base).}
$$

$$
h(P)\in\{ 0,1 \}\quad\text{: human majority choice (1 if humans prefer IF-enhanced).}
$$

Aggregate (for model (i)):

$$
C_i = \sum_{P\in\mathcal{P}_i^{\text{cons}}} \mathbf{1}\{ J(P)=h(P) \}
$$

$$
N_i = \lvert \mathcal{P}_i^{\text{cons}} \rvert
$$

$$
n^i_{10} = \sum_{P\in\mathcal{P}_i^{\text{cons}}} \mathbf{1}\{ J(P)=1; h(P)=0 \}
$$

LLM says IF but humans say Base.

$$
n^i_{01} = \sum_{P\in\mathcal{P}_i^{\text{cons}}} \mathbf{1}\{ J(P)=0; h(P)=1 \}
$$

LLM says Base but humans say IF.

#### Report

Table with one row per model:

|    Model (i) | $N_i$ | C_i | (n_{10,i}) | (n_{01,i}) |
| -----------: | ----: | ----: | ---------: | ---------: |
| `model-name` | `N_i` | `C_i` | `n_{10,i}` | `n_{01,i}` |
|          ... |   ... |   ... |        ... |        ... |

---
#### 2) Per-Model Accuracy and Confidence Interval (Is LLM better than chance?)

For each model $M_i$, we perform a baseline assessment of the LLM Judge's agreement with the human majority ($\mathbf{h}$). This checks whether the judge performs significantly better than random chance ($50\%$) when evaluating a specific model pair.

* **Statistic:** Accuracy ($\widehat{\mathrm{Acc}}_i$) is the proportion of predictions where the LLM Judge matches the human majority: $\widehat{\mathrm{Acc}}_i = C_i / N_i$.
* **Confidence Interval:** We use the **Wilson 95% Confidence Interval** for a proportion, which provides a more robust estimate than the normal approximation, especially near the boundary proportions (0 or 1):
    $$
    \text{Wilson CI: }\quad \widehat{p}=\frac{C_i}{N_i},\quad
    \mathrm{CI}_{\text{Wilson}} = \frac{\widehat{p} + \frac{z^2}{2N_i} \pm z\sqrt{\frac{\widehat{p}(1-\widehat{p})}{N_i} + \frac{z^2}{4N_i^2}}}{1 + \frac{z^2}{N_i}},\quad z=1.96.
    $$
* **Hypothesis Test:** We test the null hypothesis that $\text{Accuracy} \le 0.5$ (random judge) using the **Exact One-Sided Binomial Test**:
    $$
    p_i = \sum_{k=C_i}^{N_i} \binom{N_i}{k} \, 0.5^{N_i}.
    $$
* **Decision Rule:** The judge is declared predictive for model $M_i$ if $p_i < 0.05$ and $\widehat{\mathrm{Acc}}_i > 0.5$.

#### What to report

•	$\widehat{\mathrm{Acc}}_i$, Wilson 95% CI, exact binomial one-sided p-value, and raw counts $(C_i, N_i)$.

--- 

#### 3) Per-Model Bias with Systematic Error Check (Is LLM systematically biased?)

#### Why
We check for systematic bias by analyzing the pairs where the LLM Judge and humans disagree (**discordant pairs**). This assesses whether the judge is more prone to favoring the IF-enhanced response or the Base response when it makes an error.

* **Data Used:** Only discordant pairs, where $m = n^i_{10} + n^i_{01}$.
    * $n^i_{10}$: LLM prefers IF, Humans prefer Base (LLM **over-calls IF**).
    * $n^i_{01}$: LLM prefers Base, Humans prefer IF (LLM **under-calls IF**).

* **Bias Test:** The **Exact McNemar's Test** checks if the counts of the two error types are symmetric ($H_0$: $n^i_{10} = n^i_{01}$), modeling $n^i_{10}$ under $\mathrm{Binom}(m, 0.5)$. We use the exact binomial test, or the continuity-corrected $\chi^2$ statistic if $m$ is large:
    $$
    \chi^2 = \frac{(|n_{10}-n_{01}|-1)^2}{n_{10}+n_{01}},\quad \text{(1 d.f.)}
    $$
* **Bias Magnitude:** The **Discordant Odds Ratio** ($\widehat{\mathrm{OR}}$) quantifies the direction and magnitude of the imbalance: $\widehat{\mathrm{OR}} = n^i_{10}/n^i_{01}$. A value significantly greater than 1 indicates a bias toward over-calling IF.

#### Decision rule

•	If exact McNemar $p < 0.05$ and $n^i_{10} < n^i_{01}$ (i.e., LLM under-calls IF less than it over-calls Base) — we may interpret that LLM is not unfairly overcalling IF. If $n_{10} > n_{01}$ and $p < 0.05$, that is evidence the LLM overcalls IF (bias toward IF).

#### What to report

•	$n^i_{10}, n^i_{01}, m$, exact McNemar p-value, $\widehat{\mathrm{OR}}$ + 95% CI. State direction (which error is larger).

---

#### 4) Pooled Inference and Robustness (Final Validation with Dependent Assumption)

This section provides the primary statistical conclusion on the overall reliability of the chosen LLM Judge, explicitly addressing the dependency introduced by using shared conversation prompts.

#### Dependency Correction

To ensure the final claim of the LLM Judge’s overall reliability is robust, we calculate the **Global Accuracy** across all 500 human-labeled pairs and correct the variance estimate for the dependency across models that share the same conversation prompt.

* **The Problem:** The same **192 conversation prompts** are reused across the five models. Since judgments sharing a prompt are correlated (a prompt that is easy to judge for $M_1$ is likely easy for $M_5$), standard CIs and p-values are anti-conservative.
* **Method:** We use **Cluster-Robust Bootstrapping**. This method treats the **Conversation ID ($k$)** as the unit of independence (the cluster), correctly partitioning the variance.
    1.  **Resampling:** $B=5000$ bootstrap samples are generated by resampling the **192 unique Conversation IDs** with replacement.
    2.  **Accuracy Calculation:** The pooled accuracy ($\widehat{\mathrm{Acc}}_{\text{Global}}$) is computed for each of the $B$ bootstrap samples.
    3.  **Inference:** The **Cluster-Robust 95% CI** for the Global Accuracy is determined by the 2.5th and 97.5th percentiles of the resulting bootstrap distribution.

* **Decision Rule:** The LLM Judge is declared globally reliable if the lower bound of the Cluster-Robust 95% CI exceeds $0.5$. We report the overall accuracy and the robust CI.

---

#### 5) Results of LLM-Human Agreement Experiments

This section summarizes the criteria for determining the reliability of the LLM Judge, ensuring both **accuracy** and **lack of systematic bias** are evaluated for individual models and the pooled dataset.

#### Per-Model Reliability Conclusion

For each model $(M_i)$, the LLM Judge is concluded to be **predictive** if it satisfies two complementary criteria:

1.  **(A) Baseline Predictive Accuracy:** The Exact one-sided binomial p-value $(p_i < 0.05)$ and $\widehat{\mathrm{Acc}}_i > 0.5$. This confirms the Judge's raw accuracy is significantly better than chance.
2.  **(B) Absence of Systematic Error:** McNemar’s exact test **$p > 0.05$** (showing no significant error asymmetry); **OR** if $p < 0.05$, the bias must be in the direction of **under-calling IF** ($n^i_{10} < n^i_{01}$).

We report $\widehat{\mathrm{Acc}}_i$, the **Wilson 95% CI**, the exact binomial p-value, and the exact McNemar p-value and **Discordant Odds Ratio** ($\widehat{\mathrm{OR}}$) for all models.

---

#### Overall Pooled Claim Across Models (Dependency Corrected)

The LLM Judge's overall reliability is determined by its **Global Accuracy** across the entire 500-pair human validation set, accounting for the dependency introduced by shared conversation prompts.

* **Primary Metric (Accuracy and CI):** We report the **Global Accuracy** ($\widehat{\mathrm{Acc}}_{\text{Global}}$) along with its **Cluster-Robust 95% Confidence Interval (CI)**, derived from $B=2000$ bootstrap replicates clustered on the **Conversation ID**.
* **Significance Test:** The LLM Judge is declared reliable overall if the **lower bound** of the Cluster-Robust 95% CI is **$> 0.5$** (i.e., significantly better than chance).

---

#### Interpretation Rule

* **Low Inter-Rater Agreement ($\kappa$):** If Fleiss’ $\kappa$ is low ($\kappa < 0.4$), be cautious when interpreting the LLM's agreement with the human majority. This indicates high human disagreement, suggesting the task itself may be ambiguous or highly subjective.
* **High Accuracy + Robust CI ($\text{CI}_{\text{lower}} > 0.5$):** LLM successfully matches human preference patterns across the population of prompts.
* **Significant McNemar with $(n_{10} > n_{01})$:** LLM exhibits a dangerous bias, tending to prefer the IF-enhanced variant even when humans prefer the Base (an **overcall bias**). This LLM Judge must be either discarded or the bias must be statistically controlled for in downstream analysis.

## 4 Annotating the rest of the dataset
After running the above tests, we want to end up with a judge model that can balance accuracy (with sigficant binom test) and the McNemar test to prevent bias

We then use this judge to annotate the entire datasets (remaining 460 samples) so we would then get the full 960 annotated labels of preferred dialogue pairs


## 5. Bayesian Cross-Classified Bradley–Terry Model for Effect Estimation

To estimate the effect of instruction-following (IF) enhancement on AI tutoring guidance, we employ a **Bayesian Cross-Classified Hierarchical Bradley–Terry (BT) model**. This approach explicitly models the effect of the IF enhancement while simultaneously accounting for **variability across models** and **correlation across common conversation prompts**. This ensures accurate uncertainty quantification by partitioning the variance.

### 5.1 Justification for Hierarchical and Cross-Classified Modeling

* **Partial pooling / shrinkage**:
    Some models may have fewer paired observations or noisier preferences. Hierarchical modeling “borrows strength” across models, shrinking noisy estimates ($\alpha_i$) toward the group mean ($\mu$) and reducing overconfidence.
* **Accounting for Data Dependency**:
    By treating the conversation ID ($k$) as a random effect ($\beta_k$), the model correctly controls for the correlation among judgments that share the same input prompt, preventing the overestimation of precision (narrow credible intervals).
* **Robust pooled inference**:
    The posterior over the overall mean effect ($\mu$) gives a principled measure of the average IF enhancement effect across all models, with proper uncertainty quantification.
* **Flexibility**:
    The variance hyperparameters ($\sigma^2$ and $\tau^2$) capture heterogeneity in effects across models ($\sigma^2$) and heterogeneity in judgment difficulty across conversations ($\tau^2$).

---

### 5.2 Model Formulation (Cross-Classified)

Let $M_i$ be the base model and $M_i^{\text{IF}}$ its instruction-following–enhanced variant, for $i = 1,\dots,5$. Let $k$ index the conversation (prompt) used, for $k=1, \dots, n$. For each paired response $P_{i,k} = (r_{i,k}^{\text{base}}, r_{i,k}^{\text{IF}})$:

$$
y_{i,k} =
\begin{cases}
1 & \text{IF-enhanced response preferred} \\
0 & \text{base response preferred}
\end{cases}
$$

We define:
* $\alpha_i$: The **model-specific latent guidance strength** (effect of IF enhancement on model $M_i$).
* $\beta_k$: The **conversation-specific random effect** (bias introduced by the $k$-th input prompt).

The BT probability is now modeled with **two separate latent effects** in the linear predictor:

$$
\Pr(y_{i,k} = 1 \mid \alpha_i, \beta_k) = \frac{\exp(\alpha_i + \beta_k)}{1 + \exp(\alpha_i + \beta_k)}
$$

---

### 5.3 Hierarchical Prior Structure

We place hierarchical priors on both sets of effects. 

1.  **Model-Specific Effects ($\alpha_i$)**:
    $$
    \alpha_i \sim \mathcal{N}(\mu, \sigma^2), \quad i = 1, \dots, 5
    $$
    * $\mu$ = overall mean effect of IF enhancement (pooled effect)
    * $\sigma^2$ = variance of effects across models
    * Hyperpriors: $\mu \sim \mathcal{N}(0, 1), \quad \sigma \sim \text{HalfNormal}(0,1)$

2.  **Conversation-Specific Effects ($\beta_k$)**:
    $$
    \beta_k \sim \mathcal{N}(0, \tau^2), \quad k = 1, \dots, n
    $$
    * $\tau^2$ = variance of conversation effects (captures heterogeneity in prompt difficulty/bias)
    * Hyperprior: $\tau \sim \text{HalfNormal}(0,1)$

---

### 5.4 Likelihood (Conditional on Two Random Effects)

Conditional on the model-specific effects ($\alpha_i$) and conversation effects ($\beta_k$), the likelihood of observed paired preferences $\mathbf{y} = \{y_{i,k}\}$ is:

$$
\mathcal{L}(\alpha_i, \beta_k \mid \mathbf{y}) = \prod_{i=1}^{5} \prod_{k=1}^{192} \Pr(y_{i,k} = 1 \mid \alpha_i, \beta_k)^{y_{i,k}}
\left[1 - \Pr(y_{i,k} = 1 \mid \alpha_i, \beta_k)\right]^{1 - y_{i,k}}
$$

The product now runs over all unique combinations of model pairs ($i$) and conversation prompts ($k$), totaling $5 \times 192 = 960$ individual judgments.

---

### 5.5 Posterior Inference

The posterior over all parameters:

$$
p(\mu, \sigma, \tau, \{\alpha_i\}, \{\beta_k\} \mid \mathbf{y}) \propto \mathcal{L}(\{\alpha_i\}, \{\beta_k\} \mid \mathbf{y}) \cdot p(\{\alpha_i\} \mid \mu, \sigma) \cdot p(\{\beta_k\} \mid \tau) \cdot p(\mu) \cdot p(\sigma) \cdot p(\tau)
$$

Inference is performed using **Hamiltonian Monte Carlo (HMC)** with the **No-U-Turn Sampler (NUTS)**. Draw $S = 4000$ posterior samples for all parameters.

---

### 5.6 Posterior Summaries

The summaries for $\hat{\alpha}_i$, $\hat{\mu}$, and $\hat{\sigma}$ remain the same, but we add a new summary for the conversation variability:

4.  **Across-conversation variability**:

$$
\hat{\tau} = \frac{1}{S} \sum_{s=1}^{S} \tau^{(s)}
$$

$$
\text{CI}_{95\%} = \text{quantile}_{2.5\%}^{97.5\%}({\tau^{(s)}})
$$

* Large $\tau$ → high variance in human preference across different conversation prompts (i.e., some prompts are much harder/easier to score than others).

---

### 5.7 Interpretation

* $\alpha_i > 0$ → model-specific IF-enhanced responses provide superior guidance.
* $\mu > 0$ → IF enhancement improves guidance on average across all models.
* **Credible intervals and posterior probabilities** quantify uncertainty, now correctly adjusted by the $\tau$ parameter.
* $\sigma$ captures cross-model heterogeneity, and **$\tau$ captures cross-conversation heterogeneity**, informing whether certain models or prompts drove the judgment variability.

