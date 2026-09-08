# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["TriggerCreateParams"]


class TriggerCreateParams(TypedDict, total=False):
    event_types: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="eventTypes")]]
    """Event types to subscribe to."""

    sender_ids: Required[Annotated[SequenceNotStr[Optional[str]], PropertyInfo(alias="senderIds")]]
    """Senders to scope the triggers to. Use null for all senders."""

    cron: str
    """
    Required when eventTypes includes `cron`: a 5-field cron expression (minute hour
    day-of-month month day-of-week), evaluated in UTC.
    """
