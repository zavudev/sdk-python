# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .channel import Channel
from .._models import BaseModel
from .message_type import MessageType
from .message_status import MessageStatus
from .message_content import MessageContent

__all__ = ["Message"]


class Message(BaseModel):
    id: str

    channel: Channel
    """Delivery channel. Use 'auto' for intelligent routing."""

    created_at: datetime = FieldInfo(alias="createdAt")

    message_type: MessageType = FieldInfo(alias="messageType")
    """Type of message.

    Non-text types are supported by WhatsApp and Telegram (varies by type).
    """

    status: MessageStatus

    to: str

    content: Optional[MessageContent] = None
    """Content for non-text message types (WhatsApp and Telegram)."""

    cost: Optional[float] = None
    """MAU cost in USD (charged for first contact of the month)."""

    cost_provider: Optional[float] = FieldInfo(alias="costProvider", default=None)
    """Provider cost in USD (Telnyx, SES, etc.)."""

    cost_total: Optional[float] = FieldInfo(alias="costTotal", default=None)
    """Total cost in USD (MAU + provider cost)."""

    error_code: Optional[str] = FieldInfo(alias="errorCode", default=None)

    error_message: Optional[str] = FieldInfo(alias="errorMessage", default=None)

    from_: Optional[str] = FieldInfo(alias="from", default=None)

    metadata: Optional[Dict[str, str]] = None

    provider_message_id: Optional[str] = FieldInfo(alias="providerMessageId", default=None)
    """Message ID from the delivery provider."""

    sender_id: Optional[str] = FieldInfo(alias="senderId", default=None)

    text: Optional[str] = None
    """Text content or caption."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
