from httpx import AsyncClient
import pytest

from api.schemas.quiz import Quiz
from domain.constants import ErrorMessages
from tests.conftest import get_error_json

@pytest.mark.asyncio
async def test_get_quizzes(async_client: AsyncClient):
    response = await async_client.get(url="/quizzes")
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_get_quizz_by_id_success(async_client: AsyncClient):
    target_id="1ea4026f-fabe-4392-877b-45180095c2ee"
    response = await async_client.get(
        url=f"/quizzes/{target_id}",
    )
    assert response.status_code == 200
    assert Quiz.model_validate(response.json()).id == target_id

@pytest.mark.asyncio
async def test_get_quizz_by_id_not_found(async_client: AsyncClient):
    target_id="dummy"
    response = await async_client.get(
        url=f"/quizzes/{target_id}",
    )
    assert response.status_code == 404
    assert response.json() == get_error_json(ErrorMessages.QUIZ_NOT_FOUND)

