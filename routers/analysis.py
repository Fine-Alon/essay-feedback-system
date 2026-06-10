from fastapi import APIRouter

# This is the line that must exist for main.py to find it
router = APIRouter()

@router.get("/")
async def get_analysis():
    return {"message": "Analysis endpoint working"}