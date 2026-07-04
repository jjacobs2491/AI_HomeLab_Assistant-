from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Homelab Assistant is running!"}