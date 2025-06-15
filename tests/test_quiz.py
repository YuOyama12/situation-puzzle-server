from httpx import AsyncClient
import pytest

client = AsyncClient(base_url="http://localhost:8000/")

@pytest.mark.asyncio
async def test_get_quizzes():
    response = await client.get(url="/quizzes")
    assert response.status_code == 200
