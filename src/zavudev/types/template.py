# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .whatsapp_category import WhatsappCategory

__all__ = ["Template", "Button", "Whatsapp"]


class Button(BaseModel):
    otp_type: Optional[Literal["COPY_CODE", "ONE_TAP"]] = FieldInfo(alias="otpType", default=None)
    """OTP button type. Required when type is 'otp'."""

    package_name: Optional[str] = FieldInfo(alias="packageName", default=None)
    """Android package name. Required for ONE_TAP buttons."""

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)

    signature_hash: Optional[str] = FieldInfo(alias="signatureHash", default=None)
    """Android app signature hash. Required for ONE_TAP buttons."""

    text: Optional[str] = None

    type: Optional[Literal["quick_reply", "url", "phone", "otp"]] = None

    url: Optional[str] = None


class Whatsapp(BaseModel):
    """WhatsApp-specific template information."""

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

    add_security_recommendation: Optional[bool] = FieldInfo(alias="addSecurityRecommendation", default=None)
    """Add 'Do not share this code' disclaimer. Only for AUTHENTICATION templates."""

    buttons: Optional[List[Button]] = None
    """Template buttons."""

    code_expiration_minutes: Optional[int] = FieldInfo(alias="codeExpirationMinutes", default=None)
    """Code expiration time in minutes. Only for AUTHENTICATION templates."""

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
