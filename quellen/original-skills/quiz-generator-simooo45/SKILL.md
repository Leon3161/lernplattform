---
name: quiz-generator
description: >
  Write or rewrite exam-style multiple-choice questions (MCQ): a stem, a
  set of options, and one correct answer, with distractors that require
  real subject knowledge to eliminate rather than being guessable from
  tone, length, or absurdity. Use when asked to write new quiz/exam
  questions, build or fix a question bank, rewrite weak distractors, or
  when the request mentions "quiz", "MCQ", "multiple choice", "question
  bank", "exam questions", or "distractors".
license: MIT
---

# Quiz Generator

You are writing exam-style MCQs for a subject you know cold, not padding
out a question count. Every option should make a reader who hasn't
studied pause and think — never let tone, length, or an obviously silly
option hand the answer away for free.

## Ground every question in real source material

Never invent a fact. Base each question on the actual reference material
you've been given (textbook, notes, slides, documentation) rather than on
vague generalities. If you're unsure a claim is accurate, check it against
the source before using it in a stem or an option — especially in a
distractor, which has to be *specifically* wrong, not vaguely wrong.

## Writing the stem

- Self-contained: never reference another question's number or "the
  previous question" — question order isn't guaranteed to stay fixed.
- Test one real idea from the source material, not a trivia aside.
- Match whatever formatting conventions the target already uses (Markdown,
  LaTeX, code spans) consistently — check an existing question in the same
  bank before introducing a new convention.

## Writing the options

This is where a weak bank fails. For each option:

1. **Balance length and register.** A generated bank's most common tell:
   the correct option runs noticeably longer (or shorter) than the other
   options, so it stands out without the reader knowing anything. After
   drafting, check the correct option's length against the average of the
   others — target within ~20% (a ratio under ~1.2x either way). Get there
   by writing real, specific wrong answers (below), not by padding: a good
   distractor is exactly as detailed as the correct option because it
   commits to a specific, real-sounding claim. When a distractor comes up
   short, add another concrete, checkable clause of content — never a bare
   intensifier ("entirely", "completely", "whatsoever", "genuinely",
   "purely", "strictly", "classical"). These pad length without adding
   anything a reader needs to know, and several of them quietly signal
   which option "sounds legitimate" — exactly what rule 2 below bans, just
   introduced through the length fix instead of the first draft.
2. **Every distractor must require subject knowledge to eliminate.** Read
   each one and ask: could someone reject this from tone or length alone,
   without knowing the material? If yes, rewrite it. Banned: hardware/
   resource non-sequiturs ("just use a faster CPU"), joke-tier criteria
   ("alphabetical order", "whoever asks first"), an option so extreme it
   answers itself ("always", "never", "with no exceptions" stacked onto an
   obviously-false claim), and a bare "they're the same / no real
   difference" option — if the question asks for a difference, that option
   refutes its own premise for free.
3. **Reach for a role-swap before a denial.** The strongest replacement
   for "X and Y are the same" is: state the same two real facts, but
   attach each to the wrong name (X's real definition mislabeled as Y's,
   and vice versa). It's exactly as long and technical as the correct
   answer, and only wrong if you actually know which is which. Other
   reliable distractor shapes: reverse a direction/inequality, answer a
   subtly different question than the one asked, state a real fact about
   an adjacent concept, over- or under-generalize a real, narrower claim.
4. **Vary which option is correct.** Don't let the correct answer land in
   the same position out of habit.

Self-check before moving on: after writing the question, ask "what's the
right answer?" — if it's obvious at a glance, something's wrong. If you
can spot it cold, a first-time reader can too.

## When rewriting a weak bank

Rewrite the whole question fresh — stem and all options — rather than
patching one distractor at a time. Editing options piecemeal tends to
converge on "plausible content, still an outlier length": the length
problem and the content problem are usually the same root cause, so
fixing only the wording rarely fixes the length balance.

## Verification

`scripts/verify-quiz.mjs` checks a question bank for structural issues
(duplicate ids, wrong option count, out-of-range correct index) and flags
questions where the correct option is a length outlier (the ratio
described above). Zero dependencies, plain Node:

```
node ${CLAUDE_SKILL_DIR}/scripts/verify-quiz.mjs <path-to-questions.json> [expectedOptionCount]
```

Expects a JSON file holding an array of questions shaped like:

```json
[
  {
    "id": "unique-id",
    "question": "stem text",
    "options": ["...", "...", "...", "..."],
    "correct": 0,
    "explanation": "optional, not checked"
  }
]
```

If your bank lives in a JS/TS module instead of plain JSON, export (or
convert) the array to JSON before running the check — the script only
cares about the shape above, not where it came from.

Run it after every batch, before moving to the next set of questions.
Zero errors and a shrinking flagged list is the bar, not a one-shot pass:
rewrite whatever's still flagged and re-run.
