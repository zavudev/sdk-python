# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .agent_execution_status import AgentExecutionStatus

__all__ = ["AgentExecution"]


class AgentExecution(BaseModel):
    id: str

    agent_id: str = FieldInfo(alias="agentId")

    cost: float
    """Cost in USD."""

    created_at: datetime = FieldInfo(alias="createdAt")

    input_tokens: int = FieldInfo(alias="inputTokens")

    latency_ms: int = FieldInfo(alias="latencyMs")

    output_tokens: int = FieldInfo(alias="outputTokens")

    status: AgentExecutionStatus
    """Status of an agent execution."""

    error_message: Optional[str] = FieldInfo(alias="errorMessage", default=None)

    inbound_message_id: Optional[str] = FieldInfo(alias="inboundMessageId", default=None)

    response_message_id: Optional[str] = FieldInfo(alias="responseMessageId", default=None)

    response_text: Optional[str] = FieldInfo(alias="responseText", default=None)
