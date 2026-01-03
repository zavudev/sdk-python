# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .webhook_event import WebhookEvent

__all__ = ["SenderUpdateParams"]


class SenderUpdateParams(TypedDict, total=False):
    email_receiving_enabled: Annotated[bool, PropertyInfo(alias="emailReceivingEnabled")]
    """Enable or disable inbound email receiving for this sender."""

    name: str

    set_as_default: Annotated[bool, PropertyInfo(alias="setAsDefault")]

    webhook_active: Annotated[bool, PropertyInfo(alias="webhookActive")]
    """Whether the webhook is active."""

    webhook_events: Annotated[List[WebhookEvent], PropertyInfo(alias="webhookEvents")]
    """Events to subscribe to."""

    webhook_url: Annotated[Optional[str], PropertyInfo(alias="webhookUrl")]
    """HTTPS URL for webhook events. Set to null to remove webhook."""
