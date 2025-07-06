from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api.schemas.quiz import *
from api.schemas.result_response import *
from data.database.db import get_db
from domain.constants import ErrorMessages
from usecase.favorite_use_case import FavoriteUseCase

router = APIRouter()

favorite_use_case = FavoriteUseCase()

API_FAVORITE_TAG = "favorite" 

@router.post(
        "/favorites/{quiz_id}",
        response_model = ResultResponse,
        tags = [API_FAVORITE_TAG],
        description = "問題お気に入り追加API"
    )
async def add_to_favorites(
    quiz_id: str,
    user_id: int = Header(None),
    db: AsyncSession = Depends(get_db)
):
    if (user_id is None):
        raise HTTPException(status_code=401, detail=ErrorMessages.AUTH_FAILED)
    
    await favorite_use_case.add_to_favorites(
        db=db,
        user_id=user_id,
        quiz_id=quiz_id,
    )

    return ResultResponse(code=200, message="OK")


@router.delete(
        "/favorites/{quiz_id}",
        response_model = ResultResponse,
        tags = [API_FAVORITE_TAG],
        description = "問題お気に入り削除API"
    )
async def remove_from_favorites(
    quiz_id: str,
    user_id: int = Header(None),
    db: AsyncSession = Depends(get_db)
):
    if (user_id is None):
        raise HTTPException(status_code=401, detail=ErrorMessages.AUTH_FAILED)
    
    await favorite_use_case.remove_from_favorites(
        db=db,
        user_id=user_id,
        quiz_id=quiz_id,
    )

    return ResultResponse(code=200, message="OK")