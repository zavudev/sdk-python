# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["FlowTriggerParam"]


class FlowTriggerParam(TypedDict, total=False):
    type: Required[Literal["keyword", "intent", "always", "manual"]]
    """Type of trigger for a flow."""

    intent: str
    """Intent that triggers the flow (for intent type)."""

    keywords: SequenceNotStr[str]
    """Keywords that trigger the flow (for keyword type)."""
