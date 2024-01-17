from typing import Any

from pydantic import ValidationError

from services.employers.dataclasses import Employer


def validate_employer(data: Any) -> str:
    """Data validation method for Employer"""
    try:
        Employer(**data)
    except ValidationError as error_message:
        return error_message
    else:
        return 'Success'


def validate_employers(data: Any) -> str:
    """Data validation method for Employers List"""
    try:
        for record in data:
            Employer(**record)
    except ValidationError as error_message:
        return error_message
    else:
        return 'Success'
