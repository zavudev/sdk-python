# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .broadcast_channel import BroadcastChannel
from .broadcast_message_type import BroadcastMessageType
from .broadcast_content_param import BroadcastContentParam

__all__ = ["BroadcastCreateParams"]


class BroadcastCreateParams(TypedDict, total=False):
    channel: Required[BroadcastChannel]
    """Broadcast delivery channel. Use 'smart' for per-contact intelligent routing."""

    name: Required[str]
    """Name of the broadcast campaign."""

    content: BroadcastContentParam
    """Content for non-text broadcast message types."""

    email_html_body: Annotated[str, PropertyInfo(alias="emailHtmlBody")]
    """HTML body for email broadcasts."""

    email_subject: Annotated[str, PropertyInfo(alias="emailSubject")]
    """Email subject line. Required for email broadcasts."""

    idempotency_key: Annotated[str, PropertyInfo(alias="idempotencyKey")]
    """Idempotency key to prevent duplicate broadcasts."""

    message_type: Annotated[BroadcastMessageType, PropertyInfo(alias="messageType")]
    """Type of message for broadcast."""

    metadata: Dict[str, str]

    scheduled_at: Annotated[Union[str, datetime], PropertyInfo(alias="scheduledAt", format="iso8601")]
    """Schedule the broadcast for future delivery."""

    sender_id: Annotated[str, PropertyInfo(alias="senderId")]
    """Sender profile ID. Uses default sender if omitted."""

    text: str
    """Text content or caption. Supports template variables: {{name}}, {{1}}, etc."""
