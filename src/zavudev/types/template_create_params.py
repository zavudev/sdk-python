# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .whatsapp_category import WhatsappCategory

__all__ = ["TemplateCreateParams", "Button"]


class TemplateCreateParams(TypedDict, total=False):
    body: Required[str]

    language: Required[str]

    name: Required[str]

    add_security_recommendation: Annotated[bool, PropertyInfo(alias="addSecurityRecommendation")]
    """Add 'Do not share this code' disclaimer. Only for AUTHENTICATION templates."""

    buttons: Iterable[Button]
    """Template buttons (max 3)."""

    code_expiration_minutes: Annotated[int, PropertyInfo(alias="codeExpirationMinutes")]
    """Code expiration time in minutes. Only for AUTHENTICATION templates."""

    variables: SequenceNotStr[str]

    whatsapp_category: Annotated[WhatsappCategory, PropertyInfo(alias="whatsappCategory")]
    """WhatsApp template category."""


class Button(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["quick_reply", "url", "phone", "otp"]]

    otp_type: Annotated[Literal["COPY_CODE", "ONE_TAP"], PropertyInfo(alias="otpType")]
    """Required when type is 'otp'.

    COPY_CODE shows copy button, ONE_TAP enables Android autofill.
    """

    package_name: Annotated[str, PropertyInfo(alias="packageName")]
    """Android package name. Required for ONE_TAP buttons."""

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]

    signature_hash: Annotated[str, PropertyInfo(alias="signatureHash")]
    """Android app signature hash. Required for ONE_TAP buttons."""

    url: str
