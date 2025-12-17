# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .whatsapp_business_profile_vertical import WhatsappBusinessProfileVertical

__all__ = ["WhatsappBusinessProfile"]


class WhatsappBusinessProfile(BaseModel):
    """WhatsApp Business profile information."""

    about: Optional[str] = None
    """Short description of the business (max 139 characters)."""

    address: Optional[str] = None
    """Physical address of the business (max 256 characters)."""

    description: Optional[str] = None
    """Extended description of the business (max 512 characters)."""

    email: Optional[str] = None
    """Business email address."""

    profile_picture_url: Optional[str] = FieldInfo(alias="profilePictureUrl", default=None)
    """URL of the business profile picture."""

    vertical: Optional[WhatsappBusinessProfileVertical] = None
    """Business category for WhatsApp Business profile."""

    websites: Optional[List[str]] = None
    """Business website URLs (maximum 2)."""
