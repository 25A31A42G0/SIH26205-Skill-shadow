from fastapi import FastAPI
from ai.analyzer import analyze_response

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "AI Skill Analysis API is running"
    }


@app.post("/analyze")
def analyze(data: dict):
    return analyze_response(data)