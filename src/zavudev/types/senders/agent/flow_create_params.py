# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["FlowCreateParams", "Step", "Trigger"]


class FlowCreateParams(TypedDict, total=False):
    name: Required[str]

    steps: Required[Iterable[Step]]

    trigger: Required[Trigger]

    description: str

    enabled: bool

    priority: int


class Step(TypedDict, total=False):
    id: Required[str]
    """Unique step identifier."""

    config: Required[Dict[str, object]]
    """Step configuration (varies by type)."""

    type: Required[Literal["message", "collect", "condition", "tool", "llm", "transfer"]]
    """Type of flow step."""

    next_step_id: Annotated[Optional[str], PropertyInfo(alias="nextStepId")]
    """ID of the next step to execute."""


class Trigger(TypedDict, total=False):
    type: Required[Literal["keyword", "intent", "always", "manual"]]
    """Type of trigger for a flow."""

    intent: str
    """Intent that triggers the flow (for intent type)."""

    keywords: SequenceNotStr[str]
    """Keywords that trigger the flow (for keyword type)."""
