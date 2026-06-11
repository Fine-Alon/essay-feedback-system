import json
import os
from pathlib import Path
from utils.id_generator import generate_uuid
from services.text_checker import create_report_dic

#                       <<<  C R U D  >>>


# ================  USER  ==========================
USER_DATA_DIR = Path("data/users")
USER_DATA_DIR.mkdir(parents=True, exist_ok=True)


def save_user_profile(user_name: str, user_data: dict):
    file_path = USER_DATA_DIR / f"{user_name}.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(user_data, f, indent=4, ensure_ascii=False)


def load_user_profile(user_name: str) -> dict:
    file_path = USER_DATA_DIR / f"{user_name}.json"
    if not file_path.exists():
        return {}
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


# ================  ESSAY  ==========================
ESSAY_DATA_DIR = Path("data/essays")
ESSAY_DATA_DIR.mkdir(parents=True, exist_ok=True)


# CREATE
def create_essay_record(user_name: str, text: str):
    # generate ID for new essay
    new_essay_id = generate_uuid()

    # Create file name (Like: '550e8400-e29b-41d4.json')
    filename = f"{new_essay_id}.json"

    # path to save in (папка data/essays/)
    file_path = ESSAY_DATA_DIR / filename

    # Forming data structure: JSON
    essay_data = {
        "essay_id": new_essay_id,
        "user_name": user_name,
        "original_text": text,
        "status": "completed",
        "analysis_results": create_report_dic(text),
    }

    # Then will be script to save dict: essay_data to file(DB)...
    print(f"Ready to save in file: {filename}")

    with open(file_path, "w", encoding="utf-8") as f:
        # dump make Python dict as JSON format and record to file
        json.dump(essay_data, f, ensure_ascii=False, indent=4)

    return new_essay_id  # return ID helps reach this essay later on Client...


# READ
def get_essay(essay_id: str) -> dict:
    """
    Look for essay JSON file by its ID, reade it and return as dict.
    In case file NOT found, return None.
    """

    filename = f"{essay_id}.json"
    file_path = ESSAY_DATA_DIR / filename  # get right path to file

    #  Check if file exist
    if not file_path.exists():
        print(f"Error: Essay with {essay_id} ID not found")
        return {}

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            # json.load takes text from JSON file and turn it to Python ( dict !!!)
            essay_data = json.load(f)

        return essay_data

    except json.JSONDecodeError:
        # In case file was corrupted and no longer valid JSON
        print(f"Error: File {file_path} corrupted!")
        return {}


# UPDATE
def update_essay_results(essay_id: str, analysis_data: dict) -> bool:
    """
    Update essay JSON file with results of checking
    Change status 'completed' and record data from Oren's checking functions
    return True in case of success and False if there is Error.
    """
    filename = f"{essay_id}.json"
    filepath = ESSAY_DATA_DIR / filename

    # Check if file exists
    if not filepath.exists():
        print(f"Update error: Essay with {essay_id} ID not found")
        return False

    try:
        # Reading
        with open(filepath, "r", encoding="utf-8") as f:
            essay_data = json.load(f)

        # Updating of the appropriate fields in the dict
        essay_data["analysis_results"] = analysis_data
        essay_data["status"] = "completed"

        # Recording new updated content
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(essay_data, f, ensure_ascii=False, indent=4)

        print(f"Success: Results for the essay {essay_id} were saved")
        return True

    except Exception as e:
        # Here we catch any exceptions.
        print(f"Critical issue while saving results for {essay_id}: {str(e)}")
        return False
