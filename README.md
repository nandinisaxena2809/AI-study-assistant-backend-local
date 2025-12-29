# Local ML Inference API

A FastAPI-based backend service that performs **Question Answering** and **Text Summarization**
using **locally hosted transformer models**.  
This project intentionally avoids paid cloud inference APIs and runs entirely on local CPU.

## Features
- Question Answering using a locally hosted RoBERTa model  
- Text Summarization using a **distilled BART model** optimized for CPU inference
- Runs fully locally (CPU-based)
- Zero-cost inference (no Hugging Face Inference API, no cloud compute)
- Auto-generated Swagger docs

## Tech Stack
- Python
- FastAPI
- Hugging Face Transformers
- PyTorch
- Uvicorn

## Setup

```bash
python -m venv hf-local
hf-local\Scripts\activate
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```
Open:
```text
http://127.0.0.1:8000/docs
```

---

## Available Endpoints

### POST /qa
Performs question answering on a given context.

#### Input
```text
{
  "question": "type question",
  "context": "Notes"
}
```

### POST /summarize
Generates a concise summary from a longer text input.

### Input
```text
{
  "text": "Long input text to summarize..."
}
```

---

## Model Choices & Design Decisions
- Question Answering: deepset/roberta-base-squad2
- Summarization: sshleifer/distilbart-cnn-12-6

