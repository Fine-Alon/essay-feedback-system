# Импортируем нашу функцию из папки utils
from utils.id_generator import generate_uuid


def create_essay_record(user_id: str, text: str):
    # generate ID for new essay
    new_essay_id = generate_uuid()

    # Create file name (Like: '550e8400-e29b-41d4.json')
    filename = f"{new_essay_id}.json"

    # Forming data structure: JSON
    essay_data = {
        "essay_id": new_essay_id,
        "user_id": user_id,
        "original_text": text,
        "status": "pending",
        "analysis_results": {},
    }

    # Then will be script to save dict: essay_data to file...
    print(f"Ready to save in file: {filename}")
    return new_essay_id


def save_essay_to_json(data):
    pass
