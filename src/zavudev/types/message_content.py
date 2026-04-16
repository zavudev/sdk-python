# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MessageContent", "Button", "Contact", "Section", "SectionRow"]


class Button(BaseModel):
    id: str

    title: str


class Contact(BaseModel):
    name: Optional[str] = None

    phones: Optional[List[str]] = None


class SectionRow(BaseModel):
    id: str

    title: str

    description: Optional[str] = None


class Section(BaseModel):
    rows: List[SectionRow]

    title: str


class MessageContent(BaseModel):
    """Content for non-text message types (WhatsApp and Telegram)."""

    buttons: Optional[List[Button]] = None
    """Interactive buttons (max 3)."""

    contacts: Optional[List[Contact]] = None
    """Contact cards for contact messages."""

    cta_display_text: Optional[str] = FieldInfo(alias="ctaDisplayText", default=None)
    """Button label for cta_url messages."""

    cta_header_media_url: Optional[str] = FieldInfo(alias="ctaHeaderMediaUrl", default=None)
    """
    Public HTTPS URL of the header media when ctaHeaderType is 'image', 'video', or
    'document'. WhatsApp fetches this URL — it must be publicly reachable and return
    the declared content type.
    """

    cta_header_text: Optional[str] = FieldInfo(alias="ctaHeaderText", default=None)
    """Header text when ctaHeaderType is 'text'."""

    cta_header_type: Optional[Literal["text", "image", "video", "document"]] = FieldInfo(
        alias="ctaHeaderType", default=None
    )
    """Optional header type for cta_url messages."""

    cta_url: Optional[str] = FieldInfo(alias="ctaUrl", default=None)
    """Destination URL opened in the device's default browser when the button is
    tapped.

    Used with messageType=cta_url. WhatsApp requires HTTPS in production.
    """

    emoji: Optional[str] = None
    """Emoji for reaction messages."""

    filename: Optional[str] = None
    """Filename for documents."""

    footer_text: Optional[str] = FieldInfo(alias="footerText", default=None)
    """Optional footer text for cta_url messages."""

    latitude: Optional[float] = None
    """Latitude for location messages."""

    list_button: Optional[str] = FieldInfo(alias="listButton", default=None)
    """Button text for list messages."""

    location_address: Optional[str] = FieldInfo(alias="locationAddress", default=None)
    """Address of the location."""

    location_name: Optional[str] = FieldInfo(alias="locationName", default=None)
    """Name of the location."""

    longitude: Optional[float] = None
    """Longitude for location messages."""

    media_id: Optional[str] = FieldInfo(alias="mediaId", default=None)
    """WhatsApp media ID if already uploaded."""

    media_url: Optional[str] = FieldInfo(alias="mediaUrl", default=None)
    """URL of the media file (for image, video, audio, document, sticker)."""

    mime_type: Optional[str] = FieldInfo(alias="mimeType", default=None)
    """MIME type of the media."""

    react_to_message_id: Optional[str] = FieldInfo(alias="reactToMessageId", default=None)
    """Message ID to react to."""

    sections: Optional[List[Section]] = None
    """Sections for list messages."""

    template_id: Optional[str] = FieldInfo(alias="templateId", default=None)
    """Template ID for template messages."""

    template_variables: Optional[Dict[str, str]] = FieldInfo(alias="templateVariables", default=None)
    """Variables for template rendering. Keys are variable positions (1, 2, 3...)."""
