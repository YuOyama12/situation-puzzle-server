
from api.models.user import User
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

class AuthRepository:
    async def create_user(
        self,
        db: AsyncSession,
        user: User,
    ) -> 'User' :
        try:
            db.add(user)
            await db.commit()
            await db.refresh(user)

            return user
        except Exception as e:
            if db.in_transaction():
                await db.rollback()
            raise e
             

    async def login(
        self,
        db: AsyncSession,
    ):
        pass
