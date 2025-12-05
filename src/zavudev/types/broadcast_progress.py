# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .broadcast_status import BroadcastStatus

__all__ = ["BroadcastProgress"]


class BroadcastProgress(BaseModel):
    broadcast_id: str = FieldInfo(alias="broadcastId")

    delivered: int
    """Successfully delivered."""

    failed: int
    """Failed to deliver."""

    pending: int
    """Not yet queued for sending."""

    percent_complete: float = FieldInfo(alias="percentComplete")
    """Percentage complete (0-100)."""

    sending: int
    """Currently being sent."""

    skipped: int
    """Skipped (broadcast cancelled)."""

    status: BroadcastStatus
    """Current status of the broadcast."""

    total: int
    """Total contacts in broadcast."""

    actual_cost: Optional[float] = FieldInfo(alias="actualCost", default=None)
    """Actual cost so far in USD."""

    estimated_completion_at: Optional[datetime] = FieldInfo(alias="estimatedCompletionAt", default=None)

    estimated_cost: Optional[float] = FieldInfo(alias="estimatedCost", default=None)
    """Estimated total cost in USD."""

    reserved_amount: Optional[float] = FieldInfo(alias="reservedAmount", default=None)
    """Amount reserved from balance in USD."""

    started_at: Optional[datetime] = FieldInfo(alias="startedAt", default=None)
