
from sqlalchemy.ext.asyncio import AsyncSession

class AuthUseCase:
    async def login(
        self,
        db: AsyncSession,
    ):
        pass