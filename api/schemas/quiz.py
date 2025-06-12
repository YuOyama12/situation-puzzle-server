from datetime import datetime
from pydantic import BaseModel

class Quiz(BaseModel):
    id: str
    title: str
    question: str
    answer: str
    created_at: datetime
    updated_at: datetime


class PostQuiz(BaseModel):
    title: str
    question: str
    answer: str
