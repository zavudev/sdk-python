# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .tool_parameters import ToolParameters

__all__ = ["AgentTool"]


class AgentTool(BaseModel):
    id: str

    agent_id: str = FieldInfo(alias="agentId")

    created_at: datetime = FieldInfo(alias="createdAt")

    description: str
    """Description for the LLM to understand when to use this tool."""

    enabled: bool

    name: str

    parameters: ToolParameters

    updated_at: datetime = FieldInfo(alias="updatedAt")

    webhook_url: str = FieldInfo(alias="webhookUrl")
    """HTTPS URL to call when the tool is executed."""
