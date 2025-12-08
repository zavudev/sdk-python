# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .phone_number_status import PhoneNumberStatus
from .owned_phone_number_pricing import OwnedPhoneNumberPricing

__all__ = ["OwnedPhoneNumber"]


class OwnedPhoneNumber(BaseModel):
    id: str

    capabilities: List[str]

    created_at: datetime = FieldInfo(alias="createdAt")

    phone_number: str = FieldInfo(alias="phoneNumber")

    pricing: OwnedPhoneNumberPricing

    status: PhoneNumberStatus

    name: Optional[str] = None
    """Optional custom name for the phone number."""

    next_renewal_date: Optional[datetime] = FieldInfo(alias="nextRenewalDate", default=None)

    sender_id: Optional[str] = FieldInfo(alias="senderId", default=None)
    """Sender ID if the phone number is assigned to a sender."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
