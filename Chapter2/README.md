# Motivation
Beyond their application as a tutor, since the release of large-scale generative AI models, the higher education sector has been repeatedly identified as one of the domains poised to benefit most profoundly from these technologies. Academic literature has highlighted the potential of generative AI to expand access to personalised feedback, enhance student support, reduce administrative burdens, and provide scalable tutoring capabilities across diverse disciplines. As a result, universities worldwide have faced strong calls from researchers, policymakers, and industry to integrate AI into teaching and learning environments in meaningful ways.

Yet, despite these optimistic projections, a growing counter-movement has emerged, warning against uncritical or extensive adoption of AI in education. Critics argue that generative AI may foster over-reliance, enable academic misconduct, disrupt the development of critical thinking, and reduce opportunities for meaningful peer interaction and engagement within classrooms. Some educators also express concerns about cognitive offloading, arguing that if AI tools are used to bypass effortful thinking—such as solving exercises, generating explanations, or producing writing—students may experience long-term erosion in analytical and problem-solving skills. These opposing narratives have created a polarised discourse in which AI is simultaneously framed as a transformative educational innovation and a potentially harmful shortcut.

If one side of this debate is to ultimately prevail, the true benefits and harms of AI must be empirically established rather than assumed. Surprisingly, however, large-scale institutional adoption remains limited. This is particularly puzzling given that a broad body of non-experimental research—primarily surveys and interviews conducted across diverse geographical regions—reports overwhelmingly positive attitudes toward AI among university students. Students consistently describe AI tools as convenient, accessible, and beneficial for understanding complex content, clarifying concepts, and supporting their studies. These findings might lead one to expect rapid and widespread adoption of AI-driven educational practices.

Instead, studies involving real student usage paint a much more complex and inconsistent picture. In controlled or course-embedded deployments, some disciplines—most notably computer science and programming—report high student engagement with AI assistants and clear preferences for studying with AI support. Students in these fields often describe AI as a “debugging companion,” a “coding partner,” or a “24/7 tutor,” suggesting that AI meaningfully enhances their learning experience. Conversely, other disciplines show low uptake or limited interest in using AI for learning tasks, even when students are familiar with the technology. In some humanities and social science contexts, for example, students express concerns about the accuracy, relevance, or disciplinary appropriateness of AI-generated outputs, leading to cautious or minimal adoption.

Complicating matters further, several recent studies have adopted a more naturalistic, observational approach by analysing students’ real chat logs with AI systems. Unlike controlled experiments, these studies do not restrict the types of questions students can ask or the timeframe of usage. Instead, they capture authentic, everyday interactions. Findings from such analyses reveal that a substantial portion of student queries are not aligned with deep learning goals. Many interactions involve asking AI for direct answers to homework questions, generating assignment-ready content, or using AI for convenience-based tasks rather than meaningful cognitive engagement. Other interactions are unrelated to academic work altogether, involving personal, professional, or entertainment-oriented queries. These observations challenge the assumption that enthusiastic attitudes towards AI necessarily translate into beneficial or pedagogically sound usage patterns.

Together, these contradictions raise a critical question about where the actual educational value of generative AI lies. If student attitudes are overwhelmingly positive, yet real-world usage varies widely and often gravitates toward shallow or non-academic activities, then institutions cannot assume that AI will automatically enhance learning. Understanding the real value of AI is essential not only for justifying its incorporation into everyday university learning environments but also for guiding strategic institutional investment. Moreover, insights into how students genuinely use AI are vital for developers of educational AI systems, who must align their tools with what meaningfully benefits students rather than what is simply convenient or superficially appealing.

These concerns motivate the central problem addressed in this research: although generative AI has rapidly become ubiquitous, its actual impact on students’ learning practices remains unclear. Without a grounded, empirical understanding of how AI reshapes the everyday routines, strategies, and behaviours of university students, the sector risks designing policies, technologies, and teaching practices based on assumptions rather than realities.

## Research Question
Thus, the key research question guiding this study is:

How does the use of generative AI reshape students’ learning practices?

To examine this question, the study further investigates the following subquestions:

1) In what ways do students integrate AI tools with university-provided learning materials (such as textbooks, lecture notes, and LMS content)?

2) What types of learning activities or outcomes are enabled by AI tools, and which are simply eased—made more efficient or convenient—without fundamentally transforming the underlying learning process?

Through addressing these questions, this research aims to illuminate the real, rather than presumed, role of generative AI in contemporary university education and to provide evidence-based guidance for institutions, educators, and developers navigating this rapidly changing landscape.

# Preliminary Study
Here, investigate the adoption of AI tutor at the University of Melbourne. Talk about our effort in first year attempt at COMP90059. Describe

### Study Design
recruitment strategy - subject coordinator endorsement, training video, personal introduction at tutorials and lectures, tutors reminders
target population
compensation - none, volunteer basis, annonymised data

### Technical Report
Web interface
Web URL access link and hosting infrastructure
Weekly tutorial embedding
Chat area

### AI features
Socratic tutor
Progressive hints

### Results
Low adoption, only 10 sign ups, 162 collected conversation threads, averaged around 3 conversation lengths
confirmed through chatlogs- reasons for dropoffs include requesting for answers or move on request, denoting frictions 

# Methods

This study adopts a mixed-methods Exploratory Sequential design, integrating qualitative and quantitative research to develop a comprehensive understanding of how university students incorporate generative AI tools into their learning practices. The decision to employ an exploratory design reflects the emerging and understudied nature of day-to-day AI use in higher education. While substantial policy discussions and conceptual debates surround AI in learning, empirical evidence capturing how students actually use AI remains limited. Combining qualitative exploration with quantitative validation therefore enables both openness to new patterns and the ability to evaluate their generalisability across a larger population.

### Theoretical Framework

Past research on AI in education has predominantly relied on frameworks such as:

* Technology Acceptance Model (TAM)

* Self-Regulated Learning (SRL)

* Unified Theory of Acceptance and Use of Technology (UTAUT)

* Technology–Task Fit (TTF)

These models have been valuable for assessing perceived usefulness, ease of use, and self-efficacy, yet they offer limited insight into the specific sources of value students derive from AI. In other words, these frameworks explain whether students find AI helpful, but not how or why it changes their learning.

To address this gap, the present study draws on the Substitution, Augmentation, Modification, and Redefinition (SAMR) framework. SAMR provides a structured way to distinguish between:

* Easing uses (defined in original study as enhacement): Sub and Augment, where AI substitutes or augements tasks without changing or little change to learning practices, and

* Enabling uses (defined in original study as transforming) : Mod and Redefine, where AI introduces fundamentally new learning opportunities or transforms how tasks are approached.

SAMR is therefore uniquely suited to evaluating whether AI enhances education in a pedagogically meaningful way or merely accelerates or outsources existing tasks. This distinction is especially relevant given current debates on academic integrity, cognitive offloading, and the risk of over-reliance on AI.

We explicitly use SAMR as "sensitising framework". A sensitising concept helps us notice relevant things without determining what the data must be. This means that SAMR is used to guide question creation, but then analysis are performed inductively without forcing data into a predefined model. After themes emerge, we then apply SAMR deductively for final interpreation. 

The original SAMR by Puentedura (2009, 2020), however, is too narrow and leaves too much room for interpretation, making it hard to accurately code usages to each level. Instead, this study will use (Crompton & Burke, 2020) extended definition for clear differentiation of each level:

<img width="668" height="595" alt="Screenshot 2025-12-15 at 4 10 31 pm" src="https://github.com/user-attachments/assets/8b94a4aa-9f3b-4e34-9e26-4878151177ab" />


### Justification for Exploratory Design 

Mixed-methods research has been widely adopted in educational technology studies when the aim is to understand both the complexity of human behaviours and the general prevalence of patterns (Creswell & Plano Clark, 2017). Because generative AI is a novel and rapidly evolving tool, student usage has not yet stabilised into predictable or well-defined patterns. Consequently, qualitative inquiry is essential to uncover behaviours, use cases, and perceptions that existing theories or surveys might overlook.

The two phases of this study are designed to function as an integrated exploratory–confirmatory sequence, where qualitative insights from Phase 1 directly inform and structure the quantitative investigation in Phase 2. Phase 1 generates conceptual categories of AI usage through semi-structured interviews, allowing students to describe their behaviours, strategies, and perceptions in their own words. These emergent themes are interpreted through the SAMR framework, which sensitises the analysis to distinctions between uses that enable new learning practices (Modification/Redefinition) and those that ease existing tasks (Substitution/Augmentation). This approach ensures that the qualitative exploration remains inductive, capturing the full range of student experiences, while also producing theoretically meaningful categories that can guide further measurement.

Phase 2 translates these Phase 1 themes into quantifiable constructs within a large-scale survey. Each usage category identified qualitatively becomes a survey item or cluster of items, allowing measurement of its prevalence, frequency, and perceived impact across a broad and diverse student population. SAMR-aligned enabling and easing distinctions inform the coding of these survey responses, providing a consistent lens for interpreting which behaviours represent pedagogically significant transformation versus efficiency-focused convenience. By operationalising qualitative findings in this way, Phase 2 serves as a validation and generalisation step, testing whether patterns observed in the exploratory sample are evident at scale.

Finally, qualitative and quantitative results are integrated through a joint inferential framework. Convergence is assessed where Phase 2 data support Phase 1 themes, demonstrating stability and generalisability of usage patterns. Complementarity is established where qualitative insights explain the mechanisms behind quantitative trends—for example, how specific enabling uses contribute to self-reported understanding or engagement. Divergence is examined where Phase 2 outcomes differ from Phase 1 expectations, highlighting areas where emergent behaviours may not translate into measurable learning outcomes. Together, this analytical integration ensures coherence across the study, linking theory, empirical observation, and interpretation, and providing a comprehensive understanding of how generative AI reshapes students’ learning practices in higher education.

In the section below, we provide the design of each phase of study in more detail. 

## Qualitative Study (Phase 1)
The initial qualitative phase aims to identify the actual ways students integrate generative AI into their everyday coursework. The objective is to generate categories of usage, explore their underlying motivations, and understand whether students experience these practices as transformative or merely convenient.

### Study Design
Data will be collected through semi-structured interviews, each lasting approximately 20 minutes. Semi-structured interviews are chosen because they balance flexibility—allowing students to describe their usage in their own terms—with comparability across participants. This format is particularly appropriate for exploratory technology research, where unknown behaviours may emerge during conversation.

#### Instruments

A custom interview guide will be developed, guided by past SAMR work. Topics will include:

* Concrete examples of recent AI usage within coursework

* Interactions between AI tools and university-provided materials

* Students’ perceived benefits, challenges, and risks

* Perceived changes in study behaviour since adopting AI

* Perceived necessity of AI for certain tasks

The interview guide will be piloted with 2–3 students to ensure clarity and appropriateness.

#### Additional Data to Collect
To contextualise the results and enable later comparison across subgroups, participants will also provide:

* name and email address: only to report findings or contact for any required changes to data. Not used for any analysis
* Year level: to explore whether senior students use AI differently
* course: to account for known differences between STEM and non-STEM use patterns
* self-rated AI familiarity: account for how well students are familiar with their capabilities 
* english level proficiency: studies have reported AI used for translation. Could be indicator here since University of Melbourne is English speaking instritution

#### Recording and Transcription
Interviews will be audio-recorded with participants’ consent. Transcription will be performed using contemporary speech-to-text models known for high accuracy in educational settings. If consent for recording is not granted, detailed notes will be taken instead.

---

### Participants
Participants will be active undergraduate or postgraduate students at the University of Melbourne. Because interviews are conducted in English, participants must demonstrate adequate English proficiency. To ensure relevance, students must have used generative AI at least once in the past six months.

The study will aim for approximately 40 participants or until thematic saturation is reached. This sample size is consistent with exploratory qualitative research where the goal is to map the space of behaviours rather than achieve statistical proportionality.

Recruitment will occur through:

* Flyers posted around campus

* Announcements made in subjects with the support of coordinators

* Personal networks and referrals

All potential participants will receive information about the study’s aims, interview topics, data retention policies, confidentiality protections, result disemmination strategy, and the ethics approval for this project. Participation will proceed only after informed consent is obtained, with sufficient time to review all documents. Participants will be compensated at a pro-rated rate of $50 per hour.

---

### Data Analysis
Two complementary analytical approaches will be used: sentiment analysis and thematic analysis, followed by a computational check using semantic cluster analysis.

#### Sentiment Analysis

Sentiment analysis provides a preliminary quantitative assessment of the emotional tone of participants’ discussions about AI. This is particularly useful given that self-reported attitudes may be influenced by social desirability or normative pressure in higher-education environments. Automated sentiment scoring offers a consistent and unbiased method for identifying whether students’ experiences are broadly positive, negative, or neutral. It also helps detect patterns of enthusiasm, frustration, or ambivalence that might correlate with specific uses of AI.

##### **Step A: Annotate each response by usage type**

* During coding, assign each participant response to a theme (e.g., “concept explanation,” “debugging,” “assignment outsourcing”) from our thematic analysis.
* Each theme should also have its SAMR label: enabling vs easing.

##### **Step B: Sentiment at the theme level**

* Perform sentiment analysis on each response within a theme.
* Then, **aggregate sentiment per theme for each participant** rather than across the entire interview.

**Example:**

| Participant | Theme                 | SAMR     | Sentiment Score |
| ----------- | --------------------- | -------- | --------------- |
| P1          | Concept Explanation   | Enabling | +0.8            |
| P1          | Assignment Completion | Easing   | -0.1            |
| P2          | Debugging             | Enabling | +0.5            |

This keeps the affective tone tied to **specific AI usage patterns**, which is much more informative for interpretation.

* With this, we can answer questions like:

  * Are enabling uses associated with more positive sentiment than easing uses?
  * Do participants express frustration when using AI for certain tasks?
  * Does sentiment correlate with perceived learning impact?

* For a visual or analytical summary, thinking to create heatmaps:

  * X-axis: Usage type/theme
  * Y-axis: Sentiment score
  * Color: SAMR category (enabling/easing)
This allows quick inspection of which tasks students enjoy or dislike and whether enabling uses are more positively experienced.


#### Thematic Analysis

The main analytic process will involve inductive thematic analysis, chosen because it aligns with the exploratory goal of identifying emerging patterns without forcing responses into predefined categories.

Procedure: 

1) Initial coding

Each interview transcript will be read closely, and segments describing specific AI-related behaviours will be given short descriptive codes (e.g., "summarising lectures", "debugging code", "checking grammar"). Coding will be iterative and evolve as new patterns emerge.

2) Code refinement and grouping

Related codes will be examined and clustered into broader categories or subthemes. These may include categories like “efficiency-driven use,” “task outsourcing,” “conceptual clarification,” or “creativity support.” (Examples only; actual themes will emerge from data.)

3) Theme generation

The subthemes will then be grouped into overarching themes that capture core dimensions of how students apply AI in their study routines.

Because the coding will be conducted by a single primary researcher, the study incorporates an additional computational validity check.


#### Sematic Cluster Analysis (Bias Mitigation)

To reduce potential coder bias and strengthen the reliability of the thematic structure, the study will use semantic cluster analysis:

* Each individual usage example (coded excerpt) will be embedded using a modern text-embedding model.

* A centroid will be computed for each theme.

* Distances between each usage example and all theme centroids will be calculated.

* Instances where the assigned theme is not the nearest centroid will be flagged for review.

This method, commonly used in topic modelling and clustering research, allows a systematic, data-driven check on whether usage descriptions are grouped coherently.

#### Enabling vs. Easing Coding

After identifying themes, each will be evaluated through the lens of the SAMR framework:

* Enabling (Modification/Redefinition):
AI is used in a way that introduces new learning behaviours or capabilities not previously possible. These reflect AI’s potential as a transformative educational technology.

* Easing (Substitution/Augmentation):
AI is used to speed up, automate, or refine existing tasks without fundamentally changing the form of the learning activity. These uses suggest AI may be helpful but not pedagogically significant.

This stage is essential for interpreting not just how students use AI, but whether those uses align with meaningful learning enhancement. It also directly contributes to ongoing debates about whether AI’s benefits outweigh its risks, particularly when uses lean toward convenience or task outsourcing rather than conceptual development.

## Quantitative Study (Phase 2)
Building on the qualitative insights generated in Phase 1, Phase 2 aims to evaluate the generalisability, prevalence, and educational significance of students’ AI usage patterns across a larger and more diverse student population. While Phase 1 identifies how students use AI and why they perceive certain benefits, Phase 2 examines how widespread these behaviours are, how they vary across demographic and academic groups, and whether different forms of AI use (enabling vs. easing) are associated with meaningful learning outcomes. This phase serves to validate the qualitative findings, quantify their distribution, and provide empirical evidence to guide institutional policy and pedagogical decisions.

Phase 2 transforms the rich qualitative insights from Phase 1 into quantifiable, testable constructs, enabling:

* Large-scale validation of usage patterns
* Identification of population-wide trends
* Insights into enabling vs. easing practices
* Evidence-based recommendations for university AI policy
* Clear implications for designing future AI-based educational tools

## **Participants**

The target population mirrors that of Phase 1 but expands its scope to achieve statistical power and representativeness.

### **Who**

Participants will include:

* Undergraduate and graduate students enrolled at the University of Melbourne.
* Students from all faculties (STEM and non-STEM) to capture disciplinary variation in AI use.
* Students who have used generative AI tools (e.g., ChatGPT, Claude, Gemini, GitHub Copilot) within the past six months, ensuring responses reflect current habits and not outdated behaviours.

No restrictions will be placed on age, residency status, or academic standing.

### **Sample Size**

The study aims to recruit **at least 300 participants**.
This sample size is chosen to:

* Enable stable estimation for multivariate analyses (e.g., regression, cluster analysis).
* Provide statistical confidence when comparing subgroups (e.g., STEM vs non-STEM; novice vs expert AI users).
* Ensure adequate representation of diverse AI usage patterns identified in Phase 1.

### **Recruitment**

Recruitment will occur through multiple channels to ensure broad reach:

* Learning Management System (LMS) announcements with support from course coordinators.
* Flyers posted in student spaces.
* Email invitations via faculty mailing lists where permissible.
* Social media posts within university-affiliated groups.
* Snowball sampling, where participants may share the study link with peers.

Participants will receive detailed information about the study’s aims, data handling procedures, risks, and consent requirements prior to participation.


## **Study Design**

Phase 2 uses a cross-sectional online survey, administered via Google Forms, allowing efficient distribution to a large number of students and enabling data collection within a consistent and structured format.

### **Instrument**

A survey instrument will be developed based on:

1. **Themes and usage types identified in Phase 1 thematic analysis**, including:

   * Concept explanation
   * Assignment/task support
   * Brainstorming
   * Code debugging or walkthroughs
   * Study planning and organisation
   * Translation or language clarification
   * Personal or non-academic use

2. **SAMR-aligned enabling/easing classifications** derived from Phase 1.

3. **Sentiment patterns** identified earlier (e.g., positive, negative, neutral orientation towards AI).

4. **Established constructs** from learning sciences and technology adoption literature, such as:

   * Perceived usefulness
   * Self-regulated learning behaviours
   * Cognitive offloading tendencies
   * Perceived academic integrity risks
   * AI literacy or proficiency

Items will be primarily Likert scale (1–5), with some categorical and open-ended fields to capture nuanced responses.

### **Data Collected**

The survey will collect multiple categories of data to support rich quantitative analysis:

---

### **1. Demographic and Academic Background**

* Faculty/discipline (STEM, humanities, commerce, health sciences, etc.)
* Level of study (undergraduate, graduate, PhD)
* Year level
* Domestic vs. international status
* English language proficiency (self-rated)
* Prior academic performance (self-reported average grade band)

Purpose: To examine how AI usage differs across student groups and educational contexts.

---

### **2. AI Familiarity and Usage Profile**

* Frequency of AI use (daily, weekly, monthly)
* Duration of AI use (in months/years)
* Self-rated AI proficiency
* AI tools used (ChatGPT, Gemini, Claude, Copilot, Perplexity, others)

Purpose: Controls for familiarity and exposure.

---

### **3. AI Usage Behaviours (Based on Phase 1 Themes)**

Participants will rate how often they use AI for each usage category identified qualitatively, e.g.:

* Explain difficult concepts
* Summarise lectures or textbooks
* Translate or simplify text
* Generate ideas or brainstorm
* Assist with assignments
* Debug programming tasks
* Review writing
* Organise study plans
* Provide emotional or motivational support
* Non-academic personal tasks

Purpose: To quantify usage prevalence and identify usage clusters.

---

### **4. SAMR-Aligned Enabling vs. Easing Classification**

For each usage activity, students will be asked:

* Whether AI allowed them to perform a task they *could not do before* (enabling/transformation)
* Whether AI primarily made the task *faster or easier* (easing/substitution)

Purpose: To measure the degree of pedagogical transformation and evaluate the educational significance of AI use.

---

### **5. Perceived Learning Outcomes**

Students will rate:

* Perceived understanding of concepts when using AI
* Confidence in completing tasks
* Engagement with course materials
* Self-reported academic performance changes
* Over-reliance concerns
* Perceived risks to academic integrity

Purpose: To link AI use to meaningful learning indicators.

---

### **6. Attitudes, Sentiments, and Emotional Orientation**

Based on Phase 1 sentiment patterns, students will respond to items capturing:

* Trust in AI tools
* Enjoyment or frustration when using AI
* Anxiety about misuse or errors
* Overall positivity or negativity toward AI

Purpose: To understand emotional drivers of behaviour.

---

### **7. Open-Ended Questions**

A small number of optional open-ended questions will capture nuance, e.g.:

* “Describe a time AI significantly improved your learning.”
* “Describe a time AI negatively affected your learning or engagement.”


## **Analysis Plan**

Phase 2 will use a combination of descriptive, inferential, and exploratory statistical analyses:

**Notation:**
  * $n$ = number of participants (target $\ge 300$)
  * $K$ = number of usage themes from Phase 1
  * $E_{ik}$ = participant $i$'s enabling/easing score for theme $k$
  * $E_i = \frac{1}{K} \sum_{k=1}^{K} E_{ik}$ = overall enabling/easing score
  * $U_{ik}$ = usage frequency for theme $k$ (Likert 1–5)
  * $P_i$ = self-rated AI proficiency (1–5)
  * $S_i$ = subgroup membership (STEM/non-STEM, coded 0/1)
  * $Y_i$ = learning outcome variables (perceived understanding, engagement, self-reported performance, etc.)

Missing data will be handled via pairwise deletion or multiple imputation; scales will be standardized as needed $\tilde x = (x-\bar x)/s_x$.

### **1) Descriptive Statistics**

---

### 1.1) Prevalence of each usage pattern

#### **Why This Is Important**

Our qualitative study identified specific usage patterns (e.g., conceptual explanation, summarisation, translation, debugging, assignment completion). The quantitative phase needs to determine:

* Which usage patterns are **common enough** to represent institutional trends
* Which patterns are **emerging behaviours** worth supporting
* Which patterns are **educationally concerning** (e.g., asking AI for answers)

This helps universities and AI tool designers prioritise interventions, support, or guardrails.

#### **How to Interpret the Results**

* **High prevalence** → indicates stable, generalisable behaviours.
* **Moderate prevalence** → suggests context-dependent usage.
* **Low prevalence** → may mean the behaviour is rare, discipline-specific, or emerges only under special circumstances.

If a theme from Phase 1 shows up rarely in Phase 2, we plan to discuss this as:

> “A behaviour observed in qualitative data but not widely generalisable at scale.”

**Inputs:** Usage frequency $U_{ik}$ (1–5)

**Formula:**

* Binary use indicator: $B_{ik} = \mathbf{1}(U_{ik} \ge 2)$
* Count per theme: $n_k = \sum_{i=1}^{n} B_{ik}$
* Prevalence proportion: $\hat p_k = n_k / n$
* 95% CI: $\hat p_k \pm z_{0.975} \sqrt{\hat p_k (1-\hat p_k)/n}$

**Outputs:** Table of counts, proportions, 95% CI; bar charts per theme

### 1.2) Frequency distributions

#### **Why This Is Important**

AI usage behaviours may not be uniformly distributed. Frequency distributions should allow us to observe patterns such as:

* Heavy-tailed usage (a minority use AI extensively)
* Bimodal distributions (groups of avoiders vs. enthusiasts)
* Normal or near-normal patterns (uniform adoption across the student population)

These insights are critical for designing targeted interventions and understanding heterogeneity within the student body.

**Inputs:** $U_{ik}$

**Formula:**
$
\Pr(U_k = r) = \frac{1}{n} \sum_{i=1}^n \mathbf{1}(U_{ik} = r), \quad r \in {1,2,3,4,5}
$

**Outputs:** Histograms, mode, median, IQR for each theme

#### **How to Interpret the Results**

* **Right-skewed** → many light users, few heavy users.
* **Left-skewed** → many heavy users, few light users.
* **Bimodal** → students are polarised; large groups either enthusiastically adopt or avoid AI.
* **Normal distribution** → indicates stable, homogeneous adoption patterns across the population.

This helps the argument of whether AI adoption is **diffuse or polarised**.

### 1.3) Mean scores for enabling vs. easing behaviours

#### **Why This Is Important**

Our thesis will focus on the distinction between:

* **Enabling behaviours** = transformative learning practices
* **Easing behaviours** = efficiency or shortcut-based uses

Mean scores help to quantify *how much* AI is reshaping learning.

#### **How to Interpret the Results**

* **Higher enabling score** → AI is genuinely transforming learning (aligns with SAMR “Modification/Redefinition”).
* **Higher easing score** → AI is primarily used as a substitute or shortcut (aligns with SAMR “Substitution”).
* **Comparable scores** → mixed uses; AI supports both efficiency and transformation.

This connects well to the main research question:

> *How is AI reshaping learning practices?*

**Inputs:** $E_i$ per participant

**Formula:**
$
\bar E = \frac{1}{n} \sum_{i=1}^{n} E_i, \quad SE(\bar E) = s_E / \sqrt{n}
$

where
$
s_E = \sqrt{\frac{1}{n-1} \sum_{i=1}^n (E_i - \bar{E})^2}
$ 

**Outputs:**

* Mean, SD, SE, 95% CI: $\bar E \pm t_{n-1,0.975} SE(\bar E)$
* Boxplots by subgroup (STEM vs non-STEM, year level, etc.)

### **2) Inferential Tests**

---

### 2.1) Comparisons between groups (t-tests)

#### **Why This Is Important**

We'll examine whether particular student groups differ in their AI usage:

* STEM vs. non-STEM
* Undergraduates vs. postgraduates
* Domestic vs. international students
* High-AI-proficiency vs. low-proficiency users

This helps identify **who benefits most** and where targeted support may be necessary.

#### **How to Interpret the Results**

* **Significant differences** → group membership meaningfully shapes AI use or AI-derived outcomes.
* **Non-significant differences** → behaviours are consistent across demographic or academic groups, suggesting broader generalisability.

Examples:

* If STEM students use enabling AI tools more → this supports the idea that procedural/technical domains benefit differently.
* If international students rely more on translation → this has implications for inclusivity and language support.

**Formula:**
$
t = \frac{\bar E_1 - \bar E_0}{\sqrt{s_1^2/n_1 + s_0^2/n_0}}
$

**Outputs:** t-value, df, p-value, Cohen’s d, 95% CI

### 2.2) Correlations between AI proficiency, usage types, and outcomes

#### **Why This Is Important**

The conceptual model constructed assumes that factors like AI proficiency, usage style, and perceived outcomes are related. Correlations show:

* Whether relationships exist
* Whether these relationships are positive or negative
* How strong they are

#### **How to Interpret the Results**

* **Strong positive correlation** (e.g., enabling use ↗ and perceived learning gain ↗) → enabling AI behaviours are pedagogically beneficial.
* **Strong negative correlation** (e.g., easing use ↗ and engagement ↘) → surface-level use may be detrimental.
* **Weak correlation** → behaviours are independent or context-specific.

Correlations should further support theorisation of *how AI use reshapes learning*.

**Inputs:** $E_i, P_i, U_{ik}, Y_i$

**Formula (Pearson):**
$
r_{XY} = \frac{\sum_i (X_i - \bar X)(Y_i - \bar Y)}{\sqrt{\sum_i (X_i - \bar X)^2 \sum_i (Y_i - \bar Y)^2}}
$

**Outputs:** Correlation matrix, p-values, heatmaps; optionally Spearman for ordinal variables

### **3) Structural and Exploratory Analyses**

---

Unlike the formulas above, in this step, we'll be using SmartPLS software for Factor Analysis and SEM modelling.

### **3.1) Factor analysis**

**1) When it should be used**

Treat a SAMR level (Substitution, Augmentation, Modification, Redefinition) as a latent variable only when it is represented by at least 3–4 observed usage themes.

This ensures the factor is identifiable, meaning the model can reliably separate the underlying latent construct from random variation.

If a SAMR level has fewer than 3 themes, it should be treated as a simple observed average of the available themes rather than latent.

**2) What we are measuring**

The latent SAMR construct estimates the true pedagogical impact of AI usage at that level.

It captures the underlying tendency for students’ reported AI activities to align with the intended educational effect (e.g., Substitution = easing existing tasks; Redefinition = enabling new learning opportunities).

This approach compensates for the fact that students may not accurately self-assess the educational significance of each activity — the latent factor aggregates across multiple themes to provide a more robust estimate of impact.

So when doing factor loading, expect to see 4 factors. Then a valid Phase 1 assignment would mean that all themes assigned to Substitution loads on one factor highly and less on others. 


#### **Why This Is Important**

Factor analysis tests whether the themes from Phase 1:

* Are statistically real
* Cluster together in coherent dimensions
* Represent valid, measurable constructs

This strengthens the legitimacy of the qualitative findings.

#### **How to Interpret the Results**

* **Loadings > 0.40** → strong association with the factor
* **Clear factor structure** → Phase 1 themes are valid
* **Cross-loadings** → behaviours may overlap
* **Poor structure** → themes may require reconceptualisation

This helps bridge qualitative and quantitative insights.

### **3.2) Path models (SEM)**


#### **Why This Is Important**

Path modelling allows us to test *causal pathways* implied by theory:

* Does AI proficiency lead to more enabling use?
* Does usage type mediate learning outcomes?
* Does discipline influence outcomes through usage patterns?

This produces a theoretically grounded explanation of student behaviour.

#### **How to Interpret the Results**

* **Significant mediated pathways** → support claim that usage style drives outcomes.
* **Non-significant paths** → challenge assumptions about how AI influences learning.
* **Good model fit indices** (CFI > 0.90, RMSEA < 0.08) → the theoretical model aligns well with the empirical data.

This ties the entire thesis together by showing how AI reshapes learning in a structured, causal manner.

----

Together, these analyses determine:

* Whether Phase 1 themes hold statistically
* Which AI practices carry genuine educational value
* Where risks (over-reliance, shallow learning) are concentrated
* How different student populations interact with AI


