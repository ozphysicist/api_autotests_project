from typing import List, Optional, Union

from pydantic import BaseModel


class Area(BaseModel):
    """
    Data model describes Area object
    """
    id: str
    parent_id: Union[str, None]
    name: str
    areas: List
    name_prepositional: Optional[str] = None
