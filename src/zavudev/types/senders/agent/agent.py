# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ..agent_provider import AgentProvider

__all__ = ["Agent", "Stats"]


class Stats(BaseModel):
    total_cost: Optional[float] = FieldInfo(alias="totalCost", default=None)
    """Total cost in USD."""

    total_invocations: Optional[int] = FieldInfo(alias="totalInvocations", default=None)

    total_tokens_used: Optional[int] = FieldInfo(alias="totalTokensUsed", default=None)


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

    stats: Optional[Stats] = None

    temperature: Optional[float] = None
    """LLM temperature (0-2)."""

    trigger_on_channels: Optional[List[str]] = FieldInfo(alias="triggerOnChannels", default=None)
    """Channels that trigger the agent."""

    trigger_on_message_types: Optional[List[str]] = FieldInfo(alias="triggerOnMessageTypes", default=None)
    """Message types that trigger the agent."""
