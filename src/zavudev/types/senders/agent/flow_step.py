# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["FlowStep"]


class FlowStep(BaseModel):
    id: str
    """Unique step identifier."""

    config: Dict[str, object]
    """Step configuration (varies by type)."""

    type: Literal["message", "collect", "condition", "tool", "llm", "transfer"]
    """Type of flow step."""

    next_step_id: Optional[str] = FieldInfo(alias="nextStepId", default=None)
    """ID of the next step to execute."""
