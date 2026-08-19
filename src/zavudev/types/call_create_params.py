# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CallCreateParams"]


class CallCreateParams(TypedDict, total=False):
    to: Required[str]
    """Recipient phone number in E.164 format."""

    greeting: str
    """Overrides the agent's configured greeting for this call only."""

    language: str
    """
    Language the agent speaks on this call only, as a BCP-47 tag (`en`, `es`,
    `es-ES`, `pt-BR`), or `auto` to detect the caller's language and follow it.
    Overrides the agent's configured language for speech recognition, the agent's
    replies, and the synthesized voice. If the agent uses a custom voice you
    supplied, that voice is kept and only the language changes. When omitted, the
    agent's configured language is used.
    """

    max_duration_minutes: Annotated[int, PropertyInfo(alias="maxDurationMinutes")]
    """Overrides the agent's maximum call duration for this call only."""

    metadata: Dict[str, str]
    """Arbitrary metadata to associate with the call.

    Returned on the call object and included in voice webhooks.
    """

    sender_id: Annotated[str, PropertyInfo(alias="senderId")]
    """Sender profile that places the call.

    Uses the project's default sender if omitted. The sender's agent must have voice
    enabled.
    """
