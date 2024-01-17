import allure
import pytest

from asserts import assert_equal

from services.employers.steps import EmployerServiceSteps
from helpers import get_random_string_with_letters


@allure.title('Positive case: get employer "МойОФис"')
def test_get_employers(employer_service: EmployerServiceSteps) -> None:
    user_agent = get_random_string_with_letters(10)
    text = 'МойОФис'
    employer_service.get_employers(user_agent=user_agent, text=text)


@allure.title("Negative case: get employers without user agent in headers")
def test_get_employers_without_user_agent(employer_service: EmployerServiceSteps) -> None:
    user_agent = None
    employer_service.get_employers_bad_user_agent(user_agent=user_agent)


@allure.title("Positive case: test pagination")
@pytest.mark.parametrize("page, per_page", [(0, 20), (499, 10)])
def test_get_employers_pagination(employer_service: EmployerServiceSteps, page: int, per_page: int) -> None:
    user_agent = get_random_string_with_letters(10)
    page_data = employer_service.get_employers(user_agent=user_agent, per_page=per_page, page=page)
    with allure.step('Checking the number of employers on the page'):
        assert_equal(
            len(page_data['items']),
            per_page,
        )


@allure.title("Negative case: test pagination (get 5001 employer)")
def test_get_5001_employer(employer_service: EmployerServiceSteps) -> None:
    user_agent = get_random_string_with_letters(10)
    employer_service.get_5001_employer(user_agent=user_agent, per_page=1, page=5000)
