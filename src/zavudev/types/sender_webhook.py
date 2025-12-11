# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .webhook_event import WebhookEvent

__all__ = ["SenderWebhook"]


class SenderWebhook(BaseModel):
    """Webhook configuration for the sender."""

    active: bool
    """Whether the webhook is active."""

    events: List[WebhookEvent]
    """List of events the webhook is subscribed to."""

    url: str
    """HTTPS URL that will receive webhook events."""

    secret: Optional[str] = None
    """Webhook secret for signature verification.

    Only returned on create or regenerate.
    """
