# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ContactCreateParams", "Channel"]


class ContactCreateParams(TypedDict, total=False):
    channels: Required[Iterable[Channel]]
    """Communication channels for the contact."""

    display_name: Annotated[str, PropertyInfo(alias="displayName")]
    """Display name for the contact."""

    metadata: Dict[str, str]
    """Arbitrary metadata to associate with the contact."""


class Channel(TypedDict, total=False):
    """Input for creating a contact channel."""

    channel: Required[Literal["sms", "whatsapp", "email", "telegram", "voice"]]
    """Channel type."""

    identifier: Required[str]
    """Channel identifier (phone number in E.164 format or email address)."""

    country_code: Annotated[str, PropertyInfo(alias="countryCode")]
    """ISO country code for phone numbers."""

    is_primary: Annotated[bool, PropertyInfo(alias="isPrimary")]
    """Whether this should be the primary channel for its type."""

    label: str
    """Optional label for the channel."""
