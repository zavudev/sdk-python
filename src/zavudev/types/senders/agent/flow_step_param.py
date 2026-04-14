# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["FlowStepParam"]


class FlowStepParam(TypedDict, total=False):
    id: Required[str]
    """Unique step identifier."""

    config: Required[Dict[str, object]]
    """Step configuration (varies by type)."""

    type: Required[Literal["message", "collect", "condition", "tool", "llm", "transfer"]]
    """Type of flow step."""

    next_step_id: Annotated[Optional[str], PropertyInfo(alias="nextStepId")]
    """ID of the next step to execute."""
