---
name: quiz-generator
description: >
  Generate rigorous multiple-choice practice exams and quiz questions, enforced by a
  research-backed quality gate (distractor plausibility, answer-position balance, option-length
  parity, no stem-echo, no self-undermining qualifiers) and a self-review scoring loop that runs
  before delivery. For reusable practice exams, builds a sized question pool with seen-question
  tracking so retakes surface fresh questions instead of repeating the same set. Use when the
  user asks for a quiz, practice exam, mock exam, test questions, or multiple-choice questions
  on any subject.
---

# quiz-generator

Generate rigorous, hard-to-game multiple-choice practice exams and quiz questions — enforced by a research-backed quality gate and a self-review scoring loop, not ad hoc generation.

## Hard rules — multiple choice quality (non-negotiable)

These came from a real failure: a generated 80-question exam put the correct answer in option B 60+ times out of 80, and most distractors were throwaway options eliminable on sight. Both defeat the purpose of testing — the test becomes a position/length pattern-match instead of actual recall. Independently validated by the educational-measurement literature — Haladyna, Downing & Rodriguez (2002), *A Review of Multiple-Choice Item-Writing Guidelines for Classroom Assessment* (Applied Measurement in Education 15(3)), a taxonomy of 31 guidelines built from consensus across 27 testing textbooks plus 27 empirical studies since 1990 — cited inline below where a specific finding sharpens or extends a rule. Every multiple-choice set this skill produces must follow, in priority order:

1. **Every distractor must be a real, plausible, adjacent concept** — not a throwaway/absurd option included just to fill a slot. Build wrong answers from genuine near-misses: a related command/tool that solves a different layer of the same kind of problem, a real concept that's commonly confused with the correct one, a true statement about something adjacent that doesn't actually answer the question asked. A test-taker who half-knows the material should be able to talk themselves into the wrong answer — that's what makes a distractor do its job. This is the foundation: no rule below matters if the wrong answers aren't real.
   - **Consistency over uniform perfection:** one weaker distractor per question is acceptable; multiple is not. Haladyna & Downing's (1993) analysis of real exam items found the *typical* multiple-choice question has only one distractor that actually functions — gets chosen often enough to discriminate between test-takers who know the material and those who don't. Two-thirds of the four-option items they studied had just one or two functioning distractors; none of the five-option items had four. The failure mode isn't having a weak option — that's normal — it's having **two or more** in the same question, which turns it into a coin flip among the obviously-wrong-eliminated remainder. Self-check: for each question, ask how many of the three distractors are doing real work. One carry is fine. Two or three is the violation.
2. **Balance correct-answer position across all options roughly evenly.** Before finalizing a question set, count how many times each letter/index is correct. Across N questions there should be roughly N/4 of each (for 4-option questions) — never let any single position dominate. Do not default to writing the most-detailed reasoning into one consistent slot (e.g. always "B") — that becomes a length tell even without checking letters.
3. **Match length and specificity across all four options — check this even after fixing position.** This bit twice in practice: positions got balanced across A/B/C/D, but the correct answer still won on sight because its option text carried a full "because X, since Y, unlike Z" reasoning clause while distractors were short bare claims — a 27-question set measured out to the correct answer averaging 100+ characters longer than the others on 25 of 27 questions. Balancing position alone does not fix this; it's a separate axis.
   - **The fix:** keep the option text itself to a short claim — roughly the same length as a distractor — and move the "why it's correct / why the others are wrong" reasoning into the explanation field, which exists for exactly this purpose and is already shown after the user answers.
   - Give each distractor a brief justification clause too (e.g. "...since X" / "...because Y"), even if the justification is the plausible-but-wrong reasoning a half-informed test-taker would use. This keeps all four options at comparable length and grammatical shape, not just the correct one.
   - **Verify, don't eyeball it:** before delivering, measure each option's character length against the other three in its question. If the correct answer is consistently 20+ characters longer across many questions, it's still a length tell even if positions are balanced — go back and trim.
4. **Don't let the question stem name the correct answer.** Two failure patterns, both real: (a) the question asks "why is X the right construct here" — naming X before the options even appear, making the question pure recall-confirmation instead of a real test. Rephrase to "which construct fits this best, and why" so the test-taker has to actually pick X, not just justify a given. (b) a distinctive word or phrase from the question stem (e.g. "fastest," "no need for battery runtime") gets reused verbatim in only the correct option — a test-taker can match on that shared word without knowing the material. Validated directly by the literature's Guideline 28 ("clang associations" — option wording echoing the stem). After drafting, scan each question for words appearing in both the stem and exactly one option; if found, paraphrase the option (or the stem) to break the verbatim overlap while keeping the same meaning. **This check has to be re-run after every later edit pass, not just the first draft** — a question that was clean got a stem-echo reintroduced when it was later rewritten for an unrelated reason (length-fix touched the option text, put a phrase from the stem back into it). Re-scan the whole set after any edit pass, not just the questions that were directly touched.
5. **All four options must read with equal confidence — no option gets to argue with itself.** This is the tone equivalent of the length-bias problem: a distractor written as "...relying on credential strength **alone**," "...which doesn't **actually** segment traffic," "...**despite** SecureBoot already being on," or "...**treating this as** a disk issue" is pre-hedging its own wrongness. If the correct option is left as a clean, unqualified statement while three distractors carry built-in disqualifiers, a test-taker can pick the one answer that doesn't undercut itself without knowing the content at all. Found at scale (15-20 of 80 questions) in a set that had already passed the position/length/stem-echo checks — this is a distinct axis, not caught by any of the rules above, and the subtlest of the five tells here: it's been the last one caught every time.
   - **The fix:** every option — correct or not — should read as a plausible, confidently-stated claim. Hedge words and self-undermining qualifiers ("alone," "despite," "treating this as," "doesn't actually," "merely") belong in the explanation field if they're needed to articulate why something is wrong, not inline in the option text itself.
   - **Verify by reading just the options, not the question:** if you can identify the correct answer from tone/confidence alone without reading the stem, the distractors are under-hedged relative to the correct option. Rewrite until all four are equally flat, equally confident statements.
6. **Use scenario/application questions, not bare recall, for intermediate+ difficulty.** "What does X do" is 基础 (basic). "A user reports Y symptom, which of these explains it" forces actually reasoning through the concept rather than pattern-matching a memorized definition.
7. **State the central idea in the stem, not the options.** The single highest-endorsed guideline in the item-writing literature — 100% textbook agreement across the 27 testing textbooks Haladyna et al. reviewed. A stem should make the test-taker hold one real question in mind; a stem that just gestures at a topic and pushes the actual question down into four mini-questions in the options is the named failure mode ("unfocused stem").
   - **Word the stem positively.** Avoid NOT/EXCEPT-style negation. If it's genuinely unavoidable, bold or capitalize the negative term so it can't be skimmed past under time pressure.
   - **Cut window dressing.** Strip stem verbiage that doesn't change what's being asked. A longer stem isn't a harder question, just a slower one to read.
8. **Self-check before delivering:** after drafting a set, tally correct-answer positions (rule 2), skim each question's four options for length parity (rule 3), scan for stem-echo (rule 4), check distractor tone parity (rule 5), and confirm no question has two or more non-functioning distractors (rule 1's consistency clause). If skewed, physically reorder options (move the correct text to a different index, shift others to fill the gap) rather than rewriting from scratch — this preserves the explanation text, which references the answer dynamically and doesn't need to change.

## Self-review loop

Run this gate after drafting any question set and before delivering or writing to file. **Score → list violations → fix → repeat until clean.**

1. **Score the set 0–100.** One point deducted per violation found. Violations to check:
   - *Per-question:* ≥2 non-functioning distractors in a single question · correct answer 20+ characters longer than alternatives · verbatim stem word appears only in the correct option · self-undermining qualifier (alone, despite, doesn't actually, treating this as, merely) in any option text · bare-recall phrasing on an intermediate+ difficulty question
   - *Across the set:* any position (A/B/C/D) holds more than N/4 + 2 correct answers

2. **List every violation** by question index and rule number (1–8 above).

3. **If score < 100:** fix only the flagged questions — reorder options for position, trim/expand for length, paraphrase for stem-echo, remove qualifiers for tone. Do not touch passing questions.

4. **Re-score only the changed questions.** Repeat from step 2 until the full set is clean, then deliver.

**HTML exams:** run this loop on the POOL/QUESTIONS array data before encoding it into the HTML file. Fixing raw data takes seconds; patching rendered HTML takes minutes.

## Delivery format

**Default (conversational quiz/explanation requests):** Deliver questions **one at a time** — present a single question, wait for the user's answer, give immediate feedback (correct/incorrect + brief explanation), then move to the next question. Never batch all questions into one message.

**Practice exam / drill test requests for this vault:** When the request is for a practice exam, mock exam, or drill test meant to be taken interactively and reused, deliver it as a **self-contained interactive HTML file** instead of chat-delivered Markdown, per `me.md`'s "Flashcards/quizzes use interactive HTML" rule. Follow this pattern for all pool-based HTML exams:
- Single HTML file, no external dependencies, inline `<style>`/`<script>`
- One question rendered at a time with a progress bar, score-so-far counter, and a results screen with a missed-questions review list
- `QUESTIONS` array of `{q, o:[...4 options], c:<correct index>, e:<explanation>}` objects — render options dynamically from the array (never hardcode option order in the DOM), so reordering for balance is a one-line data change
- On reaching the results screen, save `{pct, score, total, missed, date}` to `localStorage` keyed by a stable per-quiz string — use a short topic prefix plus `document.title`, e.g. `'quiz_results::' + document.title`. Show a dismissible "last completed result" banner on reload if a saved result exists — "Retake exam" must still always start fresh regardless of any saved result
- Save the file into the relevant subject folder under `Projects/`, not as a chat artifact only

**Question pool & sampling (for reusable practice exams):** Applies whenever the source material exceeds one attempt's worth of questions — mixed/combined exams spanning multiple sub-topics, or any single-topic exam with enough question content that one sitting wouldn't use all of it. A static, fixed-order `QUESTIONS` array is wrong for these: retaking the exam must not just reset the score counter and replay the identical list. A working example of this pattern lives at `Projects/Career & Certs/CompTIA A+ Core 2/A+ Core 2 Full Practice Exam (Mixed Domains).html` — refer to it for concrete structure, but follow the pattern described here rather than inheriting its A+-specific configuration.
1. Build a `POOL` array holding every available question, each tagged with a category field (e.g. `d:"D1 — Operating Systems"`). Size the pool to whatever source content actually exists — don't pad to or cap at a fixed number.
2. Define a single `const ATTEMPT_SIZE = N` — the number of questions per attempt. Per-category targets are derived automatically from pool composition: `Math.round((categoryPool.length / POOL.length) * ATTEMPT_SIZE)`. This is self-calibrating — a pool built to reflect real topic coverage will naturally produce the right weights without manual configuration. Rounding means actual attempt size may vary by ±(number of categories); this is acceptable and already handled by updating `#totalQ`/`#totNum` from `QUESTIONS.length` (see item 6). Optional: define a sparse `DOMAIN_WEIGHTS` map to override specific category counts when official weights differ significantly from pool composition (uncommon).
3. Add a Fisher-Yates `shuffle(arr)` helper (in place, returns the array).
4. Add a `sampleExam()` function: group `POOL` by category, derive each category's target proportionally (`Math.round((categoryPool.length / POOL.length) * ATTEMPT_SIZE)`), `shuffle()` each category's slice, take the target count from each, concatenate, then `shuffle()` the combined result once more. This becomes that attempt's `QUESTIONS`. If `DOMAIN_WEIGHTS` overrides are defined, use the override count for that category instead of the proportional calculation.
5. Assign `let QUESTIONS = sampleExam();` on initial load — never a hardcoded literal array.
6. Inside `restart()`, reassign `QUESTIONS = sampleExam();` before resetting `current`/`score`/`missed` and re-rendering. Re-sampling on retake (not just on first load) is the entire point — without it "Retake exam" just replays the same set, which is the bug this pattern fixes. Update any displayed total-question count (e.g. `#totalQ`, `#totNum`) from the new `QUESTIONS.length` too, since pool sampling can make attempt size vary if targets don't sum to a fixed total.

**Seen-question tagging (add to all pool-based exams):** After the sampling pattern is in place, add seen-question filtering so retakes draw from unseen questions first rather than the full pool.

7. Add a `SEEN_KEY` constant (placed *before* the `let QUESTIONS = sampleExam()` call so it's initialized when `sampleExam` first runs): `const SEEN_KEY = 'quiz_seen::' + document.title;` — use the same topic prefix chosen for `RESULTS_KEY` so all keys for a given file share a consistent namespace.
8. Add four helpers — declare them as `function` declarations (not arrow functions / `const`) so they hoist past the `sampleExam()` call:
   ```js
   function getSeenSet() {
     try { return new Set(JSON.parse(localStorage.getItem(SEEN_KEY) || '[]')); }
     catch(e) { return new Set(); }
   }
   function markSeen(q) {
     const s = getSeenSet(); s.add(q);
     localStorage.setItem(SEEN_KEY, JSON.stringify([...s]));
   }
   function resetSeen() { localStorage.removeItem(SEEN_KEY); }
   function getFreshCount() {
     const seen = getSeenSet();
     return POOL.filter(q => !seen.has(q.q)).length;
   }
   ```
9. Modify `sampleExam()` to prioritize unseen questions per category, falling back to seen ones only if a category runs low. Uses proportional targets — no `DOMAIN_TARGETS` needed:
   ```js
   function sampleExam(){
     const seen = getSeenSet();
     const byDomain = {};
     POOL.forEach(q => { (byDomain[q.d] = byDomain[q.d] || []).push(q); });
     let picked = [];
     Object.keys(byDomain).forEach(d => {
       const domPool = byDomain[d];
       const target = Math.round((domPool.length / POOL.length) * ATTEMPT_SIZE);
       const fresh = shuffle(domPool.filter(q => !seen.has(q.q)).slice());
       const stale = shuffle(domPool.filter(q => seen.has(q.q)).slice());
       const take = fresh.slice(0, target).concat(stale.slice(0, Math.max(0, target - fresh.length)));
       picked = picked.concat(take);
     });
     return shuffle(picked);
   }
   ```
10. Call `markSeen(item.q)` in both places a question is resolved — in `selectAnswer()` immediately after `answered = true;`, and in the skip handler inside the `if(!answered)` guard before incrementing `current`.
11. Add a `<span>Fresh: <b id="freshCount">?</b> of N</span>` element to the header stats row (where N is the total pool size). In `updateStats()`, add `document.getElementById('freshCount').textContent = getFreshCount();` — this keeps the counter live as questions are answered.
12. In `renderResults()`, replace the single "Retake exam" button with a two-button row: one standard retake (keeps seen history, so the *next* attempt continues filtering) and one "Reset seen & retake" that calls `resetSeen()` then `restart()`. Use a flex wrapper div for layout. Add the corresponding `.restart-row { display:flex; gap:.75rem; justify-content:center; margin-top:1.5rem; }` CSS rule.

## Building a POOL from unstructured source material

When the source is raw notes, a textbook chapter, a doc, or any material that doesn't arrive pre-tagged with categories:

1. **Identify natural topic clusters** — section headers, concept groups, or subject areas in the source. Use those as `d` values. Aim for 3–6 categories: fewer than 3 loses the weighted-sampling benefit entirely; more than 6 makes individual category pools too small to sample meaningfully across retakes.
2. **If no meaningful clusters exist**, tag all questions `d: "General"` — proportional sampling then reduces to flat sampling automatically, with no special-case code needed.
3. **Size the pool to the source** — generate as many questions as the material supports. Don't cap at a round number. The seen-question filter only provides real benefit when the pool is meaningfully larger than ATTEMPT_SIZE; aim for at least a 3:1 ratio (e.g. ATTEMPT_SIZE 30 → pool of 90+) to get value across multiple retakes.
4. **Category balance matters more than pool size.** A pool of 200 questions split 190/5/5 across three categories is effectively a single-category pool — the two thin categories will exhaust quickly and fall back to stale questions on the second retake. Build categories with roughly proportional depth, or consolidate thin ones.
