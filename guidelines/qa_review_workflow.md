# Quality Assurance (QA) Review Workflow

This document outlines the evaluation approach for reviewing annotated audio files. The goal is to ensure high inter-rater reliability and maintain strict adherence to the edge-case guidelines.

## QA Evaluation Criteria

Reviewers must assess annotations against three axes:
1. **Transcription Accuracy:** Does the text exactly match the spoken words? (Tolerance: 0% error for critical nouns/verbs, 5% for filler words).
2. **Tagging Compliance:** Are `[unintelligible]` and `[background_noise]` tags used correctly? 
3. **Code-Switch Consistency:** Is English transcribed in English, and Hindi transliterated consistently?

## Dispute Resolution Process

When a QA reviewer disagrees with an annotator's output:
1. **Minor Error (e.g., missing punctuation, slight spelling variation):** Reviewer corrects the data directly. Logged as a minor deduction.
2. **Systemic Error (e.g., guessing unintelligible words, translating instead of transcribing):** The file is rejected and sent back to the annotator with specific reference to the `annotation_edge_cases.md` documentation.
3. **Ambiguity Escalation:** If the reviewer and annotator cannot agree on the spoken word, the `audio_id` is escalated to the Lead Analyst and tagged `[needs_review]`.

## Reviewer Notes Format
When rejecting a file, reviewers must leave clear, actionable feedback.
* **Bad Note:** "Transcript is wrong."
* **Good Note:** "Transcription translated 'target' to 'lakshya'. Revert to spoken word 'target'. Refer to Rule 1 on Code-Switching."
