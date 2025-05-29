from api.schemas.auth import LoginRequest, SignUpRequest
from data.database.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends
from api.schemas.quiz import *
from api.schemas.result_response import *


router = APIRouter()

API_AUTH_TAG = "auth" 

@router.post(
        "/login",
        response_model = ResultResponse,
        tags = [API_AUTH_TAG],
        description = "ログインAPI"
    )
async def login(
    request_body: LoginRequest,
    db: AsyncSession = Depends(get_db)
):
    return ResultResponse(code=200, message="てすと")

@router.post(
        "/signup",
        response_model = ResultResponse,
        tags = [API_AUTH_TAG],
        description = "アカウント登録API"
    )
async def register_account(
    request_body: SignUpRequest,
    db: AsyncSession = Depends(get_db)
):
    return ResultResponse(code=200, message="てすと")