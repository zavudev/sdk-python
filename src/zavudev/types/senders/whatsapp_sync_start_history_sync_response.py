# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .whats_app_sync_status import WhatsAppSyncStatus

__all__ = ["WhatsappSyncStartHistorySyncResponse"]


class WhatsappSyncStartHistorySyncResponse(BaseModel):
    message: str
    """Success message."""

    sync: WhatsAppSyncStatus
    """WhatsApp coexistence sync status."""
