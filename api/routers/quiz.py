from typing import List
from data.database.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException
from api.schemas.quiz import *
from api.schemas.result_response import *
from usecase.quiz_use_case import QuizUseCase 


router = APIRouter()

quiz_use_case = QuizUseCase()

API_QUIZ_TAG = "quiz" 

@router.get(
        "/quizzes/sample",
        response_model = List[Quiz],
        tags = [API_QUIZ_TAG],
        description = "サンプル問題取得API"
    )
async def get_sample_quizzes():
    return Quiz.samples()

@router.get(
        "/quizzes",
        response_model = List[Quiz],
        tags = [API_QUIZ_TAG],
        description = "投稿済み問題取得API"
    )
async def get_quizzes(
    db: AsyncSession = Depends(get_db)
):
    result = await quiz_use_case.fetch_quizzes(db)
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

    if result is None:
        raise HTTPException(status_code=404, detail="quiz_not_found")
    
    return result


@router.post(
        "/quiz",
        response_model = ResultResponse,
        tags = [API_QUIZ_TAG],
        description = "問題投稿API"
    )
async def post_quiz(
    request_body: PostQuiz,
    db: AsyncSession = Depends(get_db)
):
    result = await quiz_use_case.post_quiz(request_body, db = db)

    if result is not None:
        return ResultResponse(code=200, message="OK")
    else:
        return ResultResponse(code=500, message="Post Failed")