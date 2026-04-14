# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["UsageRetrieveResponse", "Limits"]


class Limits(BaseModel):
    emails: Optional[int] = None

    messages_a2_p: Optional[int] = FieldInfo(alias="messagesA2P", default=None)


class UsageRetrieveResponse(BaseModel):
    emails_sent: int = FieldInfo(alias="emailsSent")
    """Emails sent this month."""

    limits: Limits

    messages_a2_p: int = FieldInfo(alias="messagesA2P")
    """A2P messages sent this month (WhatsApp replies + Telegram)."""

    month_key: str = FieldInfo(alias="monthKey")
    """Current month in YYYY-MM format."""

    tier: Literal["free", "pro", "scale", "enterprise"]
