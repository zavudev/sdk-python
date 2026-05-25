# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel
from ..agent_execution import AgentExecution

__all__ = ["ExecutionRetrieveResponse"]


class ExecutionRetrieveResponse(BaseModel):
    execution: AgentExecution
