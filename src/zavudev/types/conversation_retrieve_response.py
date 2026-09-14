# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .channel import Channel
from .._models import BaseModel

__all__ = [
    "ConversationRetrieveResponse",
    "Conversation",
    "ConversationLastMessage",
    "ConversationGroup",
    "ConversationWhatsapp",
]


class ConversationLastMessage(BaseModel):
    """
    Denormalized preview of the most recent message, so a thread list needs no extra fetch.
    """

    id: str

    at: datetime

    channel: Channel
    """Delivery channel. Use 'auto' for intelligent routing."""

    direction: Literal["inbound", "outbound"]

    text: str
    """Text or caption. Empty when the last message carried no text (e.g. media)."""


class ConversationGroup(BaseModel):
    """Present when the thread is a group chat rather than a one-to-one conversation."""

    id: str

    participant_count: Optional[int] = FieldInfo(alias="participantCount", default=None)

    subject: Optional[str] = None


class ConversationWhatsapp(BaseModel):
    """WhatsApp identity, present when the contact adopted a username."""

    bsuid: Optional[str] = None
    """Business-scoped user ID. Can be used as `to` when sending."""

    username: Optional[str] = None


class Conversation(BaseModel):
    """An inbox thread with one contact.

    A conversation groups every message exchanged with that contact across channels, so a contact who writes on WhatsApp and later by email stays in one thread.
    """

    id: str

    channels: List[str]
    """Every channel this thread has carried messages on."""

    contact_identifier: str = FieldInfo(alias="contactIdentifier")
    """
    The key this thread is filed under: a phone number in E.164, a WhatsApp
    business-scoped user ID (BSUID), a numeric chat ID
    (Telegram/Instagram/Messenger), or a group JID. It is not always a phone number,
    so do not parse it as one.
    """

    created_at: datetime = FieldInfo(alias="createdAt")

    last_message: ConversationLastMessage = FieldInfo(alias="lastMessage")
    """
    Denormalized preview of the most recent message, so a thread list needs no extra
    fetch.
    """

    message_count: int = FieldInfo(alias="messageCount")

    unread_count: int = FieldInfo(alias="unreadCount")
    """Inbound messages not yet marked read.

    Reset with POST /v1/conversations/{conversationId}/read.
    """

    updated_at: datetime = FieldInfo(alias="updatedAt")

    contact_id: Optional[str] = FieldInfo(alias="contactId", default=None)
    """ID of the contact this thread belongs to.

    Absent on group threads and on threads whose contact has not been resolved yet.
    """

    email: Optional[str] = None
    """Email address of the thread, when the contact was reached by email."""

    group: Optional[ConversationGroup] = None
    """Present when the thread is a group chat rather than a one-to-one conversation."""

    sender_id: Optional[str] = FieldInfo(alias="senderId", default=None)
    """Sender that last handled this thread.

    Use it as the `Zavu-Sender` header when replying so the answer leaves from the
    same number the contact knows.
    """

    whatsapp: Optional[ConversationWhatsapp] = None
    """WhatsApp identity, present when the contact adopted a username."""


class ConversationRetrieveResponse(BaseModel):
    conversation: Conversation
    """An inbox thread with one contact.

    A conversation groups every message exchanged with that contact across channels,
    so a contact who writes on WhatsApp and later by email stays in one thread.
    """
