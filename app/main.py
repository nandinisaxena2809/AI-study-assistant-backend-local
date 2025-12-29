from fastapi import FastAPI
from pydantic import BaseModel
from app.model import answer_question

app = FastAPI(title="Local ML Inference API")

class QARequest(BaseModel):
    question: str
    context: str

@app.post("/qa")
def qa_endpoint(payload: QARequest):
    return answer_question(payload.question, payload.context)
