from typing import List
from data.database.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException, Header
from api.schemas.quiz import *
from api.schemas.result_response import *
from domain.constants import ErrorMessages
from usecase.quiz_use_case import QuizUseCase 


router = APIRouter()

quiz_use_case = QuizUseCase()

API_QUIZ_TAG = "quiz" 

@router.get(
        "/quizzes",
        response_model = List[Quiz],
        tags = [API_QUIZ_TAG],
        description = "問題一覧取得API"
    )
async def get_quizzes(
    db: AsyncSession = Depends(get_db)
):
    result = await quiz_use_case.fetch_quizzes(db)
    return result

@router.get(
        "/my-quizzes",
        response_model = List[Quiz],
        tags = [API_QUIZ_TAG],
        description = "自分の投稿済問題一覧取得API"
    )
async def get_my_quizzes(
    user_id: int = Header(None),
    db: AsyncSession = Depends(get_db)
):
    if (user_id is None):
        return []
    
    result = await quiz_use_case.fetch_quizzes_by_user_id(user_id=user_id, db=db)
    return result

@router.get(
        "/quizzes/new_arrivals",
        response_model = List[Quiz],
        tags = [API_QUIZ_TAG],
        description = "新着問題取得API"
    )
async def get_new_arrived_quizzes(
    db: AsyncSession = Depends(get_db)
):
    result = await quiz_use_case.fetch_new_arrived_quizzes(db)
    return result

@router.get(
        "/quizzes/{quiz_id}",
        response_model = Quiz,
        tags = [API_QUIZ_TAG],
        description = "問題取得API",
    )
async def get_quiz(
    quiz_id: str,
    db: AsyncSession = Depends(get_db)
):
    result = await quiz_use_case.fetch_quiz_by_id(id = quiz_id, db = db)
    return result


@router.post(
        "/quiz",
        response_model = ResultResponse,
        tags = [API_QUIZ_TAG],
        description = "問題投稿API"
    )
async def post_quiz(
    request_body: PostQuiz,
    user_id: int = Header(None),
    db: AsyncSession = Depends(get_db)
):
    if (user_id is None):
        raise HTTPException(status_code=401, detail=ErrorMessages.AUTH_FAILED)
    
    await quiz_use_case.post_quiz(request_body, user_id=user_id, db=db)

    return ResultResponse(code=200, message="投稿が完了しました")