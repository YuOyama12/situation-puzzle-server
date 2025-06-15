from httpx import AsyncClient
import pytest

@pytest.mark.asyncio
async def test_get_quizzes(async_client: AsyncClient):
    response = await async_client.get(url="/quizzes")
    assert response.status_code == 200
