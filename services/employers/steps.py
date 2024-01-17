from typing import Dict

import allure
from asserts import assert_equal

from base.base_steps import BaseSteps
from services.employers.utils import validate_employer, validate_employers
from vars.enums import ResponseCodes, ErrorMessages


class EmployerServiceSteps(BaseSteps):
    @allure.step('get employer (positive)')
    def get_employers(self, user_agent: str, text: str = None,  area: str = None, emp_type: str = None,
                      only_with_vacancies: bool = None, sort_by: str = None, page: int = None, per_page: int = None,
                      auth: bool = False, locale: str = None, host: str = None) -> Dict:
        result = self._client.get(
            path=f'/employers',
            auth=auth,
            headers={'HH-User-Agent': user_agent},
            params={'text': text, 'area': area, 'type': emp_type, 'only_with_vacancies': only_with_vacancies,
                    'sort_by': sort_by, 'page': page, 'per_page': per_page, 'locale': locale, 'host': host}
        )
        assert_equal(
            result.status_code,
            ResponseCodes.OK.value,
            msg_fmt=f'Expected status code is 200, got {result.status_code}'
        )
        data = result.json()
        if len(data['items'][0]) == 1:
            data_validation_result = validate_employer(data=data['items'][0])
        else:
            data_validation_result = validate_employers(data=data['items'])
        assert_equal(
            'Success',
            data_validation_result,
            f'The data validation has not passed. Error message - {data_validation_result}',
        )
        return data

    @allure.step('get 5001st employer')
    def get_5001_employer(self, user_agent, per_page: int, page: int, auth: bool = False) -> Dict:
        result = self._client.get(
            path=f'/employers',
            auth=auth,
            headers={'User-Agent': user_agent},
            params={'per_step': per_page, 'page': page}
        )
        assert_equal(
            result.status_code,
            ResponseCodes.BAD_REQUEST.BAD_REQUEST.value,
            msg_fmt=f'Expected status code is 400, got {result.status_code}'
        )
        data = result.json()
        assert_equal(
            data['description'],
            ErrorMessages.MORE_THAN.value,
            msg_fmt=f'Expected description is {ErrorMessages.BAD_USER_AGENT.value}, actual - {data["description"]}'
        )
        return data

    @allure.step('get employers (bad user agent)')
    def get_employers_bad_user_agent(self, user_agent, auth: bool = False) -> Dict:
        result = self._client.get(
            path=f'/employers',
            auth=auth,
            headers={'User-Agent': user_agent},
            params={}
        )
        assert_equal(
            result.status_code,
            ResponseCodes.BAD_REQUEST.BAD_REQUEST.value,
            msg_fmt=f'Expected status code is 400, got {result.status_code}'
        )
        data = result.json()
        assert_equal(
            data['description'],
            ErrorMessages.BAD_USER_AGENT.value,
            msg_fmt=f'Expected description is {ErrorMessages.BAD_USER_AGENT.value}, actual - {data["description"]}'
        )
        return data
