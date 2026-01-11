# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .broadcast_status import BroadcastStatus
from .broadcast_channel import BroadcastChannel
from .broadcast_content import BroadcastContent
from .broadcast_message_type import BroadcastMessageType

__all__ = ["Broadcast", "ReviewResult"]


class ReviewResult(BaseModel):
    """AI content review result."""

    categories: Optional[List[str]] = None
    """Policy categories violated, if any."""

    flagged_content: Optional[List[str]] = FieldInfo(alias="flaggedContent", default=None)
    """Problematic text fragments, if any."""

    reasoning: Optional[str] = None
    """Explanation of the review decision."""

    reviewed_at: Optional[datetime] = FieldInfo(alias="reviewedAt", default=None)

    score: Optional[float] = None
    """Content safety score from 0.0 to 1.0, where 1.0 is completely safe."""


class Broadcast(BaseModel):
    id: str

    channel: BroadcastChannel
    """Broadcast delivery channel. Use 'smart' for per-contact intelligent routing."""

    created_at: datetime = FieldInfo(alias="createdAt")

    message_type: BroadcastMessageType = FieldInfo(alias="messageType")
    """Type of message for broadcast."""

    name: str

    status: BroadcastStatus
    """Current status of the broadcast."""

    total_contacts: int = FieldInfo(alias="totalContacts")
    """Total number of contacts in the broadcast."""

    actual_cost: Optional[float] = FieldInfo(alias="actualCost", default=None)
    """Actual cost so far in USD."""

    completed_at: Optional[datetime] = FieldInfo(alias="completedAt", default=None)

    content: Optional[BroadcastContent] = None
    """Content for non-text broadcast message types."""

    delivered_count: Optional[int] = FieldInfo(alias="deliveredCount", default=None)

    email_subject: Optional[str] = FieldInfo(alias="emailSubject", default=None)

    estimated_cost: Optional[float] = FieldInfo(alias="estimatedCost", default=None)
    """Estimated total cost in USD."""

    failed_count: Optional[int] = FieldInfo(alias="failedCount", default=None)

    metadata: Optional[Dict[str, str]] = None

    pending_count: Optional[int] = FieldInfo(alias="pendingCount", default=None)

    reserved_amount: Optional[float] = FieldInfo(alias="reservedAmount", default=None)
    """Amount reserved from balance in USD."""

    review_attempts: Optional[int] = FieldInfo(alias="reviewAttempts", default=None)
    """Number of review attempts (max 3)."""

    review_result: Optional[ReviewResult] = FieldInfo(alias="reviewResult", default=None)
    """AI content review result."""

    scheduled_at: Optional[datetime] = FieldInfo(alias="scheduledAt", default=None)

    sender_id: Optional[str] = FieldInfo(alias="senderId", default=None)

    sending_count: Optional[int] = FieldInfo(alias="sendingCount", default=None)

    started_at: Optional[datetime] = FieldInfo(alias="startedAt", default=None)

    text: Optional[str] = None

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
