# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .agent_provider import AgentProvider

__all__ = ["AgentUpdateParams", "Voice"]


class AgentUpdateParams(TypedDict, total=False):
    api_key: Annotated[str, PropertyInfo(alias="apiKey")]

    context_window_messages: Annotated[int, PropertyInfo(alias="contextWindowMessages")]

    enabled: bool

    include_contact_metadata: Annotated[bool, PropertyInfo(alias="includeContactMetadata")]

    max_tokens: Annotated[Optional[int], PropertyInfo(alias="maxTokens")]

    model: str

    name: str

    provider: AgentProvider
    """LLM provider for the AI agent."""

    system_prompt: Annotated[str, PropertyInfo(alias="systemPrompt")]

    temperature: Optional[float]

    trigger_on_channels: Annotated[SequenceNotStr[str], PropertyInfo(alias="triggerOnChannels")]

    trigger_on_message_types: Annotated[SequenceNotStr[str], PropertyInfo(alias="triggerOnMessageTypes")]

    voice: Voice
    """Voice Agent configuration.

    Patch this object to enable voice, change the greeting, or adjust call limits.
    Requires the Voice Agents feature to be enabled for your team.
    """


class Voice(TypedDict, total=False):
    """Voice Agent configuration.

    Patch this object to enable voice, change the greeting, or adjust call limits. Requires the Voice Agents feature to be enabled for your team.
    """

    enabled: Required[bool]
    """Whether the agent handles voice calls.

    When false, the sender's number is not answered by the voice agent and outbound
    calls are rejected.
    """

    greeting: str
    """Opening line the agent speaks when the call connects.

    If omitted, the agent waits for the caller to speak first.
    """

    greetings: Dict[str, str]
    """Greeting per language, keyed by language code.

    Used when the caller's language differs from the one `greeting` is written in.
    """

    interruptible: bool
    """Whether the caller can interrupt the agent while it is speaking (barge-in).

    When true, the agent stops talking as soon as the caller starts.
    """

    language: str
    """BCP-47 language code used for both speech recognition and speech synthesis (e.g.

    `en`, `es`, `pt-BR`). Auto-detected from the recipient when omitted.
    """

    max_call_duration_minutes: Annotated[int, PropertyInfo(alias="maxCallDurationMinutes")]
    """Hard limit on call length in minutes. The call ends automatically when reached."""

    max_idle_seconds: Annotated[int, PropertyInfo(alias="maxIdleSeconds")]
    """How long the agent waits during silence before ending the call."""

    model: str
    """
    Model that runs the conversation, co-located in the voice network for lowest
    latency. Independent of the model used for text messaging. Derived from the
    agent's text model when omitted.
    """

    record_calls: Annotated[bool, PropertyInfo(alias="recordCalls")]
    """Whether the call audio is recorded."""

    stt_model: Annotated[str, PropertyInfo(alias="sttModel")]
    """Speech-recognition model. Uses the default when omitted."""

    stt_provider: Annotated[str, PropertyInfo(alias="sttProvider")]
    """Speech-recognition provider. Uses the default when omitted."""

    transfer_phone_number: Annotated[str, PropertyInfo(alias="transferPhoneNumber")]
    """E.164 phone number the agent can transfer the call to.

    When set, the agent is given a transfer tool it can use to hand the call to a
    human.
    """

    tts_provider: Annotated[str, PropertyInfo(alias="ttsProvider")]
    """Speech-synthesis provider. Uses the default when omitted."""

    tts_voice_id: Annotated[str, PropertyInfo(alias="ttsVoiceId")]
    """Identifier of the synthesized voice that speaks.

    Choose from the voices available in the dashboard. Uses a neutral default when
    omitted.
    """

    voicemail_action: Annotated[Literal["hangup", "leave_message"], PropertyInfo(alias="voicemailAction")]
    """
    What the agent does when an answering machine or voicemail is detected on an
    outbound call.
    """

    voicemail_message: Annotated[str, PropertyInfo(alias="voicemailMessage")]
    """Message spoken when `voicemailAction` is `leave_message`.

    Falls back to `greeting` when omitted.
    """

    voice_speed: Annotated[float, PropertyInfo(alias="voiceSpeed")]
    """Speech rate.

    1.0 is natural. Only honoured by voices that support rate control; ignored by
    the others.
    """
