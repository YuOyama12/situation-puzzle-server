from api.schemas.auth import AuthResponse, LoginRequest, SignUpRequest
from data.database.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends
from api.schemas.quiz import *
from api.schemas.result_response import *
from usecase.auth_use_case import AuthUseCase


router = APIRouter()

auth_use_case = AuthUseCase()

API_AUTH_TAG = "auth" 

@router.post(
        "/login",
        response_model = AuthResponse,
        tags = [API_AUTH_TAG],
        description = "ログインAPI"
    )
async def login(
    request_body: LoginRequest,
    db: AsyncSession = Depends(get_db)
):
    result = await auth_use_case.login(
        db=db,
        request=request_body,
    )

    display_name: str = auth_use_case.decide_display_name(result)

    return AuthResponse(user_id= result.id, display_name= display_name)

@router.post(
        "/signup",
        response_model = AuthResponse,
        tags = [API_AUTH_TAG],
        description = "アカウント登録API"
    )
async def register_account(
    request_body: SignUpRequest,
    db: AsyncSession = Depends(get_db)
):
    result = await auth_use_case.create_user(
        db= db,
        user_name= request_body.user_name,
        password= request_body.password,
        nickname= request_body.nickname,
    )

    display_name: str = auth_use_case.decide_display_name(result)

    return AuthResponse(user_id= result.id, display_name= display_name)