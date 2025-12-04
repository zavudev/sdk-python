# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .message import Message
from .._models import BaseModel

__all__ = ["MessageListResponse"]


class MessageListResponse(BaseModel):
    items: List[Message]

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
