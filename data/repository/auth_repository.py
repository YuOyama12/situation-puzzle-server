
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

class AuthRepository:
    async def login(
        self,
        db: AsyncSession,
    ):
        pass
