from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health():
    return {
        "status": "healthy",
        "application": "AI Homelab Assistant",
        "version": "0.1.0"
    }