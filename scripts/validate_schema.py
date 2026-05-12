import json
import sys

def validate_annotations(file_path):
    required_keys = {"audio_id", "transcript", "category", "confidence_score", "tags", "reviewer_notes"}
    valid = True

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
            for index, item in enumerate(data):
                missing_keys = required_keys - set(item.keys())
                if missing_keys:
                    print(f"Error at index {index} (audio_id: {item.get('audio_id', 'UNKNOWN')}): Missing keys {missing_keys}")
                    valid = False
                
                if not (0.0 <= item.get("confidence_score", -1) <= 1.0):
                    print(f"Error at index {index}: confidence_score must be between 0.0 and 1.0")
                    valid = False

        if valid:
            print("Validation Passed: All JSON objects conform to the required schema.")
            return 0
        else:
            print("Validation Failed: Fix schema errors before merging.")
            return 1

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return 1
    except json.JSONDecodeError:
        print("Invalid JSON format.")
        return 1

if __name__ == "__main__":
    sys.exit(validate_annotations('data/annotation_samples.json'))
