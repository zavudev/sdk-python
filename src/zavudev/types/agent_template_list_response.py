# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AgentTemplateListResponse", "Item"]


class Item(BaseModel):
    """Compact catalog entry for a factory agent."""

    id: str

    category: Literal["sales", "support", "frontDesk", "ops"]

    name: str

    summary: str

    tool_count: int = FieldInfo(alias="toolCount")

    voice: bool
    """Whether this agent answers phone calls."""


class AgentTemplateListResponse(BaseModel):
    items: List[Item]
