import json
import os
from utils.id_generator import generate_uuid

# C R U D --->


# CREATE
def create_essay_record(user_id: str, text: str):
    # generate ID for new essay
    new_essay_id = generate_uuid()

    # Create file name (Like: '550e8400-e29b-41d4.json')
    filename = f"{new_essay_id}.json"

    # path to save in (папка data/essays/)
    filepath = os.path.join("data", "essays", filename)

    # Forming data structure: JSON
    essay_data = {
        "essay_id": new_essay_id,
        "user_id": user_id,
        "original_text": text,
        "status": "pending",  # PENDING!!!
        "analysis_results": {},
    }

    # Then will be script to save dict: essay_data to file(DB)...
    print(f"Ready to save in file: {filename}")

    with open(filepath, "w", encoding="utf-8") as f:
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
    filepath = os.path.join("data", "essays", filename)  # get right path to file

    #  Check if file exist
    if not os.path.exists(filepath):
        print(f"Error: Essay with {essay_id} ID not found")
        return None

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            # json.load takes text from JSON file and turn it to Python ( dict !!!)
            essay_data = json.load(f)

        return essay_data

    except json.JSONDecodeError:
        # In case file was corrupted and no longer valid JSON
        print(f"Error: File {filepath} corrupted!")
        return None


## OREN - usage
# from services.storage import get_essay

# def analyze_essay_text(essay_id: str):
## OREN ask for data
# data = get_essay(essay_id)

# if data is None:
#   return "No essay found!"

## OREN - get any text by key "original_text"
# text_to_check = data["original_text"]

## OREN - run any checks


# UPDATE
def update_essay_results(essay_id: str, analysis_data: dict) -> bool:
    """
    Update essay JSON file with results of checking
    Change status 'completed' and record data from Oren's checking functions
    return True in case of success and False if there is Error.
    """
    filename = f"{essay_id}.json"
    filepath = os.path.join("data", "essays", filename)

    # Check if file exists
    if not os.path.exists(filepath):
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
