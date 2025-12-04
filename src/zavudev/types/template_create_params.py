# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .whatsapp_category import WhatsappCategory

__all__ = ["TemplateCreateParams"]


class TemplateCreateParams(TypedDict, total=False):
    body: Required[str]

    language: Required[str]

    name: Required[str]

    variables: SequenceNotStr[str]

    whatsapp_category: Annotated[WhatsappCategory, PropertyInfo(alias="whatsappCategory")]
    """WhatsApp template category."""
