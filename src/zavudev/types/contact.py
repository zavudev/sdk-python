# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Contact"]


class Contact(BaseModel):
    id: str

    phone_number: str = FieldInfo(alias="phoneNumber")
    """E.164 phone number."""

    available_channels: Optional[List[str]] = FieldInfo(alias="availableChannels", default=None)
    """List of available messaging channels for this contact."""

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    default_channel: Optional[Literal["sms", "whatsapp", "telegram", "email"]] = FieldInfo(
        alias="defaultChannel", default=None
    )
    """Preferred channel for this contact."""

    metadata: Optional[Dict[str, str]] = None

    profile_name: Optional[str] = FieldInfo(alias="profileName", default=None)
    """Contact's WhatsApp profile name. Only available for WhatsApp contacts."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    verified: Optional[bool] = None
    """Whether this contact has been verified."""
