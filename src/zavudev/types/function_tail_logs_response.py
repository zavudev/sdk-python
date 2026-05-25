# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["FunctionTailLogsResponse", "Event"]


class Event(BaseModel):
    message: str

    timestamp: datetime


class FunctionTailLogsResponse(BaseModel):
    events: List[Event]

    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)
    """Pass to the next request to fetch the following page of logs."""
