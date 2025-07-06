
from typing import Optional

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from data.database.tables.favorite import Favorite
from domain.constants import ErrorMessages


class FavoriteRepository:
    async def add_favorite(
        self,
        db: AsyncSession,
        favorite: Favorite,
    ) :
        try:
            db.add(favorite)
            await db.commit()
        except Exception as e:
            if db.in_transaction():
                await db.rollback()
            raise e
             
    async def delete_favorite(
        self,
        db: AsyncSession,
        user_id: int,
        quiz_id: str,
    ):
        try:
            target_favorite = await self._fetch_favorite_by_ids(
                db=db,
                user_id=user_id,
                quiz_id=quiz_id
            )
            
            if target_favorite is None:
                raise HTTPException(status_code=404, detail=ErrorMessages.FAVORITE_ALREADY_REMOVED)

            await db.delete(target_favorite)
            await db.commit()
        except Exception as e:
            if db.in_transaction():
                await db.rollback()
            raise e
        
    async def _fetch_favorite_by_ids(
        self,
        db: AsyncSession,
        user_id: int,
        quiz_id: str,
    ) -> Optional[Favorite]:
        result = await db.execute(
            select(Favorite).filter(Favorite.user_id == user_id, Favorite.quiz_id == quiz_id)
        )

        return result.scalar_one_or_none()

