# Hindi-English Audio Annotation & Quality Assurance
**[📊 View the Project Architecture & Operational Blueprint PDF here](./Indic_Audio_Annotation_Blueprint.pdf)**

This repository contains operational guidelines, quality assurance workflows, and sample datasets for processing Hindi and mixed Hindi-English (Hinglish) audio data. 

The primary objective is to standardize transcription and annotation across highly variable audio inputs, specifically focusing on regional accents, acoustic noise, code-switching, and ambiguous speech patterns.

## Repository Structure

* `guidelines/`: Contains rules for handling edge cases and standardizing the QA review process.
* `data/`: JSON datasets containing categorized audio transcriptions and metadata.
* `scripts/`: Python utilities for validating annotation schemas.

## Core Operational Challenges Addressed

1. **Code-Switching (Hinglish):** Establishing clear boundaries for transcription when speakers rapidly switch between English and Hindi.
2. **Regional Pronunciation:** Standardizing spelling and tagging for regional variations (e.g., typical dialectical shifts in North India).
3. **Acoustic Ambiguity:** Protocols for tagging background noise, overlapping speech, and unintelligible segments to prevent false data generation.

## Schema Overview
The annotation data strictly follows this JSON schema:
- `audio_id`: Unique identifier.
- `transcript`: The raw text.
- `tags`: List of metadata tags (e.g., `[noise]`, `[regional_accent]`).
- `confidence_score`: 0.0 to 1.0 rating of audio clarity.
- `reviewer_notes`: Contextual notes for quality assurance.
