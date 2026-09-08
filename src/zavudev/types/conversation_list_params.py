# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ConversationListParams"]


class ConversationListParams(TypedDict, total=False):
    channel: Literal["sms", "sms_oneway", "whatsapp", "email", "telegram", "instagram", "messenger", "voice"]
    """Keep only threads that have carried this channel."""

    cursor: str
    """Opaque cursor from a previous response's `nextCursor`. Do not construct it."""

    limit: int

    search: str
    """
    Search threads by identity: phone number (any format — `+1 (555) 123-4567` and
    `15551234567` both match), email address (full or local part), WhatsApp group
    subject, WhatsApp username, or BSUID. Matching is by whole word, with prefix
    matching on the last term, so `mar` finds `maria@example.com` and `+1555` finds
    `+15551234567`; a fragment from the middle or end of a number (`4567`) does not
    match.

    It does **not** search message bodies — only who the thread is with.

    Results come back ranked by relevance rather than by recency, so the usual "most
    recently active first" ordering does not apply while `q` is set. `senderId` and
    `channel` still narrow the results, and `cursor` paginates them as usual. An
    empty or whitespace-only `q` returns no items rather than the full list.
    """

    sender_id: Annotated[str, PropertyInfo(alias="senderId")]
    """Keep only threads last handled by this sender."""
