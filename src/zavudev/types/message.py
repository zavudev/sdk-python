# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

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

    direction: Literal["inbound", "outbound"]
    """Who sent the message.

    Needed to render a thread: `status` cannot tell the two apart, because an
    inbound message is also stored as `delivered`.
    """

    message_type: MessageType = FieldInfo(alias="messageType")
    """Type of message.

    Non-text types are supported by WhatsApp and Telegram (varies by type).

    `location_request` asks the recipient to share their location and is
    WhatsApp-only. It takes no `content` object — the prompt goes in `text` (max
    1024 characters) and the button label is fixed by WhatsApp. The recipient's
    answer arrives as an inbound `location` message whose `content.replyToMessageId`
    is the ID of the request.

    `request_contact_info` asks the recipient to share their phone number and is
    WhatsApp-only. Like `location_request` it takes no `content` object — the prompt
    goes in `text` (max 1024 characters) and WhatsApp renders a fixed **Share
    Contact Info** button. The answer arrives as an inbound `contact` message. Use
    it to recover the phone number of a contact who adopted a WhatsApp username and
    is only known by their business-scoped user ID (BSUID); when they share it, Zavu
    automatically links the phone number to that contact.
    """

    status: MessageStatus

    to: str

    content: Optional[MessageContent] = None
    """Content for non-text message types (WhatsApp and Telegram)."""

    conversation_id: Optional[str] = FieldInfo(alias="conversationId", default=None)
    """ID of the conversation (inbox thread) this message belongs to.

    Use it to build a direct dashboard link:
    `https://dashboard.zavu.dev/{locale}/inbox?conv={conversationId}`. Omitted only
    on legacy messages created before conversation threading.
    """

    cost: Optional[float] = None
    """Zavu platform charge in USD for this message.

    Messaging is billed against your plan's monthly limits plus usage-based overage.
    """

    cost_provider: Optional[float] = FieldInfo(alias="costProvider", default=None)
    """Carrier and delivery cost in USD."""

    cost_total: Optional[float] = FieldInfo(alias="costTotal", default=None)
    """Total cost in USD (platform charge + delivery cost)."""

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
