from typing import List
from fastapi import APIRouter
from api.schemas.quiz import *
from api.schemas.result_response import * 


router = APIRouter()

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
async def get_quizzes():
    return [
        Quiz(id="1", title="タイトル1", question="問題文1", answer="回答文1"),
        Quiz(id="2", title="タイトル2", question="問題文2", answer="回答文2"),
        ]

@router.post(
        "/quiz",
        response_model = ResultResponse,
        tags = [API_QUIZ_TAG],
        description = "問題投稿API"
    )
async def post_quiz(
    request_body: PostQuiz
):
    return ResultResponse(code=200, message="OK")