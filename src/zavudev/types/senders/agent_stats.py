# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AgentStats"]


class AgentStats(BaseModel):
    error_count: int = FieldInfo(alias="errorCount")

    success_count: int = FieldInfo(alias="successCount")

    total_cost: float = FieldInfo(alias="totalCost")
    """Total cost in USD."""

    total_invocations: int = FieldInfo(alias="totalInvocations")

    total_tokens_used: int = FieldInfo(alias="totalTokensUsed")

    avg_latency_ms: Optional[float] = FieldInfo(alias="avgLatencyMs", default=None)
