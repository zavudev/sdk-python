# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel
from .agent_tool import AgentTool

__all__ = ["ToolUpdateResponse"]


class ToolUpdateResponse(BaseModel):
    tool: AgentTool
