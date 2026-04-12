# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["FlowTrigger"]


class FlowTrigger(BaseModel):
    type: Literal["keyword", "intent", "always", "manual"]
    """Type of trigger for a flow."""

    intent: Optional[str] = None
    """Intent that triggers the flow (for intent type)."""

    keywords: Optional[List[str]] = None
    """Keywords that trigger the flow (for keyword type)."""
