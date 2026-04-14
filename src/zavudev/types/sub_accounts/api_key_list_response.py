# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["APIKeyListResponse", "Item"]


class Item(BaseModel):
    id: str

    created_at: float = FieldInfo(alias="createdAt")

    environment: Literal["live", "test"]

    key_prefix: str = FieldInfo(alias="keyPrefix")
    """First characters of the key for identification."""

    name: str

    key: Optional[str] = None
    """Full API key. Only returned on creation."""

    last_used_at: Optional[float] = FieldInfo(alias="lastUsedAt", default=None)

    permissions: Optional[List[str]] = None

    revoked_at: Optional[float] = FieldInfo(alias="revokedAt", default=None)


class APIKeyListResponse(BaseModel):
    items: List[Item]
