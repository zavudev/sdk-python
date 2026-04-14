# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ChannelAddParams"]


class ChannelAddParams(TypedDict, total=False):
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
