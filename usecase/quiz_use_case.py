
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from api.schemas.quiz import PostQuiz
from api.models.quiz import Quiz
from data.repository.quiz_repository import QuizRepository


class QuizUseCase:
    async def fetch_quizzes(self, db: AsyncSession) -> List[Quiz]:
        return await QuizRepository().fetch_all_quizzes(db = db)

    async def post_quiz(self, request: PostQuiz, db: AsyncSession) -> Optional[Quiz]:
        quiz_repository = QuizRepository()
        quiz = Quiz(
            title = request.title,
            question = request.question,
            answer = request.answer
        )
        return await quiz_repository.create_quiz(quiz = quiz, db = db)