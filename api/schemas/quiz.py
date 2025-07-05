from datetime import datetime
from typing import Optional
from pydantic import BaseModel

from data.database.tables.quiz import Quiz


class Quiz(BaseModel):
    id: str
    title: str
    question: str
    answer: str
    user_id: int
    favorite_count: int = 0
    is_favorite: bool = False
    created_at: datetime
    updated_at: datetime

    @classmethod
    def create(cls, quiz_model: Quiz, user_id: Optional[int]) -> Quiz:
        return Quiz(
            id = quiz_model.id,
            title=quiz_model.title,
            question=quiz_model.question,
            answer=quiz_model.answer,
            user_id=quiz_model.user_id,
            is_favorite=cls._get_is_favorite(quiz_model, user_id),
            favorite_count=cls._get_favorite_count(quiz_model),
            created_at=quiz_model.created_at,
            updated_at=quiz_model.updated_at,
        )
    
    def _get_is_favorite(
        quiz_model: Quiz,
        user_id: Optional[int]
    ) -> bool:
        if user_id is not None:
            return any(e for e in quiz_model.favorites if e.user_id == user_id and e.quiz_id == quiz_model.id)
        else: 
            return False
        
    def _get_favorite_count(
        quiz_model: Quiz,
    ) -> int:
        return len( [e for e in quiz_model.favorites if e.quiz_id == quiz_model.id] )

class PostQuiz(BaseModel):
    title: str
    question: str
    answer: str
