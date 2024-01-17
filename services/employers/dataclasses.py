from typing import Dict, List, Optional, Union

from pydantic import BaseModel


class Employer(BaseModel):
    """
    Data model describes Employer object
    """
    id: str
    name: str
    url: str
    alternate_url: str
    logo_urls: Union[Dict, None]
    vacancies_url: str
    open_vacancies: int
