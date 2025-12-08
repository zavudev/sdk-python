# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .phone_number_status import PhoneNumberStatus

__all__ = ["PhoneNumberListParams"]


class PhoneNumberListParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor."""

    limit: int

    status: PhoneNumberStatus
    """Filter by phone number status."""
