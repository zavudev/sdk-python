# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["BroadcastContent"]


class BroadcastContent(BaseModel):
    """Content for non-text broadcast message types."""

    filename: Optional[str] = None
    """Filename for documents."""

    media_id: Optional[str] = FieldInfo(alias="mediaId", default=None)
    """Media ID if already uploaded."""

    media_url: Optional[str] = FieldInfo(alias="mediaUrl", default=None)
    """URL of the media file."""

    mime_type: Optional[str] = FieldInfo(alias="mimeType", default=None)
    """MIME type of the media."""

    template_button_variables: Optional[Dict[str, str]] = FieldInfo(alias="templateButtonVariables", default=None)
    """Default button variables for dynamic URL/OTP buttons.

    Keys are the button index (0, 1, 2). Per-contact values override these.
    """

    template_header_variables: Optional[Dict[str, str]] = FieldInfo(alias="templateHeaderVariables", default=None)
    """
    Default value for a text-header variable, keyed by `1` (can be overridden per
    contact). If omitted, Zavu resolves the header from `templateVariables` by the
    header placeholder's name.
    """

    template_id: Optional[str] = FieldInfo(alias="templateId", default=None)
    """Template ID for template messages."""

    template_variables: Optional[Dict[str, str]] = FieldInfo(alias="templateVariables", default=None)
    """Default body variables (can be overridden per contact).

    Key them to match the template body: by position (`1`, `2`, ...) for positional
    templates, or by name (e.g. `customer_name`) for named templates. Zavu detects
    the template's format and sends the correct payload to Meta. Do not mix
    positional and named keys.
    """
