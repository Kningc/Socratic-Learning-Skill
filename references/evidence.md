# Design evidence and provenance

This file explains the non-obvious decisions in `SKILL.md`. It is maintenance context, not required reading during an ordinary tutoring session.

## Source project

The initial inspiration is [lmonkt/ostep-socratic-tutor](https://github.com/lmonkt/ostep-socratic-tutor). Its core materials describe a question-driven AI tutor anchored to an electronic textbook, with practice, later review, optional progress records, and optional tutor personas for motivation. The repository's `main` branch is primarily a set of articles and a bootstrapping prompt rather than a reusable tutor implementation.

This Skill retains the portable instructional ideas and deliberately leaves out its OSTEP-specific curriculum, fictional relationship system, diary/group-chat machinery, PDF conversion choice, and Claude-specific project setup.

## Why the Skill behaves this way

- **Deep questions and source-grounded explanation:** The U.S. Institute of Education Sciences practice guide recommends prompts that elicit deep explanations, quizzing, spaced review, worked-example/problem pairs, and integration of abstract and concrete representations: [Organizing Instruction and Study to Improve Student Learning](https://ies.ed.gov/ncee/wwc/practiceguide/1).
- **Retrieval and spacing:** Dunlosky et al.'s review rates practice testing and distributed practice as high-utility learning techniques across varied learners and materials: [Improving Students' Learning With Effective Learning Techniques](https://doi.org/10.1177/1529100612453266).
- **Constructive dialogue:** The ICAP framework predicts stronger learning as engagement moves from passive toward active, constructive, and interactive behavior. This supports prediction, self-explanation, generation, and genuine dialogue rather than passive summaries: [Chi & Wylie, 2014](https://doi.org/10.1080/00461520.2014.965823).
- **Adaptive scaffolding:** The Education Endowment Foundation recommends subject-embedded planning, monitoring, evaluation, modeling, and scaffolds that are reduced as independence grows: [Metacognition and Self-Regulated Learning](https://educationendowmentfoundation.org.uk/education-evidence/guidance-reports/metacognition%20).
- **Open-ended Socratic discussion:** Yale's Poorvu Center describes Socratic discussion as open-ended questioning around a particular text or artifact and emphasizes substantive responses to both good and flawed ideas: [Effective Class Discussion](https://poorvucenter.yale.edu/teaching/teaching-resource-library/effective-class-discussion).

These sources support ingredients, not a universal script. The one-question rhythm, five-level hint ladder, two-prompt escalation threshold, and material playbooks are practical design choices intended to keep dialogue usable and prevent unproductive withholding. They should be revised if real use reveals a better policy.
