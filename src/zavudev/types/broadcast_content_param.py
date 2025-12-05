# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BroadcastContentParam"]


class BroadcastContentParam(TypedDict, total=False):
    filename: str
    """Filename for documents."""

    media_id: Annotated[str, PropertyInfo(alias="mediaId")]
    """Media ID if already uploaded."""

    media_url: Annotated[str, PropertyInfo(alias="mediaUrl")]
    """URL of the media file."""

    mime_type: Annotated[str, PropertyInfo(alias="mimeType")]
    """MIME type of the media."""

    template_id: Annotated[str, PropertyInfo(alias="templateId")]
    """Template ID for template messages."""

    template_variables: Annotated[Dict[str, str], PropertyInfo(alias="templateVariables")]
    """Default template variables (can be overridden per contact)."""
