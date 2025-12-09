# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["MessageContentParam", "Button", "Contact", "Section", "SectionRow"]


class Button(TypedDict, total=False):
    id: Required[str]

    title: Required[str]


class Contact(TypedDict, total=False):
    name: str

    phones: SequenceNotStr[str]


class SectionRow(TypedDict, total=False):
    id: Required[str]

    title: Required[str]

    description: str


class Section(TypedDict, total=False):
    rows: Required[Iterable[SectionRow]]

    title: Required[str]


class MessageContentParam(TypedDict, total=False):
    """Content for non-text message types (WhatsApp only)."""

    buttons: Iterable[Button]
    """Interactive buttons (max 3)."""

    contacts: Iterable[Contact]
    """Contact cards for contact messages."""

    emoji: str
    """Emoji for reaction messages."""

    filename: str
    """Filename for documents."""

    latitude: float
    """Latitude for location messages."""

    list_button: Annotated[str, PropertyInfo(alias="listButton")]
    """Button text for list messages."""

    location_address: Annotated[str, PropertyInfo(alias="locationAddress")]
    """Address of the location."""

    location_name: Annotated[str, PropertyInfo(alias="locationName")]
    """Name of the location."""

    longitude: float
    """Longitude for location messages."""

    media_id: Annotated[str, PropertyInfo(alias="mediaId")]
    """WhatsApp media ID if already uploaded."""

    media_url: Annotated[str, PropertyInfo(alias="mediaUrl")]
    """URL of the media file (for image, video, audio, document, sticker)."""

    mime_type: Annotated[str, PropertyInfo(alias="mimeType")]
    """MIME type of the media."""

    react_to_message_id: Annotated[str, PropertyInfo(alias="reactToMessageId")]
    """Message ID to react to."""

    sections: Iterable[Section]
    """Sections for list messages."""

    template_id: Annotated[str, PropertyInfo(alias="templateId")]
    """Template ID for template messages."""

    template_variables: Annotated[Dict[str, str], PropertyInfo(alias="templateVariables")]
    """Variables for template rendering. Keys are variable positions (1, 2, 3...)."""
