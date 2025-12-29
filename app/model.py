from transformers import pipeline

qa_pipeline = pipeline(
    "question-answering",
    model="deepset/roberta-base-squad2",
    device=-1
)

def answer_question(question: str, context: str):
    return qa_pipeline(question=question, context=context)
