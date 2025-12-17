# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr
from .whatsapp_business_profile_vertical import WhatsappBusinessProfileVertical

__all__ = ["SenderUpdateProfileParams"]


class SenderUpdateProfileParams(TypedDict, total=False):
    about: str
    """Short description of the business (max 139 characters)."""

    address: str
    """Physical address of the business (max 256 characters)."""

    description: str
    """Extended description of the business (max 512 characters)."""

    email: str
    """Business email address."""

    vertical: WhatsappBusinessProfileVertical
    """Business category for WhatsApp Business profile."""

    websites: SequenceNotStr[str]
    """Business website URLs (maximum 2)."""
