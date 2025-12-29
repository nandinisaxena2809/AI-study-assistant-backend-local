# Local ML Inference API (Zero Cost)

A FastAPI backend that performs Question Answering using a locally hosted Transformer model. No external inference APIs are used.

## Features
- Runs fully locally (CPU-based)
- No Hugging Face Inference API
- Zero cost inference
- Auto-generated Swagger docs

## Tech Stack
- Python
- FastAPI
- Hugging Face Transformers
- PyTorch

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
