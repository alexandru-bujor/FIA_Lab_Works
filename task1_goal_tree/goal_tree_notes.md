# Task 1 — Goal Tree Notes

This file is the plain-English draft of the goal tree, before it becomes
actual rules in Task 2. For each tourist type, fill in the same four steps
used in the Earther Sightseer example below.

## Shared base facts (apply to every tourist, before splitting by type)

- moves with an unadapted, awkward gait
- speaks with an Earther accent
- is unfamiliar with Loona's corridors

IF (all shared base facts) THEN (is a tourist)

## Loonie facts (the other side of the top-level split)

- moves with a fast, adapted gait
- is at least 1.8m tall
- has a straight posture
- has a lean build
- supports lunar autonomy
- reacts negatively to repatriation talk

IF (all Loonie facts, or an appropriate subset) THEN (is a Loonie)

---

## WORKED EXAMPLE — Earther Sightseer

**Step 1 — shared base:**
- moves with an unadapted, awkward gait
- speaks with an Earther accent
- is unfamiliar with Loona's corridors

IF (all of the above) THEN (is a tourist)

**Step 2 — type-specific clues:**
- constantly photographs/records everything
- asks about tourist attractions
- reacts with exaggerated amazement to low gravity
- this is their first time off-world

**Step 3 — combined rule:**
IF (is a tourist)
   AND (constantly photographs everything)
   AND (asks about tourist attractions)
   AND (reacts with exaggerated amazement)
   AND (this is their first time off-world)
THEN (is an Earther Sightseer)

**Step 4 — AND vs OR check:**
Decide whether any of the four specific clues are substitutable for each
other (OR) rather than all strictly required (AND). Note your decision and
reasoning here.

---

## Belt Miner on Leave

**Step 1 — shared base:** (same three shared tourist facts)

**Step 2 — type-specific clues:**
- has calloused hands from manual work
- is completely unfazed by space/vacuum environments
- wears a mining company patch or uniform
- uses rough, casual space-worker slang

**Step 3 — combined rule:**
IF (is a tourist)
   AND (has calloused hands)
   AND (is unfazed by vacuum environments)
   AND (wears a mining company patch)
THEN (is a Belt Miner on Leave)

**Step 4 — AND vs OR check:**
"uses rough space-worker slang" is dropped from the strict AND and treated as
a supporting/optional clue rather than required — slang habits vary more than
visible gear or manner, so it's not reliable enough to gate the conclusion on.

---

## Corporate Auditor

**Step 1 — shared base:** (same three shared tourist facts)

**Step 2 — type-specific clues:**
- wears formal business attire
- checks the time frequently, visibly impatient
- carries a briefcase or documents
- shows no interest in sightseeing

**Step 3 — combined rule:**
IF (is a tourist)
   AND (wears formal business attire)
   AND (carries a briefcase or documents)
   AND (shows no interest in sightseeing)
THEN (is a Corporate Auditor)

**Step 4 — AND vs OR check:**
"checks the time frequently" is folded into an OR with "shows no interest in
sightseeing" — both point at the same underlying trait (task-focused,
impatient), so requiring both is redundant.

---

## Honeymooners

**Step 1 — shared base:** (same three shared tourist facts)

**Step 2 — type-specific clues:**
- travels as an affectionate couple
- asks about romantic/scenic locations
- purchased a zero-gravity novelty package
- wears a visible wedding/engagement ring

**Step 3 — combined rule:**
IF (is a tourist)
   AND (travels as an affectionate couple)
   AND (wears a visible wedding/engagement ring)
   AND (asks about romantic locations OR purchased a zero-gravity novelty package)
THEN (is a Honeymooner)

**Step 4 — AND vs OR check:**
"asks about romantic locations" and "purchased a zero-gravity novelty
package" are OR'd together — either is sufficient evidence of the same
romantic-getaway intent, so requiring both would be too strict.

---

## Rock-hound Collector

**Step 1 — shared base:** (same three shared tourist facts)

**Step 2 — type-specific clues:**
- asks unusually technical questions about lunar minerals
- carries specimen bags or containers
- wants to visit non-touristy geological sites
- shows geology knowledge beyond a typical visitor

**Step 3 — combined rule:**
IF (is a tourist)
   AND (asks technical questions about lunar minerals)
   AND (carries specimen bags or containers)
   AND (wants to visit non-touristy geological sites)
THEN (is a Rock-hound Collector)

**Step 4 — AND vs OR check:**
"shows geology knowledge beyond a typical visitor" overlaps heavily with
"asks technical questions" — kept as supporting evidence rather than a
separate required condition, to avoid double-counting the same trait.

---

## Repatriation Relative

**Step 1 — shared base:** (same three shared tourist facts)

**Step 2 — type-specific clues:**
- is looking for a specific named Loonie resident
- talks about "coming home" or Earth family
- shows visible emotional tension
- gets a hostile reaction back if the resident pushes back on leaving Luna

**Step 3 — combined rule:**
IF (is a tourist)
   AND (is looking for a specific named Loonie resident)
   AND (talks about "coming home" or Earth family)
   AND (shows visible emotional tension)
THEN (is a Repatriation Relative)

**Step 4 — AND vs OR check:**
The fourth clue (hostile reaction from the resident) is not part of the
tourist-classification rule itself — it's a fact about the *Loonie's*
reaction, not the tourist. Note this separately as a follow-on fact that
could feed into a Loonie's "reacts negatively to repatriation talk" rule
from the other branch of the tree, rather than into this rule's IF clause.

---

## Summary — all six types at a glance

| Type | Core distinguishing clues |
|---|---|
| Earther Sightseer | photographs everything, asks about attractions, amazed by gravity, first time off-world |
| Belt Miner on Leave | calloused hands, unfazed by vacuum, mining patch/uniform |
| Corporate Auditor | formal attire, briefcase/documents, no interest in sightseeing |
| Honeymooners | affectionate couple, wedding ring, romantic/novelty package interest |
| Rock-hound Collector | technical mineral questions, specimen bags, seeks non-touristy geological sites |
| Repatriation Relative | seeking a named resident, talks of "coming home," visible emotional tension |
