
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from api.models.quiz import Quiz

class QuizRepository:
    async def fetch_all_quizzes(
        self,
        db: AsyncSession,
    ) -> List['Quiz']:
        result = await db.execute(
            select(Quiz).filter(Quiz.deleted_at.is_(None))
        )
        quizzes = result.scalars().all()

        return quizzes

    async def create_quiz(
        self,
        quiz: Quiz,
        db: AsyncSession,
    ) -> Optional[Quiz]:
        db.add(quiz)
        await db.commit()
        await db.refresh(quiz)

        return quiz
