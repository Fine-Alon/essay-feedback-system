from fastapi import FastAPI
from routers import users, essays

# from routers.essays import router as essays_router

app = FastAPI(
    title="CyberPro Essay Feedback System",
    description="API to load texts and getting feedback",
    version="1.0.0",
)

# Registering routers to the main application
app.include_router(users.router, prefix="/api/users", tags=["Users"])
app.include_router(essays.router, prefix="/api/essays", tags=["Essays"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the CyberPro Essay Feedback System"}
