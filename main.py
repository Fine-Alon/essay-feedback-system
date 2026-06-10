from fastapi import FastAPI
from routers import users, essays, analysis

app = FastAPI(title="CyberPro Essay Feedback System")

# Registering routers to the main application
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(essays.router, prefix="/essays", tags=["Essays"])
app.include_router(analysis.router, prefix="/analysis", tags=["Analysis"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the CyberPro Essay Feedback System"}