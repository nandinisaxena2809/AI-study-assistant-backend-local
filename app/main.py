from fastapi import FastAPI
from pydantic import BaseModel
from app.model import answer_question, summarize_text

app = FastAPI(title="Local ML Inference API")

class QARequest(BaseModel):
    question: str
    context: str

class SummarizeRequest(BaseModel):
    text: str

@app.post("/qa")
def qa_endpoint(payload: QARequest):
    return answer_question(payload.question, payload.context)

@app.post("/summarize")
def summarize_endpoint(payload: SummarizeRequest):
    return summarize_text(payload.text)
