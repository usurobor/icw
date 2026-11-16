# Doc iteration protocol — 0.0.3

## Purpose

A dialogue determines what the next version should be. Owner and models build
shared understanding by iterating one versioned doc. Outputs render from it.

## Rules

1. One canonical doc. Every turn starts from the latest version.
2. In chat, the doc travels in a code block. Reasoning, questions and pushback
   stay outside it.
3. Every turn that changes the doc bumps the version and adds a changelog line.
4. Versions start at 0.0.1. Before 1.0.0, every iteration bumps the patch.
   1.0.0 is the owner accepting the doc as a whole. After 1.0.0: major, an
   accepted item reversed or removed; minor, an item added; patch, wording
   only.
5. Every item has a status: open, proposed or accepted. Only the owner sets
   accepted.
6. A turn built on a stale version is rebased onto the latest before it
   counts.
7. Outputs (README, post) live in their own doc, with their own version, and
   name the understanding version they render.
8. Automation runs only on accepted items; its job is to improve them.
9. Automation may reword an accepted item, never change its meaning. Meaning
   changes come back as proposals.
10. A pinned thesis stays word for word at the core. Caveats go after it,
    never in its place. A defensive edit that weakens it is a meaning change.

## Open

- Q1: Does an edit to an output flow back as a proposed source change?
- Q2: In git, what triggers a model turn: an owner push, a schedule, or both?
- Q3: Does an automated turn only propose on a branch, or may it commit?

## Changelog

- 0.0.3 Rules 8–10 (17 Nov 2026, README dialogue).
- 0.0.2 Rule 4: pre-1.0 is patch-only; 1.0.0 is owner acceptance.
- 0.0.1 Initial, 16 Nov 2026.
