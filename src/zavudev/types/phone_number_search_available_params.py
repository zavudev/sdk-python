# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .phone_number_type import PhoneNumberType

__all__ = ["PhoneNumberSearchAvailableParams"]


class PhoneNumberSearchAvailableParams(TypedDict, total=False):
    country_code: Required[Annotated[str, PropertyInfo(alias="countryCode")]]
    """Two-letter ISO country code."""

    contains: str
    """Search for numbers containing this string."""

    limit: int
    """Maximum number of results to return."""

    type: PhoneNumberType
    """Type of phone number to search for."""
