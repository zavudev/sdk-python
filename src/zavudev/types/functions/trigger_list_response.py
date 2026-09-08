# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TriggerListResponse", "Trigger"]


class Trigger(BaseModel):
    """A subscription that runs a Zavu Function when a messaging event fires."""

    id: str

    active: bool

    created_at: datetime = FieldInfo(alias="createdAt")

    event_type: str = FieldInfo(alias="eventType")
    """Event type that fires the function.

    See GET /v1/functions/event-types for the supported list. The special type
    `cron` fires on a schedule instead of a messaging event and carries a `cron`
    expression.
    """

    function_id: str = FieldInfo(alias="functionId")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    cron: Optional[str] = None
    """
    5-field cron expression (minute hour day-of-month month day-of-week), evaluated
    in UTC. Present only on `cron` triggers.
    """

    last_run_at: Optional[datetime] = FieldInfo(alias="lastRunAt", default=None)
    """Last time the schedule fired. Null until the first fire."""

    next_run_at: Optional[datetime] = FieldInfo(alias="nextRunAt", default=None)
    """Next scheduled fire time. Present only on `cron` triggers."""

    sender_id: Optional[str] = FieldInfo(alias="senderId", default=None)
    """Restrict the trigger to a single sender. Null means all senders in the project."""


class TriggerListResponse(BaseModel):
    triggers: List[Trigger]
