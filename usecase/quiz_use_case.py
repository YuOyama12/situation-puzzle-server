
from typing import List, Optional
from data.database.tables.quiz import Quiz
from domain.constants import MAX_QUIZ_COUNT_AS_NEW_ARRIVAL
from sqlalchemy.ext.asyncio import AsyncSession
from api.schemas.quiz import Quiz, PostQuiz
from data.repository.quiz_repository import QuizRepository

class QuizUseCase:
    def __init__(self):
        self.quiz_repository = QuizRepository()

    async def fetch_quiz_by_id(self, id: str, user_id: Optional[int], db: AsyncSession) -> Optional[Quiz]:
        quiz = await self.quiz_repository.fetch_quiz_by_id(id=id, db=db)
        return Quiz.create(quiz_model=quiz, user_id=user_id)

    async def fetch_quizzes(self, user_id: Optional[int], db: AsyncSession) -> List[Quiz]:
        quizzes = await self.quiz_repository.fetch_all_quizzes(db=db)
        return self._convert_to_quiz_schemas(quizzes=quizzes, user_id=user_id)
    
    async def fetch_quizzes_by_user_id(self, user_id: int, db: AsyncSession) -> List[Quiz]:
        quizzes = await self.quiz_repository.fetch_quizzes_by_user_id(user_id=user_id, db=db)
        return self._convert_to_quiz_schemas(quizzes=quizzes, user_id=user_id)
    
    async def fetch_new_arrived_quizzes(self, user_id: Optional[int], db: AsyncSession) -> List[Quiz]:
        quizzes = await self.quiz_repository.fetch_new_arrived_quizzes(
            db=db,
            quiz_count=MAX_QUIZ_COUNT_AS_NEW_ARRIVAL
        )
        
        if not quizzes:
            return []
        
        return self._convert_to_quiz_schemas(quizzes=quizzes, user_id=user_id)

    async def post_quiz(
        self, 
        request: PostQuiz,
        user_id: int,
        db: AsyncSession
    ) -> Optional[Quiz]:
        quiz = Quiz(
            title = request.title,
            question = request.question,
            answer = request.answer,
            user_id = user_id,
        )
        return await self.quiz_repository.create_quiz(quiz = quiz, db = db)
    
    def _convert_to_quiz_schemas(
            self,
            quizzes: List[Quiz],
            user_id: Optional[int],
        ) -> List[Quiz]:
        return list(map(lambda quiz: Quiz.create(quiz_model=quiz, user_id=user_id), quizzes))