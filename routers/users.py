from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import List
from services.storage import save_user_profile, load_user_profile
from utils.id_generator import generate_short_id

router = APIRouter()


# ==========================================
# 1. DATA SCHEMAS
# ==========================================
class UserCreate(BaseModel):
    username: str
    password: str
    email: str


class UserLogin(BaseModel):
    username: str
    password: str


# ==========================================
# 2. REGISTRATION ROUTE
# ==========================================
@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(user: UserCreate):
    if load_user_profile(user.username):
        raise HTTPException(status_code=400, detail="Username already taken")

    user_id = generate_short_id()
    hashed_password = user.password + "_securehash"

    user_profile = {
        "user_id": user_id,
        "username": user.username,
        "hashed_password": hashed_password,
        "email": user.email,
        "essay_history": [],
        "common_errors": [],
    }

    save_user_profile(user.username, user_profile)
    return {"message": "User registered successfully", "user_id": user_id}


# ==========================================
# 3. LOGIN ROUTE
# ==========================================
@router.post("/login")
async def login_user(user: UserLogin):
    user_data = load_user_profile(user.username)
    if not user_data:
        raise HTTPException(status_code=400, detail="Invalid username or password")

    expected_hash = user.password + "_securehash"
    if user_data["hashed_password"] != expected_hash:
        raise HTTPException(status_code=400, detail="Invalid username or password")

    return {"message": "Login successful", "user_id": user_data["user_id"]}


# ==========================================
# 4. PROFILE DASHBOARD ROUTE (Add it here!)
# ==========================================
@router.get("/profile/{username}")
async def get_profile(username: str):
    user_data = load_user_profile(username)
    if not user_data:
        raise HTTPException(status_code=404, detail="User profile not found")

    # Don't return the password hash to the frontend!
    user_data.pop("hashed_password", None)
    return user_data
