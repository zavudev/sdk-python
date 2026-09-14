# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

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

    regulatory_status: Literal["approved", "pending_review", "rejected"] = FieldInfo(alias="regulatoryStatus")
    """Regulatory review state.

    Numbers that need no review are `approved` immediately. A number bought with
    regulatory information is owned and billed from purchase and starts
    `pending_review`; it cannot send messages or place calls until this is
    `approved`. The state is re-checked every 6 hours: poll
    `GET /v1/phone-numbers/{phoneNumberId}` to follow it.

    Assign it to a sender with `PATCH /v1/phone-numbers/{phoneNumberId}`
    (`senderId`) before or after approval. A number assigned while under review is
    recorded and connected to that sender when it is approved; the connection is
    retried until it succeeds. A sender created over the API is set up for SMS as
    part of the assignment. `rejected` means review refused the information: the
    number cannot be assigned to a sender. A number that stays `pending_review` may
    be waiting on information the API cannot supply; contact support.
    """

    status: PhoneNumberStatus
    """Billing state of an owned number, separate from `regulatoryStatus`.

    `pending` is legacy and is not written to numbers today. The SDKs carry
    `active`, `suspended` and `pending` only; `releasing` and `released` are
    returned by the REST API until their next release.
    """

    name: Optional[str] = None
    """Optional custom name for the phone number."""

    next_renewal_date: Optional[datetime] = FieldInfo(alias="nextRenewalDate", default=None)

    sender_id: Optional[str] = FieldInfo(alias="senderId", default=None)
    """Sender ID if the phone number is assigned to a sender."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
