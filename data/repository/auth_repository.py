
from typing import Optional

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from data.database.tables.user import User


class AuthRepository:
    async def create_user(
        self,
        db: AsyncSession,
        user: User,
    ) -> User :
        try:
            db.add(user)
            await db.commit()
            await db.refresh(user)

            return user
        except Exception as e:
            if db.in_transaction():
                await db.rollback()
            raise e
             

    async def fetch_user_by_name(
        self,
        db: AsyncSession,
        user_name: str,
    ) -> Optional[User]:
        result = await db.execute(
            select(User).filter(User.name == user_name, User.deleted_at.is_(None))
        )
        
        return result.scalar_one_or_none()
