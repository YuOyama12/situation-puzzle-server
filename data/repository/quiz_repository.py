
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from api.models.quiz import Quiz

class QuizRepository:
    async def create_quiz(
        self,
        quiz: Quiz,
        db: AsyncSession,
    ) -> Optional[Quiz]:
        print(quiz.title)
        db.add(quiz)
        await db.commit()
        await db.refresh(quiz)
        return quiz
