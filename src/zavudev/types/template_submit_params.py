# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .whatsapp_category import WhatsappCategory

__all__ = ["TemplateSubmitParams"]


class TemplateSubmitParams(TypedDict, total=False):
    sender_id: Required[Annotated[str, PropertyInfo(alias="senderId")]]
    """The sender ID with the WhatsApp Business Account to submit the template to."""

    category: WhatsappCategory
    """Template category. If not provided, uses the category set on the template."""
