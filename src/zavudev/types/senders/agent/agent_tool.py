# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["AgentTool", "Parameters", "ParametersProperties"]


class ParametersProperties(BaseModel):
    description: Optional[str] = None

    type: Optional[str] = None


class Parameters(BaseModel):
    properties: Dict[str, ParametersProperties]

    required: List[str]

    type: Literal["object"]


class AgentTool(BaseModel):
    id: str

    agent_id: str = FieldInfo(alias="agentId")

    created_at: datetime = FieldInfo(alias="createdAt")

    description: str
    """Description for the LLM to understand when to use this tool."""

    enabled: bool

    name: str

    parameters: Parameters

    updated_at: datetime = FieldInfo(alias="updatedAt")

    webhook_url: str = FieldInfo(alias="webhookUrl")
    """HTTPS URL to call when the tool is executed."""
