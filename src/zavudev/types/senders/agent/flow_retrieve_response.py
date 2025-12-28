# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel
from .agent_flow import AgentFlow

__all__ = ["FlowRetrieveResponse"]


class FlowRetrieveResponse(BaseModel):
    flow: AgentFlow
