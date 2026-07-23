# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["InvitationCreateParams"]


class InvitationCreateParams(TypedDict, total=False):
    allowed_phone_countries: Annotated[SequenceNotStr[str], PropertyInfo(alias="allowedPhoneCountries")]
    """ISO country codes for allowed phone numbers."""

    client_email: Annotated[str, PropertyInfo(alias="clientEmail")]
    """Email of the client being invited."""

    client_name: Annotated[str, PropertyInfo(alias="clientName")]
    """Name of the client being invited."""

    client_phone: Annotated[str, PropertyInfo(alias="clientPhone")]
    """Phone number of the client in E.164 format."""

    connection_type: Annotated[Literal["whatsapp_waba"], PropertyInfo(alias="connectionType")]
    """How the client connects WhatsApp.

    `whatsapp_waba` (default) runs Meta's embedded signup to link an official
    WhatsApp Business Account.
    """

    expires_in_days: Annotated[int, PropertyInfo(alias="expiresInDays")]
    """Number of days until the invitation expires."""

    phone_number_id: Annotated[str, PropertyInfo(alias="phoneNumberId")]
    """ID of a Zavu phone number to pre-assign for WhatsApp registration.

    If provided, the client will use this number instead of their own.
    """
