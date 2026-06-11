from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import users, essays

# from routers.essays import router as essays_router

app = FastAPI(
    title="CyberPro Essay Feedback System",
    description="API to load texts and getting feedback",
    version="1.0.0",
)

# Allow excess from any frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow requests from anywhere
    allow_credentials=True,
    allow_methods=["*"],  # allow POST, GET exc..
    allow_headers=["*"],
)

# Registering routers to the main application
app.include_router(users.router, prefix="/api/users", tags=["Users"])
app.include_router(essays.router, prefix="/api/essays", tags=["Essays"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the CyberPro Essay Feedback System"}
