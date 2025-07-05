
from data.database.tables.favorite import Favorite
from sqlalchemy.ext.asyncio import AsyncSession
from data.repository.favorite_repository import FavoriteRepository

class FavoriteUseCase:
    def __init__(self):
        self.favorite_repository = FavoriteRepository()

    async def add_to_favorites(
        self,
        db: AsyncSession,
        user_id: int,
        quiz_id: str,
    ):
        data = Favorite(user_id=user_id, quiz_id=quiz_id)
        await self.favorite_repository.add_favorite(db=db, favorite=data)

    async def remove_from_favorites(
        self,
        db: AsyncSession,
        user_id: int,
        quiz_id: str,
    ):
        await self.favorite_repository.delete_favorite(
            db=db,
            user_id=user_id,
            quiz_id=quiz_id,
        )

        
