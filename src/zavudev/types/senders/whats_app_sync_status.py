# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .whats_app_sync_history import WhatsAppSyncHistory
from .whats_app_sync_contacts import WhatsAppSyncContacts

__all__ = ["WhatsAppSyncStatus"]


class WhatsAppSyncStatus(BaseModel):
    """WhatsApp coexistence sync status."""

    contacts: WhatsAppSyncContacts
    """Contacts sync status details."""

    history: WhatsAppSyncHistory
    """History sync status details."""

    is_coexistence: bool = FieldInfo(alias="isCoexistence")
    """Whether the account is in coexistence mode."""

    status: Literal["pending_verification", "pending_registration", "active", "disconnected", "error"]
    """WhatsApp account status."""
