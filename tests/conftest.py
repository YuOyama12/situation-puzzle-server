import pytest
from httpx import AsyncClient


def get_error_json(
    message: str,
):
    return {"detail": message}

@pytest.fixture
def async_client() -> AsyncClient:
    return AsyncClient(base_url="http://localhost:8000/")
