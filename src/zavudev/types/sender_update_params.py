# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SenderUpdateParams"]


class SenderUpdateParams(TypedDict, total=False):
    name: str

    set_as_default: Annotated[bool, PropertyInfo(alias="setAsDefault")]

    webhook_active: Annotated[bool, PropertyInfo(alias="webhookActive")]
    """Whether the webhook is active."""

    webhook_events: Annotated[
        List[Literal["message.sent", "message.delivered", "message.failed", "message.inbound", "conversation.new"]],
        PropertyInfo(alias="webhookEvents"),
    ]
    """Events to subscribe to."""

    webhook_url: Annotated[Optional[str], PropertyInfo(alias="webhookUrl")]
    """HTTPS URL for webhook events. Set to null to remove webhook."""
