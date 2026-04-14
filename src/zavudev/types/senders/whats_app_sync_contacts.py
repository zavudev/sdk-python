# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["WhatsAppSyncContacts"]


class WhatsAppSyncContacts(BaseModel):
    """Contacts sync status details."""

    can_sync: bool = FieldInfo(alias="canSync")
    """Whether contacts sync can be initiated."""

    status: Literal["not_requested", "pending", "syncing", "completed"]
    """Status of WhatsApp contacts sync."""

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
    """When the sync was last requested."""
