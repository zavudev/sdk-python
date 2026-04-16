# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["WhatsAppSyncHistory"]


class WhatsAppSyncHistory(BaseModel):
    """History sync status details."""

    can_sync: bool = FieldInfo(alias="canSync")
    """Whether history sync can be initiated."""

    status: Literal["not_requested", "pending", "syncing", "completed", "rejected"]
    """Status of WhatsApp message history sync."""

    completed_at: Optional[datetime] = FieldInfo(alias="completedAt", default=None)
    """When the sync was completed."""

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
    """When the sync was last requested."""
