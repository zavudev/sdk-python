# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .agent.agent import Agent

__all__ = ["AgentResponse"]


class AgentResponse(BaseModel):
    agent: Agent
    """AI Agent configuration for a sender."""
