import pytest
from httpx import AsyncClient

@pytest.fixture
def async_client() -> AsyncClient:
    return AsyncClient(base_url="http://localhost:8000/")
