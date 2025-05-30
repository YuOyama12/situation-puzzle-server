
from typing import Optional
from api.models.user import User
from data.repository.auth_repository import AuthRepository
from sqlalchemy.ext.asyncio import AsyncSession
import bcrypt

class AuthUseCase:
    async def login(
        self,
        db: AsyncSession,
    ):
        pass

    async def create_user(
        self,
        db: AsyncSession,
        user_name: str,
        password: str,
        nickname: str,
    ) -> 'User':
        hashed_password = self._hash_password(password)
        user = User(name=user_name, nickname=nickname, password=hashed_password)
        return await AuthRepository().create_user(db=db, user=user)

    def _hash_password(self, password: str) -> bytes:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    
    def _check_password(self, input_password: str, hashed_password: bytes) -> bool:
        return bcrypt.checkpw(input_password.encode(), hashed_password)
