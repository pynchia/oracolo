from httpx import AsyncClient
import pytest

from app.config.app import APP_CFG


@pytest.fixture
async def client():
    async with AsyncClient(
        base_url=APP_CFG.source.api_url,
    ) as ac:
        yield ac
