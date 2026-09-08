# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["AgentListVoicesResponse", "Item"]


class Item(BaseModel):
    id: str
    """Value for `voice.ttsVoiceId`."""

    language: str

    name: str


class AgentListVoicesResponse(BaseModel):
    items: List[Item]

    languages: List[str]
    """Languages an agent can be pinned to. `auto` follows the caller."""

    total: Optional[int] = None
    """Voices in the catalog, before filtering."""
