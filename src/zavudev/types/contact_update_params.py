# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ContactUpdateParams"]


class ContactUpdateParams(TypedDict, total=False):
    default_channel: Annotated[
        Optional[Literal["sms", "whatsapp", "telegram", "email", "instagram", "messenger", "voice"]],
        PropertyInfo(alias="defaultChannel"),
    ]
    """Preferred channel for this contact. Set to null to clear."""

    display_name: Annotated[Optional[str], PropertyInfo(alias="displayName")]
    """Human-readable name for this contact.

    Set to null to clear it and fall back to the contact's identifier. Contacts
    created automatically from an inbound message have no display name until you set
    one.
    """

    metadata: Dict[str, str]
