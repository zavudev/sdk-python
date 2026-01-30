# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Contact", "Channel", "ChannelMetrics"]


class ChannelMetrics(BaseModel):
    """Delivery metrics for this channel."""

    avg_delivery_time_ms: Optional[float] = FieldInfo(alias="avgDeliveryTimeMs", default=None)

    failure_count: Optional[int] = FieldInfo(alias="failureCount", default=None)

    last_success_at: Optional[datetime] = FieldInfo(alias="lastSuccessAt", default=None)

    success_count: Optional[int] = FieldInfo(alias="successCount", default=None)

    total_attempts: Optional[int] = FieldInfo(alias="totalAttempts", default=None)


class Channel(BaseModel):
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

    metrics: Optional[ChannelMetrics] = None
    """Delivery metrics for this channel."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)


class Contact(BaseModel):
    id: str

    available_channels: List[str] = FieldInfo(alias="availableChannels")
    """List of available messaging channels for this contact."""

    created_at: datetime = FieldInfo(alias="createdAt")

    metadata: Dict[str, str]

    verified: bool
    """Whether this contact has been verified."""

    channels: Optional[List[Channel]] = None
    """All communication channels for this contact."""

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    default_channel: Optional[Literal["sms", "whatsapp", "telegram", "email", "instagram", "voice"]] = FieldInfo(
        alias="defaultChannel", default=None
    )
    """Preferred channel for this contact."""

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
    """Display name for the contact."""

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)
    """DEPRECATED: Use primaryPhone instead. Primary phone number in E.164 format."""

    primary_email: Optional[str] = FieldInfo(alias="primaryEmail", default=None)
    """Primary email address."""

    primary_phone: Optional[str] = FieldInfo(alias="primaryPhone", default=None)
    """Primary phone number in E.164 format."""

    profile_name: Optional[str] = FieldInfo(alias="profileName", default=None)
    """Contact's WhatsApp profile name. Only available for WhatsApp contacts."""

    suggested_merge_with: Optional[str] = FieldInfo(alias="suggestedMergeWith", default=None)
    """ID of a contact suggested for merging."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
