# Annotation Guidelines: Edge Cases & Ambiguity

This document outlines the standard operating procedures for handling complex audio inputs. Consistency is the priority. When in doubt, tag for ambiguity rather than guessing.

## 1. Handling Code-Switching (Hinglish)
When a speaker mixes Hindi and English, transcribe the English words in the Latin alphabet and the Hindi words in the Latin alphabet (transliteration) using standard phonetic spellings. 

* **Rule:** Do not translate. Transcribe exactly what is spoken.
* **Audio:** "Mera target completion kal tak hai."
* **Correct:** "Mera target completion kal tak hai."
* **Incorrect:** "Mera lakshya completion kal tak hai." (Attempting to over-Hindi-fy)

## 2. Regional Pronunciation Variations
Speakers frequently adapt English words to local phonetic constraints (e.g., "school" pronounced as "iskool", "report" as "rapat").

* **Rule:** Transcribe the standard spelling of the intended word, but add the `[pronunciation_variant]` tag to the metadata so downstream models recognize the acoustic shift.
* **Audio:** "Woh station pe wait kar raha hai." (Pronounced "istation")
* **Transcription:** "Woh station pe wait kar raha hai."
* **Tags:** `["regional_accent", "pronunciation_variant"]`

## 3. Acoustic Noise and Unintelligible Speech
Do not guess words if the audio is compromised. 

* **Rule:** Use `[unintelligible]` for words that cannot be understood after three listens. Use `[background_noise]` at the start of the transcript if noise obscures more than 20% of the audio.
* **Audio:** "Aapka order [loud static] baje deliver hoga."
* **Transcription:** "Aapka order [unintelligible] baje deliver hoga."

## 4. Filler Words and Stuttering
* **Rule:** Include common filler words ("um", "uh", "matlab", "jaise") for acoustic modeling purposes, but ignore isolated stutters unless requested by a specific project brief.
* **Example:** "Main matlab kal jaunga."
