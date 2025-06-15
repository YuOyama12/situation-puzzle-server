from httpx import AsyncClient
import pytest

from api.schemas.auth import LoginRequest

@pytest.mark.asyncio
async def test_login_failed(async_client: AsyncClient):
    request = LoginRequest(user_name="dummy", password="dummyPassword")
    response = await async_client.post(
        url="/login",
        content=request.model_dump_json()
    )

    assert response.status_code == 401
