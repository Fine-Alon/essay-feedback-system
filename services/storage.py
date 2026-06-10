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




import os
import json
from pathlib import Path

USER_DATA_DIR = Path("data/users")
USER_DATA_DIR.mkdir(parents=True, exist_ok=True)

def save_user_profile(user_id: str, user_data: dict):
    file_path = USER_DATA_DIR / f"{user_id}.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(user_data, f, indent=4, ensure_ascii=False)

def load_user_profile(user_id: str) -> dict:
    file_path = USER_DATA_DIR / f"{user_id}.json"
    if not file_path.exists():
        return None
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
