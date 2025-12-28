# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["AgentExecutionStatus"]

AgentExecutionStatus: TypeAlias = Literal["success", "error", "filtered", "rate_limited", "balance_insufficient"]
