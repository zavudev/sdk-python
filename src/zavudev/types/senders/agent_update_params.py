# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .agent_provider import AgentProvider

__all__ = ["AgentUpdateParams"]


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
