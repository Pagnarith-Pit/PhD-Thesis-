Below is a **clean, rigorous, and flexible formalisation** of *Providing Guidance* that fits your study and can be used to motivate IndirectScore or any evaluation framework. It is written in a style suitable for an EMNLP/ACL paper or a PhD thesis.

I give you **one core formal definition**, and then **three alternative formulations** (behavioural, functional, probabilistic) you may choose from depending on what fits your chapter best.

---

# **Proposed Formal Representation of “Providing Guidance”**

We begin with the tutoring setting.

Let:

* ( S_t ) denote the **student message** at dialogue turn ( t )
* ( H_t = {(S_1, R_1), \dots, (S_{t}, R_{t})} ) denote the **dialogue history**
* ( R_t ) denote the **tutor (model) response** at turn ( t )

The goal of a tutor at turn ( t ) is to generate a response ( R_t ) that moves the learner closer to the task goal **without fully solving the task for them**.

---

# **1. Core Formalisation (Recommended)**

We define *Guidance* as a mapping from the current dialogue state to a tutor response that optimally balances *support* and *non-disclosure* of the final solution.

[
\mathcal{G}(H_t, S_t) = R_t^*
]

where ( R_t^* ) maximises:

[
R_t^* = \arg\max_{R \in \mathcal{R}}
\left[ \alpha \cdot \text{Relevance}(R, S_t)

* \beta \cdot \text{Usefulness}(R, S_t)

- \gamma \cdot \text{Directness}(R, S_t)
  \right]
  ]

with:

* **Relevance**: how directly the response addresses the student’s immediate question
* **Usefulness**: the extent to which the response helps the student make progress
* **Directness**: the extent to which the response *gives away the answer*

(\alpha, \beta, \gamma > 0) are weights representing pedagogical priorities.

A response with **high guidance** is one that has:

* high Relevance
* high Usefulness (e.g., hinting, prompting, scaffolding)
* **low Directness** (no full solution provided)

This makes *Providing Guidance* explicitly a **three-way tradeoff** that your evaluation metric can measure.


