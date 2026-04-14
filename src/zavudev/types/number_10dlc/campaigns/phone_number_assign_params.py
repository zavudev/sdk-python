# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["PhoneNumberAssignParams"]


class PhoneNumberAssignParams(TypedDict, total=False):
    phone_number_id: Required[Annotated[str, PropertyInfo(alias="phoneNumberId")]]
    """ID of the phone number to assign."""
