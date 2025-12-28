# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .agent_provider import AgentProvider

__all__ = ["AgentCreateParams"]


class AgentCreateParams(TypedDict, total=False):
    model: Required[str]

    name: Required[str]

    provider: Required[AgentProvider]
    """LLM provider for the AI agent."""

    system_prompt: Required[Annotated[str, PropertyInfo(alias="systemPrompt")]]

    api_key: Annotated[str, PropertyInfo(alias="apiKey")]
    """API key for the LLM provider. Required unless provider is 'zavu'."""

    context_window_messages: Annotated[int, PropertyInfo(alias="contextWindowMessages")]

    include_contact_metadata: Annotated[bool, PropertyInfo(alias="includeContactMetadata")]

    max_tokens: Annotated[int, PropertyInfo(alias="maxTokens")]

    temperature: float

    trigger_on_channels: Annotated[SequenceNotStr[str], PropertyInfo(alias="triggerOnChannels")]

    trigger_on_message_types: Annotated[SequenceNotStr[str], PropertyInfo(alias="triggerOnMessageTypes")]
