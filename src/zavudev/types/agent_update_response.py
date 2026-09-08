# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .senders.agent.agent import Agent

__all__ = ["AgentUpdateResponse"]


class AgentUpdateResponse(BaseModel):
    agent: Agent
    """AI Agent configuration for a sender."""
