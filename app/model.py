from transformers import pipeline

qa_pipeline = pipeline(
    "question-answering",
    model="deepset/roberta-base-squad2",
    device=-1
)

summarizer_pipeline = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6",
    device=-1
)

def answer_question(question: str, context: str):
    return qa_pipeline(question=question, context=context)

def summarize_text(text: str):
    return summarizer_pipeline(
        text,
        max_length=100,
        min_length=20,
        do_sample=False
    )[0]

