# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .contact import Contact
from .._models import BaseModel

__all__ = ["ContactListResponse"]


class ContactListResponse(BaseModel):
    items: List[Contact]

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
