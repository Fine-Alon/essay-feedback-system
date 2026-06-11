from pydantic import BaseModel
from typing import List

class UserProfile(BaseModel):
    
    username: str
    password: str
    email: str
    
    common_errors: List[str] = []