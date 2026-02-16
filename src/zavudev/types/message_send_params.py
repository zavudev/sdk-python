# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .channel import Channel
from .message_type import MessageType
from .message_content_param import MessageContentParam

__all__ = ["MessageSendParams"]


class MessageSendParams(TypedDict, total=False):
    to: Required[str]
    """Recipient phone number in E.164 format or email address."""

    channel: Channel
    """Delivery channel.

    Use 'auto' for intelligent routing. If omitted with non-text messageType,
    WhatsApp is used. For email recipients, defaults to 'email'.
    """

    content: MessageContentParam
    """Additional content for non-text message types."""

    fallback_enabled: Annotated[bool, PropertyInfo(alias="fallbackEnabled")]
    """Whether to enable automatic fallback to SMS if WhatsApp fails.

    Defaults to true.
    """

    html_body: Annotated[str, PropertyInfo(alias="htmlBody")]
    """HTML body for email messages.

    If provided, email will be sent as multipart with both text and HTML.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="idempotencyKey")]
    """Optional idempotency key to avoid duplicate sends."""

    message_type: Annotated[MessageType, PropertyInfo(alias="messageType")]
    """Type of message. Defaults to 'text'."""

    metadata: Dict[str, str]
    """Arbitrary metadata to associate with the message."""

    reply_to: Annotated[str, PropertyInfo(alias="replyTo")]
    """Reply-To email address for email messages."""

    subject: str
    """Email subject line.

    Required when channel is 'email' or recipient is an email address.
    """

    text: str
    """Text body for text messages or caption for media messages."""

    voice_language: Annotated[str, PropertyInfo(alias="voiceLanguage")]
    """Language code for voice text-to-speech (e.g., 'en-US', 'es-ES', 'pt-BR').

    If omitted, language is auto-detected from recipient's country code.
    """

    zavu_sender: Annotated[str, PropertyInfo(alias="Zavu-Sender")]
