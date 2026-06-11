from pydantic import BaseModel
from typing import List

class UserProfile(BaseModel):
    user_id: str
    username: str
    password: str
    email: str
    essay_history: List[str] = []
    common_errors: List[str] = []