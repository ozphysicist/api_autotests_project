from typing import Any

from pydantic import ValidationError

from services.area.dataclasses import Area


def validate_areas_list_data(data: Any) -> str:
    """Data validation method"""
    try:
        for record in data:
            Area(**record)
    except ValidationError as error_message:
        return error_message
    else:
        return 'Success'
