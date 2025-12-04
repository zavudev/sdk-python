# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .sender import Sender
from .._models import BaseModel

__all__ = ["SenderListResponse"]


class SenderListResponse(BaseModel):
    items: List[Sender]

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
