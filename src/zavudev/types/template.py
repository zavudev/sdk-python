# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .whatsapp_category import WhatsappCategory

__all__ = ["Template", "Button", "Whatsapp"]


class Button(BaseModel):
    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)

    text: Optional[str] = None

    type: Optional[str] = None

    url: Optional[str] = None


class Whatsapp(BaseModel):
    namespace: Optional[str] = None
    """WhatsApp Business Account namespace."""

    status: Optional[str] = None
    """WhatsApp approval status."""

    template_name: Optional[str] = FieldInfo(alias="templateName", default=None)
    """WhatsApp template name."""


class Template(BaseModel):
    id: str

    body: str
    """Template body with variables: {{1}}, {{2}}, etc."""

    category: WhatsappCategory
    """WhatsApp template category."""

    language: str
    """Language code."""

    name: str
    """Template name (must match WhatsApp template name)."""

    buttons: Optional[List[Button]] = None
    """Template buttons."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    footer: Optional[str] = None
    """Footer text for the template."""

    header_content: Optional[str] = FieldInfo(alias="headerContent", default=None)
    """Header content (text or media URL)."""

    header_type: Optional[str] = FieldInfo(alias="headerType", default=None)
    """Type of header (text, image, video, document)."""

    status: Optional[Literal["draft", "pending", "approved", "rejected"]] = None

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    variables: Optional[List[str]] = None
    """List of variable names for documentation."""

    whatsapp: Optional[Whatsapp] = None
    """WhatsApp-specific template information."""
