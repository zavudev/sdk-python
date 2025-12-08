# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PhoneNumberUpdateParams"]


class PhoneNumberUpdateParams(TypedDict, total=False):
    name: Optional[str]
    """Custom name for the phone number. Set to null to clear."""

    sender_id: Annotated[Optional[str], PropertyInfo(alias="senderId")]
    """Sender ID to assign the phone number to. Set to null to unassign."""
