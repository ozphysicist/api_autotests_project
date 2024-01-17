import pytest

from base.api_client import BaseApiClient
from services.area.steps import AreaServiceSteps


@pytest.fixture(scope="session")
def area_service() -> AreaServiceSteps:
    return AreaServiceSteps(BaseApiClient())
