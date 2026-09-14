# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .phone_number_type import PhoneNumberType

__all__ = ["PhoneNumberRequirementsParams"]


class PhoneNumberRequirementsParams(TypedDict, total=False):
    country_code: Annotated[str, PropertyInfo(alias="countryCode")]
    """Two-letter ISO country code. Required unless `phoneNumber` is given."""

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """E.164 number from `GET /v1/phone-numbers/available`, with `+` encoded as `%2B`.

    Returns the requirements the purchase of that number checks. Takes precedence
    over `countryCode`.
    """

    type: PhoneNumberType
    """Type of phone number (local, national, mobile, tollFree).

    Defaults to `local`. With `phoneNumber`, used only when the number's own
    requirements cannot be resolved and the country list is returned.
    """
