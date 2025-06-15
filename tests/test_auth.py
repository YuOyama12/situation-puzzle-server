from fastapi.testclient import TestClient
from httpx import AsyncClient
import pytest

from api.schemas.auth import LoginRequest

client = AsyncClient(base_url="http://localhost:8000/")

@pytest.mark.asyncio
async def test_login_failed():
    request = LoginRequest(user_name="dummy", password="dummyPassword")
    response = await client.post(
        url="/login",
        content=request.model_dump_json()
    )

    assert response.status_code == 401

