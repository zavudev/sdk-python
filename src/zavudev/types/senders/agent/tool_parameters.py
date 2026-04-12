# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ToolParameters", "Properties"]


class Properties(BaseModel):
    description: Optional[str] = None

    type: Optional[str] = None


class ToolParameters(BaseModel):
    properties: Dict[str, Properties]

    required: List[str]

    type: Literal["object"]
