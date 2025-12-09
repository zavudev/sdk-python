# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .line_type import LineType

__all__ = ["IntrospectValidatePhoneResponse", "Carrier"]


class Carrier(BaseModel):
    """Carrier information for the phone number."""

    name: Optional[str] = None
    """Carrier name."""

    type: Optional[LineType] = None
    """Type of phone line."""


class IntrospectValidatePhoneResponse(BaseModel):
    country_code: str = FieldInfo(alias="countryCode")

    phone_number: str = FieldInfo(alias="phoneNumber")

    valid_number: bool = FieldInfo(alias="validNumber")

    available_channels: Optional[List[str]] = FieldInfo(alias="availableChannels", default=None)
    """List of available messaging channels for this phone number."""

    carrier: Optional[Carrier] = None
    """Carrier information for the phone number."""

    line_type: Optional[LineType] = FieldInfo(alias="lineType", default=None)
    """Type of phone line."""

    national_format: Optional[str] = FieldInfo(alias="nationalFormat", default=None)
    """Phone number in national format."""
