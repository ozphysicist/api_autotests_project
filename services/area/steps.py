from typing import Dict

import allure
from asserts import assert_equal

from base.base_steps import BaseSteps
from helpers import get_random_string_with_letters
from services.area.utils import validate_areas_list_data
from vars.enums import ResponseCodes, ErrorMessages


class AreaServiceSteps(BaseSteps):
    @allure.step('get area (positive)')
    def get_areas(self, user_agent: str, auth: bool = False, locale: str = None, host: str = None,
                  additional_case: str = None) -> Dict:
        result = self._client.get(
            path=f'/areas',
            auth=auth,
            headers={'HH-User-Agent': user_agent},
            params={'locale': locale, 'host': host, 'additional_case': additional_case}
        )
        assert_equal(
            result.status_code,
            ResponseCodes.OK.value,
            msg_fmt=f'Expected status code is 200, got {result.status_code}'
        )
        data = result.json()
        data_validation_result = validate_areas_list_data(data=data)
        assert_equal(
            'Success',
            data_validation_result,
            f'The data validation has not passed. Error message - {data_validation_result}',
        )
        return data

    @allure.step('get area (bad user agent)')
    def get_area_bad_user_agent(self, user_agent, auth: bool = False) -> Dict:
        result = self._client.get(
            path=f'/areas',
            auth=auth,
            headers={'User-Agent': user_agent},
            params={}
        )
        assert_equal(
            result.status_code,
            ResponseCodes.BAD_REQUEST.BAD_REQUEST,
            msg_fmt=f'Expected status code is 400, got {result.status_code}'
        )
        return result.json()

    @allure.step('get area (invalid locale)')
    def get_area_invalid_locale(self, user_agent: str, auth: bool = False) -> Dict:
        locale = get_random_string_with_letters(2)
        result = self._client.get(
            path=f'/areas',
            auth=auth,
            headers={'HH-User-Agent': user_agent},
            params={'locale': locale}
        )
        assert_equal(
            result.status_code,
            ResponseCodes.BAD_REQUEST.value,
            msg_fmt=f'Expected status code is 400, got {result.status_code}'
        )
        data = result.json()
        assert_equal(
            data['description'],
            ErrorMessages.INVALID_LOCALE.value,
            msg_fmt=f'Expected description is {ErrorMessages.INVALID_LOCALE.value}, actual - {data["description"]}'
        )
        return data
