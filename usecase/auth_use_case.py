
import bcrypt
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api.schemas.auth import LoginRequest
from data.database.tables.user import User
from data.repository.auth_repository import AuthRepository
from domain.constants import ErrorMessages


class AuthUseCase:
    def __init__(self):
        self.auth_repository = AuthRepository()

    async def login(
        self,
        db: AsyncSession,
        request: LoginRequest
    ) -> User:
        user = await self.auth_repository.fetch_user_by_name(db=db, user_name=request.user_name)
        if (
            user is None 
            or not self._check_password(request.password, user.password)
        ):
            raise HTTPException(status_code=401, detail=ErrorMessages.LOGIN_FAILED)
        
        return user

    async def create_user(
        self,
        db: AsyncSession,
        user_name: str,
        password: str,
        nickname: str,
    ) -> User:
        same_user_name_exists = await self._check_if_user_name_exists(db=db, user_name=user_name)

        if same_user_name_exists:
            raise HTTPException(status_code=400, detail=ErrorMessages.USER_NAME_DUPLICATION)

        hashed_password = self._hash_password(password)
        user = User(name=user_name, nickname=nickname, password=hashed_password)
        return await self.auth_repository.create_user(db=db, user=user)
    
    def decide_display_name(self, user: User):
        return user.name if not user.nickname else user.nickname
    
    async def _check_if_user_name_exists(
        self,
        db: AsyncSession,
        user_name: str
    ) -> bool:
        user = await self.auth_repository.fetch_user_by_name(db=db, user_name=user_name)
        return user is not None

    def _hash_password(self, password: str) -> bytes:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    
    def _check_password(self, input_password: str, hashed_password: bytes) -> bool:
        return bcrypt.checkpw(input_password.encode(), hashed_password)
