# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BroadcastSendParams"]


class BroadcastSendParams(TypedDict, total=False):
    scheduled_at: Annotated[Union[str, datetime], PropertyInfo(alias="scheduledAt", format="iso8601")]
    """Schedule for future delivery. Omit to send immediately."""
