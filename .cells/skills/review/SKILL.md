---
name: review
description: Reviews any artifact a cell produced (an intent, a contract, a README, code) against the properties its run defines. Use as β in every cell. Dispatch with one line, "Review runs/<id> at <commit>"; everything else is resolved from the run folder.
metadata:
  version: "0.1.0"
  author: usurobor
  governing_question: "Does the artifact meet every property its run defines, and can any property be met while missing the intent?"
---

# Review

The skill holds the craft; the run holds the data. Properties, tests and
examples come from the run's contract, never from this file.

## 1. Resolve inputs

From `runs/<id>/`:

1. `CONTRACT.md`: the matter under review, the properties, each property's
   "shown by", its ✅/❌ examples, its severity.
2. The intent(s) the contract names, and the owner's words they record.
3. The producer skill the contract names, if any.
4. The matter at the named commit.

Precedence, highest first: owner's words, intent, contract, producer skill.
Where two conflict, report the conflict as a finding. Do not resolve it.

Never read α's reasoning. Read only the matter and α's dispositions.

## 2. Check every property, every round

For each property:

1. **Run its test.** Do what "shown by" says. If the test needs something you
   cannot supply (a fresh reader, the owner), the verdict is **void**, with
   what is needed.
2. **Try to game it.** Construct, in one or two sentences, an artifact that
   passes the test and still misses the property's purpose. If you can, the
   test is weak: report it.
3. **Run what runs.** Code, scripts, links, counts: execute or fetch them.
   Never judge them by reading alone.

Then, across the whole artifact:

4. **Fidelity.** Compare against the owner's words. Flag anything dropped,
   weakened, or added without being marked as proposed.
5. **Producer skill.** Note departures from it as minor. Compliance with a
   skill never makes a property pass.

## 3. Report

One row per property, and nothing else:

| Property | Verdict | Severity | Evidence (one line, quoting the artifact) |
|---|---|---|---|

- **Verdict:** pass, fail, or void.
- **Severity:** blocker (violates the owner's words, the truth, or makes the
  artifact unusable), major (a test can be gamed or cannot be run blind; a
  failure a reader would hit, form included), minor (wording, order).
- Form failures a reader would hit rank with accuracy failures.

Then one line: `VERDICT: APPROVE` (no blocker or major open) or
`VERDICT: REQUEST CHANGES`. No conditional verdicts.
