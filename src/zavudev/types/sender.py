# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Sender", "Webhook"]


class Webhook(BaseModel):
    """Webhook configuration for the sender."""

    active: bool
    """Whether the webhook is active."""

    events: List[Literal["message.sent", "message.delivered", "message.failed", "message.inbound", "conversation.new"]]
    """List of events the webhook is subscribed to."""

    url: str
    """HTTPS URL that will receive webhook events."""

    secret: Optional[str] = None
    """Webhook secret for signature verification.

    Only returned on create or regenerate.
    """


class Sender(BaseModel):
    id: str

    name: str

    phone_number: str = FieldInfo(alias="phoneNumber")
    """Phone number in E.164 format."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    is_default: Optional[bool] = FieldInfo(alias="isDefault", default=None)
    """Whether this sender is the project's default."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    webhook: Optional[Webhook] = None
    """Webhook configuration for the sender."""
