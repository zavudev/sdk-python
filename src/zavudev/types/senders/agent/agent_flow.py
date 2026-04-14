# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .flow_step import FlowStep
from ...._models import BaseModel
from .flow_trigger import FlowTrigger

__all__ = ["AgentFlow"]


class AgentFlow(BaseModel):
    id: str

    agent_id: str = FieldInfo(alias="agentId")

    created_at: datetime = FieldInfo(alias="createdAt")

    enabled: bool

    name: str

    priority: int
    """Priority when multiple flows match (higher = more priority)."""

    steps: List[FlowStep]

    trigger: FlowTrigger

    updated_at: datetime = FieldInfo(alias="updatedAt")

    description: Optional[str] = None
