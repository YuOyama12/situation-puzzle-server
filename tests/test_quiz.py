from typing import List

import pytest
from httpx import AsyncClient
from pydantic import TypeAdapter

from api.schemas.quiz import Quiz
from data.database.seeders.constants import SAMPLE_QUIZ_ID, SAMPLE_QUIZ_USER_ID
from domain.constants import ErrorMessages
from tests.conftest import get_error_json


@pytest.mark.asyncio
async def test_get_quizzes(async_client: AsyncClient):
    response = await async_client.get(url="/quizzes")
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_get_quiz_by_id_success(async_client: AsyncClient):
    target_id=SAMPLE_QUIZ_ID
    response = await async_client.get(
        url=f"/quizzes/{target_id}",
    )

    quiz = Quiz.model_validate(response.json())
    assert response.status_code == 200
    assert quiz.id == target_id
    assert quiz.is_favorite == False
    assert quiz.favorite_count == 1

@pytest.mark.asyncio
async def test_get_quiz_by_id_not_found(async_client: AsyncClient):
    target_id="dummy"
    response = await async_client.get(
        url=f"/quizzes/{target_id}",
    )
    assert response.status_code == 404
    assert response.json() == get_error_json(ErrorMessages.QUIZ_NOT_FOUND)

@pytest.mark.asyncio
async def test_get_my_favorite_quizzes_success(async_client: AsyncClient):
    headers = {
        'User-Id': str(SAMPLE_QUIZ_USER_ID),
    }

    response = await async_client.get(
        url="/quizzes/my_favorites",
        headers=headers
    )

    quizzes = TypeAdapter(List[Quiz]).validate_python(response.json())

    assert response.status_code == 200
    assert len(quizzes) == 1


@pytest.mark.asyncio
async def test_get_my_favorite_quizzes_empty(async_client: AsyncClient):
    headers = {
        'User-Id': '-1',
    }

    response = await async_client.get(
        url="/quizzes/my_favorites",
        headers=headers
    )

    quizzes = TypeAdapter(List[Quiz]).validate_python(response.json())

    assert response.status_code == 200
    assert len(quizzes) == 0
