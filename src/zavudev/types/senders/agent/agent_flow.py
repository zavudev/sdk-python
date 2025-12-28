# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["AgentFlow", "Step", "Trigger"]


class Step(BaseModel):
    id: str
    """Unique step identifier."""

    config: Dict[str, object]
    """Step configuration (varies by type)."""

    type: Literal["message", "collect", "condition", "tool", "llm", "transfer"]
    """Type of flow step."""

    next_step_id: Optional[str] = FieldInfo(alias="nextStepId", default=None)
    """ID of the next step to execute."""


class Trigger(BaseModel):
    type: Literal["keyword", "intent", "always", "manual"]
    """Type of trigger for a flow."""

    intent: Optional[str] = None
    """Intent that triggers the flow (for intent type)."""

    keywords: Optional[List[str]] = None
    """Keywords that trigger the flow (for keyword type)."""


class AgentFlow(BaseModel):
    id: str

    agent_id: str = FieldInfo(alias="agentId")

    created_at: datetime = FieldInfo(alias="createdAt")

    enabled: bool

    name: str

    priority: int
    """Priority when multiple flows match (higher = more priority)."""

    steps: List[Step]

    trigger: Trigger

    updated_at: datetime = FieldInfo(alias="updatedAt")

    description: Optional[str] = None
