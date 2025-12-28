# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .phone_number_type import PhoneNumberType

__all__ = ["PhoneNumberRequirementsParams"]


class PhoneNumberRequirementsParams(TypedDict, total=False):
    country_code: Required[Annotated[str, PropertyInfo(alias="countryCode")]]
    """Two-letter ISO country code."""

    type: PhoneNumberType
    """Type of phone number (local, mobile, tollFree)."""
