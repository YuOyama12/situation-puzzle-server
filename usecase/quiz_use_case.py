
from typing import List, Optional
from domain.constants import MAX_QUIZ_COUNT_AS_NEW_ARRIVAL
from sqlalchemy.ext.asyncio import AsyncSession
from api.schemas.quiz import PostQuiz
from api.models.quiz import Quiz
from data.repository.quiz_repository import QuizRepository

class QuizUseCase:
    def __init__(self):
        self.quiz_repository = QuizRepository()

    async def fetch_quiz_by_id(self, id: str, db: AsyncSession) -> Optional[Quiz]:
        return await self.quiz_repository.fetch_quiz_by_id(id = id, db = db)

    async def fetch_quizzes(self, db: AsyncSession) -> List[Quiz]:
        return await self.quiz_repository.fetch_all_quizzes(db = db)
    
    async def fetch_new_arrived_quizzes(self, db: AsyncSession) -> List[Quiz]:
        quizzes = await self.quiz_repository.fetch_new_arrived_quizzes(
            db=db,
            quiz_count=MAX_QUIZ_COUNT_AS_NEW_ARRIVAL
        )
        
        if not quizzes:
            return []
        
        return quizzes

    async def post_quiz(self, request: PostQuiz, db: AsyncSession) -> Optional[Quiz]:
        quiz = Quiz(
            title = request.title,
            question = request.question,
            answer = request.answer
        )
        return await self.quiz_repository.create_quiz(quiz = quiz, db = db)