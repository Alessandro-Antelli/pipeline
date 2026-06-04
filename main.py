import time
from fastapi import FastAPI
from pydantic import BaseModel
from app.analyzer import analyze_text

app = FastAPI()


class TextRequest(BaseModel):
    text: str


@app.post("/analyze")
def analyze(request: TextRequest):

    start = time.time()


    result = analyze_text(request.text)


    end = time.time()
    tempo_impiegato = round(end - start, 6)


    if result is not None:

        result["tempo impiegato in secondi"] = tempo_impiegato
        return result

    return {"error": "Invalid input"}


@app.get("/")
def read_root():
    return {"message": "Analizzatore attivo. Invia una POST a /analyze con un JSON {'text': '...'}"}