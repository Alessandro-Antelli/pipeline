from fastapi import FastAPI
from app.analyzer import analyze_text
from pydantic import BaseModel

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/analyze")
def analyze(request: TextRequest):
    return analyze_text(request.text)

@app.get("/")
def read_root():
    return {"message": "Analizzatore attivo. Invia una POST a /analyze con un JSON {'text': '...'}"}