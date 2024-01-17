import allure
import pytest

from services.area.steps import AreaServiceSteps
from helpers import get_random_string_with_letters


@allure.title("Positive case: get areas")
def test_get_areas(area_service: AreaServiceSteps) -> None:
    user_agent = get_random_string_with_letters(10)
    area_service.get_areas(user_agent=user_agent)


@allure.title("Negative case: get areas without user agent in headers")
@pytest.mark.skip('unstable test, need to investigate this problem')
def test_get_areas_without_user_agent(area_service: AreaServiceSteps) -> None:
    user_agent = None
    area_service.get_area_bad_user_agent(user_agent=user_agent)


@allure.title("Negative case: get areas with invalid locale")
def test_get_areas_with_invalid_locale(area_service: AreaServiceSteps) -> None:
    user_agent = get_random_string_with_letters(10)
    area_service.get_area_invalid_locale(user_agent=user_agent)
