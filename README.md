This repo is to contain all of the artifacts from our PhD thesis, including datasets, figures, results, scripts, instruments, etc.

This will contain 2 chapters, each corresponding to a big section of the thesis:
* Chapter 1: Improving Guidance via IF enhancement
* Chapter 2: Beyond AI Tutor: How AI enables vs eases students' learning

## Chapter Overviews

### Chapter 1 — Improving Guidance via Instruction-Following (IF) Enhancement
This chapter examines **Providing Guidance** as a core pedagogical capability of AI tutors: producing responses that help students make progress **without giving away the final answer**, preserving productive struggle while remaining relevant and useful. A central motivation is that “good tutoring” is not just linguistic fluency—effective tutors use pedagogical strategies like scaffolding, contingent feedback, and adaptive support, and today we lack scalable, construct-valid ways to evaluate these behaviours in LLM-based tutors.

The chapter addresses two linked challenges:

1) **Better evaluation (construct validity for LLM-as-a-Judge):** We develop more transparent, operational evaluation protocols for tutoring guidance, motivated by the concern that generic judge models may reward answers that *sound* helpful but are pedagogically ineffective (e.g., overly direct solutions).

2) **Improving guidance via IF:** We test the hypothesis that strengthening a model’s **Instruction Following (IF)** capability can improve guidance in tutoring contexts—because many tutoring behaviours can be framed as adherence to constraints like “don’t reveal the solution,” “ask a question,” or “provide a progressive hint sequence.” At the same time, the work explicitly probes whether this transfer holds, given guidance also depends on diagnosing learner errors and adapting to dialogue context.

**How guidance is defined (working formalisation):** Guidance is treated as mapping from dialogue state to an optimal tutor response that balances:
- **Relevance** to the student’s immediate need,
- **Usefulness** for helping them move forward, and
- low **Directness** (avoiding full solution disclosure).

**What’s included (at a high level):**
- **Study 1 (completed):** The evaluation-focused study underpinning the CODE Framework short paper, including datasets (synthetic + real tutoring dialogues), training protocols to induce different guidance behaviours, and analyses demonstrating that guidance varies systematically and can be measured.
- **Study 2:** A paired comparison design testing whether IF-enhancement improves guidance. Five base models are paired with five IF-enhanced variants, and each is evaluated on **192 tutoring prompts** (from **BRIDGE** and **Unifying AI Tutor Evaluation (BEA 2025)**), producing **960 paired outputs**. Guidance quality is assessed using a combination of **human preference judgments** (stratified sampling: 500 pairs, 3 raters each, positional-bias controls) and validated **LLM-as-a-Judge** protocols, followed by effect estimation using a **Bayesian cross-classified hierarchical Bradley–Terry model** that accounts for both model-level and prompt-level variability.

---

### Chapter 2 — Beyond AI Tutor: How AI Enables vs Eases Students’ Learning
This chapter shifts from AI as a “tutor” to AI as a ubiquitous study companion, asking how generative AI is actually reshaping student learning in higher education. While students often report strong enthusiasm and optimism, real-world deployments and observational studies show mixed outcomes across disciplines and contexts—raising the need for empirical, practice-level evidence rather than assumptions about benefit or harm.

**Central research question:**
- *How does the use of generative AI reshape students’ learning practices?*

**Key subquestions:**
1) How do students integrate AI tools with university-provided learning materials (textbooks, lecture notes, LMS content)?
2) Which uses are **enabling** (transformative, opening new learning opportunities) versus merely **easing** (making existing tasks faster/more convenient without changing the underlying learning practice)?

**Theoretical framing:** The chapter uses the **SAMR framework** (Substitution, Augmentation, Modification, Redefinition) as a *sensitising framework* to distinguish:
- **Easing uses** (Substitution/Augmentation): efficiency gains, automation, refinement, or cognitive offloading without pedagogical transformation.
- **Enabling uses** (Modification/Redefinition): genuinely new or transformed learning practices and opportunities.

**Methods: Mixed-methods exploratory sequential design**
- **Phase 1 (qualitative):** Semi-structured interviews (~20 minutes; target ~40 participants or to saturation) to map real usage patterns, the role of institutional materials, perceived benefits/risks, and changes in study behaviour. Analysis combines **inductive thematic analysis**, **theme-level sentiment analysis**, and a **semantic cluster analysis** validity check (embedding + centroid distance) to mitigate single-coder bias. Themes are then classified as enabling vs easing via SAMR.
- **Phase 2 (quantitative):** A large-scale survey (target **≥300 University of Melbourne students**) operationalising Phase 1 themes into measurable constructs: usage prevalence/frequency, enabling vs easing judgments per activity, learning-outcome perceptions (understanding, engagement, performance), integrity concerns, and attitudes/emotions. Planned analyses include descriptive prevalence estimates, subgroup comparisons (e.g., STEM vs non-STEM), correlations between proficiency/usage/outcomes, and exploratory modeling (factor analysis + SEM) to test whether the qualitative theme structure holds statistically and how usage patterns relate to outcomes.

Together, Chapter 2 clarifies where AI’s educational value is truly coming from—and provides evidence to inform both institutional policy and the design of future learning-oriented AI tools.
