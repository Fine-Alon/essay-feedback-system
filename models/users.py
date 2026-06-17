from pydantic import BaseModel
from typing import List

# ==========================================
# 1. REQUEST SCHEMAS (Matches your Router)
# ==========================================
class UserCreate(BaseModel):
    username: str
    password: str
    email: str


class UserLogin(BaseModel):
    username: str
    password: str


# ==========================================
# 2. STORAGE SCHEMA (Matches your JSON file structure)
# ==========================================
class UserProfile(BaseModel):
    username: str
    password: str
    email: str
    common_errors: List[str] = []