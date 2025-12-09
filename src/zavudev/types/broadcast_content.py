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

    template_id: Optional[str] = FieldInfo(alias="templateId", default=None)
    """Template ID for template messages."""

    template_variables: Optional[Dict[str, str]] = FieldInfo(alias="templateVariables", default=None)
    """Default template variables (can be overridden per contact)."""
