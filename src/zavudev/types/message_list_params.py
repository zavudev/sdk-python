# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .channel import Channel
from .message_status import MessageStatus

__all__ = ["MessageListParams"]


class MessageListParams(TypedDict, total=False):
    channel: Channel
    """Delivery channel.

    Use 'auto' for intelligent routing. `whatsapp_alt` is the QR-linked WhatsApp
    channel and is only accepted for teams with the WhatsApp Alternative feature
    enabled; the sender must have a connected whatsapp_alt session.
    """

    cursor: str

    limit: int

    status: MessageStatus

    to: str
