
from typing import List, Optional
from domain.constants import MAX_QUIZ_COUNT_AS_NEW_ARRIVAL
from sqlalchemy.ext.asyncio import AsyncSession
from api.schemas.quiz import PostQuiz
from api.models.quiz import Quiz
from data.repository.quiz_repository import QuizRepository


class QuizUseCase:
    async def fetch_quiz_by_id(self, id: str, db: AsyncSession) -> Optional[Quiz]:
        return await QuizRepository().fetch_quiz_by_id(id = id, db = db)

    async def fetch_quizzes(self, db: AsyncSession) -> List[Quiz]:
        return await QuizRepository().fetch_all_quizzes(db = db)
    
    async def fetch_new_arrived_quizzes(self, db: AsyncSession) -> List[Quiz]:
        quizzes = await QuizRepository().fetch_all_quizzes(db=db)
        if not quizzes:
            return []
        
        sorted_quizzes = sorted(quizzes, key=lambda quiz: quiz.created_at, reverse=True)

        return sorted_quizzes[0:MAX_QUIZ_COUNT_AS_NEW_ARRIVAL]

    async def post_quiz(self, request: PostQuiz, db: AsyncSession) -> Optional[Quiz]:
        quiz_repository = QuizRepository()
        quiz = Quiz(
            title = request.title,
            question = request.question,
            answer = request.answer
        )
        return await quiz_repository.create_quiz(quiz = quiz, db = db)