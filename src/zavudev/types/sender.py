# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .sender_webhook import SenderWebhook

__all__ = ["Sender", "Whatsapp", "WhatsappPaymentStatus"]


class WhatsappPaymentStatus(BaseModel):
    """Payment configuration status from Meta."""

    can_send_templates: Optional[bool] = FieldInfo(alias="canSendTemplates", default=None)
    """Whether template messages can be sent.

    Requires setupStatus=COMPLETE and methodStatus=VALID.
    """

    method_status: Optional[str] = FieldInfo(alias="methodStatus", default=None)
    """Payment method status (VALID, NONE, etc.)."""

    setup_status: Optional[str] = FieldInfo(alias="setupStatus", default=None)
    """Payment setup status (COMPLETE, NOT_STARTED, etc.)."""


class Whatsapp(BaseModel):
    """WhatsApp Business Account information. Only present if a WABA is connected."""

    display_phone_number: Optional[str] = FieldInfo(alias="displayPhoneNumber", default=None)
    """Display phone number."""

    payment_status: Optional[WhatsappPaymentStatus] = FieldInfo(alias="paymentStatus", default=None)
    """Payment configuration status from Meta."""

    phone_number_id: Optional[str] = FieldInfo(alias="phoneNumberId", default=None)
    """WhatsApp phone number ID from Meta."""


class Sender(BaseModel):
    id: str

    name: str

    phone_number: str = FieldInfo(alias="phoneNumber")
    """Phone number in E.164 format."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    is_default: Optional[bool] = FieldInfo(alias="isDefault", default=None)
    """Whether this sender is the project's default."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    webhook: Optional[SenderWebhook] = None
    """Webhook configuration for the sender."""

    whatsapp: Optional[Whatsapp] = None
    """WhatsApp Business Account information. Only present if a WABA is connected."""
