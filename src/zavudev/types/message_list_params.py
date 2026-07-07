# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["MessageListParams"]


class MessageListParams(TypedDict, total=False):
    channel: Literal["sms", "sms_oneway", "whatsapp", "email", "telegram", "instagram", "messenger", "voice"]
    """Filter by delivery channel."""

    cursor: str

    limit: int

    status: Literal["queued", "sending", "sent", "delivered", "failed", "received"]
    """Filter by status. Not all stored statuses are filterable."""

    to: str
