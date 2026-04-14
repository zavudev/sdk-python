# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ContactChannel", "Metrics"]


class Metrics(BaseModel):
    """Delivery metrics for this channel."""

    avg_delivery_time_ms: Optional[float] = FieldInfo(alias="avgDeliveryTimeMs", default=None)

    failure_count: Optional[int] = FieldInfo(alias="failureCount", default=None)

    last_success_at: Optional[datetime] = FieldInfo(alias="lastSuccessAt", default=None)

    success_count: Optional[int] = FieldInfo(alias="successCount", default=None)

    total_attempts: Optional[int] = FieldInfo(alias="totalAttempts", default=None)


class ContactChannel(BaseModel):
    """A communication channel for a contact."""

    id: str

    channel: Literal["sms", "whatsapp", "email", "telegram", "voice"]
    """Channel type."""

    created_at: datetime = FieldInfo(alias="createdAt")

    identifier: str
    """Channel identifier (phone number or email address)."""

    is_primary: bool = FieldInfo(alias="isPrimary")
    """Whether this is the primary channel for its type."""

    verified: bool
    """Whether this channel has been verified."""

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)
    """ISO country code for phone numbers."""

    label: Optional[str] = None
    """Optional label for the channel."""

    last_inbound_at: Optional[datetime] = FieldInfo(alias="lastInboundAt", default=None)
    """Last time a message was received on this channel."""

    metadata: Optional[Dict[str, str]] = None

    metrics: Optional[Metrics] = None
    """Delivery metrics for this channel."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
