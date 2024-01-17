import pytest

from base.api_client import BaseApiClient
from services.employers.steps import EmployerServiceSteps

@pytest.fixture(scope="session")
def employer_service() -> EmployerServiceSteps:
    return EmployerServiceSteps(BaseApiClient())
