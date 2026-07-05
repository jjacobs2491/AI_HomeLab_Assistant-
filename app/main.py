from fastapi import FastAPI
from app.routes.system import router as system_router
from app.routes.health import router as health_router

app = FastAPI(
    title="AI Homelab Assistant",
    description="A self-hosted AI assistant for managing and monitoring a personal homelab.",
    version="0.1.0"
)

app.include_router(system_router)
app.include_router(health_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to AI Homelab Assistant!",
        "status": "Running"
    }