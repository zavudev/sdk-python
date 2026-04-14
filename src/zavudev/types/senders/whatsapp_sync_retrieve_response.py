# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .whats_app_sync_status import WhatsAppSyncStatus

__all__ = ["WhatsappSyncRetrieveResponse"]


class WhatsappSyncRetrieveResponse(BaseModel):
    sync: WhatsAppSyncStatus
    """WhatsApp coexistence sync status."""
