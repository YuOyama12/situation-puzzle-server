from pydantic import BaseModel

class SignUpRequest(BaseModel):
    user_name: str
    nickname: str
    password: str

class LoginRequest(BaseModel):
    user_name: str
    password: str

class AuthResponse(BaseModel):
    user_id: int
    display_name: str