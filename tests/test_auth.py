import pytest
from httpx import AsyncClient

from api.schemas.auth import AuthResponse, LoginRequest, SignUpRequest
from domain.constants import ErrorMessages
from tests.conftest import get_error_json

dummy_signup_request = SignUpRequest(
    user_name="dummy_new_user",
    nickname="dummy_nickname",
    password="dummy_new_password"
)


@pytest.mark.asyncio
async def test_signup_success(async_client: AsyncClient):
    response = await async_client.post(
        url="/signup",
        content=dummy_signup_request.model_dump_json()
    )

    assert response.status_code == 200
    assert AuthResponse.model_validate(response.json()).display_name == dummy_signup_request.nickname

@pytest.mark.asyncio
async def test_login_success(async_client: AsyncClient):
    request = LoginRequest(
        user_name=dummy_signup_request.user_name,
        password=dummy_signup_request.password
    )

    response = await async_client.post(
        url="/login",
        content=request.model_dump_json()
    )

    assert response.status_code == 200
    assert AuthResponse.model_validate(response.json()).display_name == dummy_signup_request.nickname

@pytest.mark.asyncio
async def test_login_failed(async_client: AsyncClient):
    request = LoginRequest(user_name="dummy", password="dummyPassword")
    response = await async_client.post(
        url="/login",
        content=request.model_dump_json()
    )

    assert response.status_code == 401
    assert response.json() == get_error_json(ErrorMessages.LOGIN_FAILED)

@pytest.mark.asyncio
async def test_signup_duplicate(async_client: AsyncClient):
    response = await async_client.post(
        url="/signup",
        content=dummy_signup_request.model_dump_json()
    )

    assert response.status_code == 400
    assert response.json() == get_error_json(ErrorMessages.USER_NAME_DUPLICATION)