
from typing import List, Optional
from sqlalchemy import desc
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from fastapi import HTTPException
from data.database.tables.quiz import Quiz
from domain.constants import ErrorMessages

class QuizRepository:
    async def fetch_quiz_by_id(
        self,
        id: str,
        db: AsyncSession,
    ) -> Optional[Quiz]:
        result = await db.execute(
            select(Quiz).filter(Quiz.id == id, Quiz.deleted_at.is_(None))
        )
        quiz = result.scalar_one_or_none()

        if quiz is None:
            raise HTTPException(status_code=404, detail=ErrorMessages.QUIZ_NOT_FOUND)
         
        return quiz

    async def fetch_all_quizzes(
        self,
        db: AsyncSession,
    ) -> List[Quiz]:
        result = await db.execute(
            select(Quiz)
            .options(selectinload(Quiz.favorites))
            .filter(Quiz.deleted_at.is_(None))
            .order_by(desc(Quiz.created_at))
        )
        quizzes = result.scalars().all()

        return quizzes
    
    async def fetch_quizzes_by_user_id(
        self,
        user_id: int,
        db: AsyncSession,
    ) -> List[Quiz]:
        result = await db.execute(
            select(Quiz)
            .filter(Quiz.deleted_at.is_(None))
            .filter(Quiz.user_id == user_id)
            .order_by(desc(Quiz.created_at))
        )
        quizzes = result.scalars().all()

        return quizzes
    
    async def fetch_new_arrived_quizzes(
        self,
        db: AsyncSession,
        quiz_count: int
    ) -> List[Quiz]:
        result = await db.execute(
            select(Quiz)
            .filter(Quiz.deleted_at.is_(None))
            .order_by(desc(Quiz.created_at))
            .limit(quiz_count)
        )

        return result.scalars().all()

    async def create_quiz(
        self,
        quiz: Quiz,
        db: AsyncSession,
    ) -> Optional[Quiz]:
        try:
            db.add(quiz)
            await db.commit()
            await db.refresh(quiz)
        except:
            db.rollback()
            raise HTTPException(status_code=500)

        return quiz
