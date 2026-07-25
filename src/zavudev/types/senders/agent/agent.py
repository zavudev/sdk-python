# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ..agent_provider import AgentProvider

__all__ = ["Agent", "Stats", "Voice"]


class Stats(BaseModel):
    total_cost: Optional[float] = FieldInfo(alias="totalCost", default=None)
    """Total cost in USD."""

    total_invocations: Optional[int] = FieldInfo(alias="totalInvocations", default=None)

    total_tokens_used: Optional[int] = FieldInfo(alias="totalTokensUsed", default=None)


class Voice(BaseModel):
    """Voice Agent configuration.

    When present and enabled, the agent can answer inbound phone calls and place outbound calls with Zavu's managed voice pipeline. Requires the Voice Agents feature to be enabled for your team.
    """

    enabled: bool
    """Whether the agent handles voice calls.

    When false, the sender's number is not answered by the voice agent and outbound
    calls are rejected.
    """

    greeting: Optional[str] = None
    """Opening line the agent speaks when the call connects.

    If omitted, the agent waits for the caller to speak first.
    """

    greetings: Optional[Dict[str, str]] = None
    """Greeting per language, keyed by language code.

    Used when the caller's language differs from the one `greeting` is written in.
    """

    interruptible: Optional[bool] = None
    """Whether the caller can interrupt the agent while it is speaking (barge-in).

    When true, the agent stops talking as soon as the caller starts.
    """

    language: Optional[str] = None
    """BCP-47 language code used for both speech recognition and speech synthesis (e.g.

    `en`, `es`, `pt-BR`). Auto-detected from the recipient when omitted.
    """

    max_call_duration_minutes: Optional[int] = FieldInfo(alias="maxCallDurationMinutes", default=None)
    """Hard limit on call length in minutes. The call ends automatically when reached."""

    max_idle_seconds: Optional[int] = FieldInfo(alias="maxIdleSeconds", default=None)
    """How long the agent waits during silence before ending the call."""

    model: Optional[str] = None
    """
    Model that runs the conversation, co-located in the voice network for lowest
    latency. Independent of the model used for text messaging. Derived from the
    agent's text model when omitted.
    """

    record_calls: Optional[bool] = FieldInfo(alias="recordCalls", default=None)
    """Whether the call audio is recorded."""

    stt_model: Optional[str] = FieldInfo(alias="sttModel", default=None)
    """Speech-recognition model. Uses the default when omitted."""

    stt_provider: Optional[str] = FieldInfo(alias="sttProvider", default=None)
    """Speech-recognition provider. Uses the default when omitted."""

    transfer_phone_number: Optional[str] = FieldInfo(alias="transferPhoneNumber", default=None)
    """E.164 phone number the agent can transfer the call to.

    When set, the agent is given a transfer tool it can use to hand the call to a
    human.
    """

    tts_provider: Optional[str] = FieldInfo(alias="ttsProvider", default=None)
    """Speech-synthesis provider. Uses the default when omitted."""

    tts_voice_id: Optional[str] = FieldInfo(alias="ttsVoiceId", default=None)
    """Identifier of the synthesized voice that speaks.

    Choose from the voices available in the dashboard. Uses a neutral default when
    omitted.
    """

    voicemail_action: Optional[Literal["hangup", "leave_message"]] = FieldInfo(alias="voicemailAction", default=None)
    """
    What the agent does when an answering machine or voicemail is detected on an
    outbound call.
    """

    voicemail_message: Optional[str] = FieldInfo(alias="voicemailMessage", default=None)
    """Message spoken when `voicemailAction` is `leave_message`.

    Falls back to `greeting` when omitted.
    """

    voice_speed: Optional[float] = FieldInfo(alias="voiceSpeed", default=None)
    """Speech rate.

    1.0 is natural. Only honoured by voices that support rate control; ignored by
    the others.
    """


class Agent(BaseModel):
    """AI Agent configuration for a sender."""

    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    enabled: bool
    """Whether the agent is active."""

    model: str
    """Model ID (e.g., gpt-4o-mini, claude-3-5-sonnet)."""

    name: str

    provider: AgentProvider
    """LLM provider for the AI agent."""

    sender_id: str = FieldInfo(alias="senderId")

    system_prompt: str = FieldInfo(alias="systemPrompt")
    """System prompt for the agent."""

    updated_at: datetime = FieldInfo(alias="updatedAt")

    context_window_messages: Optional[int] = FieldInfo(alias="contextWindowMessages", default=None)
    """Number of previous messages to include as context."""

    include_contact_metadata: Optional[bool] = FieldInfo(alias="includeContactMetadata", default=None)
    """Whether to include contact metadata in context."""

    max_tokens: Optional[int] = FieldInfo(alias="maxTokens", default=None)
    """Maximum tokens for LLM response."""

    sender_ids: Optional[List[str]] = FieldInfo(alias="senderIds", default=None)
    """Senders this agent answers on.

    An agent can serve several; `senderId` remains the primary one, for
    compatibility.
    """

    stats: Optional[Stats] = None

    temperature: Optional[float] = None
    """LLM temperature (0-2)."""

    trigger_on_channels: Optional[List[str]] = FieldInfo(alias="triggerOnChannels", default=None)
    """Channels that trigger the agent."""

    trigger_on_message_types: Optional[List[str]] = FieldInfo(alias="triggerOnMessageTypes", default=None)
    """Message types that trigger the agent."""

    voice: Optional[Voice] = None
    """Voice Agent configuration.

    When present and enabled, the agent can answer inbound phone calls and place
    outbound calls with Zavu's managed voice pipeline. Requires the Voice Agents
    feature to be enabled for your team.
    """
