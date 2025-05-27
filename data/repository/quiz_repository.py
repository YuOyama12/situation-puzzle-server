
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException
from api.models.quiz import Quiz

class QuizRepository:
    async def fetch_quiz_by_id(
        self,
        id: str,
        db: AsyncSession,
    ) -> Optional['Quiz']:
        result = await db.execute(
            select(Quiz).filter(Quiz.id == id, Quiz.deleted_at.is_(None))
        )
        quiz = result.scalar_one_or_none()

        if quiz is None:
            raise HTTPException(status_code=404, detail="該当する問題が見つかりませんでした。")
         
        return quiz

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
