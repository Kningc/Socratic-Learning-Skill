# Long-form book and course mode

Use this mode when the learner wants to complete a substantial book or course, resume over multiple sessions, follow dependencies, retain progress, or combine reading with exercises and labs. Keep ordinary one-off sessions stateless.

## Use a minimal startup gate

Before asking questions, inspect the request, available material, conversation, and any existing `.socratic-learning/` state that the learner has authorized the agent to read.

If compatible state exists and the learner asks to continue, resume from it without repeating onboarding. If several courses or incompatible states could apply, ask which one to use before changing anything.

For a new course, resolve missing information in this priority order, but ask only what matters now:

1. **Scope and continuity:** focused session or sustained course. Ask only when the request is ambiguous.
2. **Persistent state:** required for reliable cross-session progress. Before the first write, name the proposed directory and files and obtain approval. An explicit request to save, track, resume, or build a persistent course already grants this approval.
3. **Learning outcome:** ask when exam preparation, conceptual mastery, practical competence, or close reading would produce meaningfully different routes. Otherwise begin with a provisional general-mastery goal and refine it later.
4. **Source identity:** ask about edition, revision, or scope only when multiple versions are present or the difference affects anchors, exercises, or correctness.
5. **Practice and labs:** ask when including executable work would materially change setup, cost, permissions, or time. Otherwise introduce the choice when the first relevant module arrives.
6. **Pace:** do not block the first lesson for a schedule. Start adaptively and ask later if deadlines or workload become consequential.

Ask at most one setup question per turn. Do not ask for information already supplied, preferences that can be inferred safely, or details that can wait. Once enough is known, briefly state the assumed frame and begin the first diagnostic or course-mapping action in the same turn when practical.

Examples:

- “Help me understand chapter 5” is a focused session; inspect it and begin without asking about persistence.
- “Help me finish this book over three months” clearly selects long-form mode; if saving was not mentioned, ask once before creating the proposed state directory.
- “Build a course and track my progress” already authorizes persistent course state; do not ask for the same permission again.
- “Continue where we stopped” with one compatible state should resume directly and surface the current target and due reviews.

When a question is necessary, make the decision concrete rather than asking for an open-ended biography. Useful shapes include:

- `Do you want one focused session on this section, or a course that continues across sessions?`
- `May I create <state-directory> with the course map, learner state, and session log?`
- `Should this route optimize mainly for conceptual mastery, an exam, or practical exercises?`

Do not create state merely because the material is long. If tracking is approved, use a `.socratic-learning/` directory in the learner's study workspace unless they choose another location.

Initialize the state by copying and completing these templates:

- `assets/course-state/course-map.md`
- `assets/course-state/learner-state.md`
- `assets/course-state/session-log.md`

Never write learner state inside the installed Skill directory. Preserve existing state and ask before replacing an incompatible course setup.

## Build a course map

Inspect the table of contents and the actual available materials. Map modules, concepts, prerequisites, source anchors, exercises, labs, and assessment points. Mark which items are essential, supporting, or optional according to the learner's goal. Do not claim complete coverage from a table of contents alone.

Record source provenance: title, edition or revision, files or URLs, access date when relevant, supplemental sources, and known errata. Distinguish textbook claims from corrections and outside explanations. When sources change, update the register and identify any affected course-map items.

Create an initial route rather than an immutable schedule. Revise it when diagnostic evidence shows that prerequisites, pace, or goals differ from the initial assumptions.

## Track learning with evidence

Use qualitative states tied to observable evidence:

- `not-started`: no meaningful evidence;
- `introduced`: encountered and discussed;
- `practiced`: succeeded with material or support;
- `demonstrated`: explained or applied independently in a new case;
- `review-due`: prior evidence exists but retrieval is due;
- `remediate`: a misconception or prerequisite gap is active;
- `skipped`: intentionally excluded from the declared goal, with the reason recorded.

Do not convert confidence or conversational fluency into mastery. Record a brief evidence note and source anchor for every `demonstrated` judgment. A failed delayed retrieval can move an item back to `remediate` without erasing its history.

Maintain three separate concerns:

- the course map records intended coverage and dependencies;
- learner state records current evidence, misconceptions, and review queue;
- the session log records a compact chronological audit trail.

## Resume efficiently

At the start of a later session, read the course map, current learner state, due review items, and only the relevant recent log entries. Then state the current location, one or two due callbacks, and the proposed target. Do not reload the entire book or complete conversation archive.

Treat the state files as the canonical cross-session memory. If conversation memory conflicts with written state, inspect the evidence and reconcile it explicitly rather than silently choosing one.

## Run a course session

Choose and name the mode when it affects expectations:

- **guided dialogue** for constructing a new conceptual model;
- **rapid review** for a small batch of retrieval or discrimination items;
- **exercise or lab** for solving, running, observing, and debugging;
- **assessment** for independent performance with feedback deferred until the checkpoint ends;
- **remediation** for repairing a specific misconception or prerequisite.

A typical session draws from this sequence without forcing every step:

1. Retrieve one or two due ideas without reopening the source.
2. Establish the session target and its dependency on prior material.
3. Teach through the appropriate material playbook.
4. Require an application, exercise, experiment, or interpretation.
5. Finish with synthesis or transfer and update the state.

Keep scope small enough to reach meaningful evidence. Depth is not coverage if essential sections are repeatedly skipped; coverage is not mastery if every item is merely marked introduced.

## Schedule review adaptively

Add important new or fragile ideas to the review queue. Use a simple starting cadence when real dates are available: next session, roughly 3–7 days, 2–4 weeks, then 2–3 months. Treat these as defaults, not promises.

After successful effortful retrieval, lengthen the interval and vary the prompt or context. After failure, correct the misconception, obtain an immediate successful attempt, shorten the next interval, and change the question rather than repeating the exact wording. Mix a few older items into later chapters when they illuminate current material.

## Handle exercises, simulators, and labs

Treat executable material as part of the curriculum, not an appendix.

1. Verify the exercise source, environment, command, inputs, and expected kind of output.
2. Ask the learner to predict the behavior or result before execution when useful.
3. Let the learner attempt the task; inspect their actual code, command, output, trace, or artifact.
4. Diagnose whether the gap is conceptual, strategic, representational, mechanical, or environmental.
5. Apply the normal hint ladder, then rerun or retest to obtain observable evidence.
6. Ask the learner to interpret why the result occurred and how it would change under a nearby condition.

Do not fabricate execution results. Follow the host's normal permission and safety rules, especially for destructive commands, external services, credentials, or costly operations. Do not expose a hidden reference solution verbatim before a reasonable attempt unless the learner explicitly asks for it; after a direct solution, require explanation or near transfer.

Record completed labs with the artifact or command used, result, interpretation, and unresolved issues. A successful command without an accurate interpretation is not sufficient evidence of conceptual mastery.

## Assess cumulative understanding

Use several checkpoints rather than one final test:

- chapter checkpoints sample essential concepts and include a new application;
- module checkpoints integrate concepts across chapters and revisit older prerequisites;
- cumulative checkpoints require selection among competing concepts, not only recall;
- a final assessment samples explanation, application, error analysis, and transfer aligned with the learner's stated goal.

Separate tutoring from assessment. During a declared assessment, do not provide hints until the learner submits or exits assessment mode. Afterward, diagnose errors, update the evidence state, and create targeted remediation—not just a score.

## Compact state without losing learning history

At session end, update current location, coverage changes, evidence, active misconceptions, review items, and next step. Append only a compact session entry: target, activities, evidence, unresolved issue, and planned callback.

When the session log becomes unwieldy, move older entries to an archive file and retain a short index. Do not summarize away recurring misconceptions, reversals in mastery, source-version changes, or evidence supporting completion decisions.

## Decide completion

A book or course is complete only relative to the learner's declared goal. Check that essential course-map items have independent evidence, required exercises or labs are finished, review debt is acceptable, and a cumulative transfer task has succeeded. Report optional or intentionally skipped material separately rather than presenting it as covered.
