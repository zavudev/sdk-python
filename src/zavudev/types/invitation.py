# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Invitation"]


class Invitation(BaseModel):
    id: str

    token: str
    """Unique invitation token."""

    created_at: datetime = FieldInfo(alias="createdAt")

    expires_at: datetime = FieldInfo(alias="expiresAt")

    status: Literal["pending", "in_progress", "completed", "expired", "cancelled"]
    """Current status of the partner invitation."""

    updated_at: datetime = FieldInfo(alias="updatedAt")

    url: str
    """Full URL to share with the client."""

    client_email: Optional[str] = FieldInfo(alias="clientEmail", default=None)

    client_name: Optional[str] = FieldInfo(alias="clientName", default=None)

    client_phone: Optional[str] = FieldInfo(alias="clientPhone", default=None)

    completed_at: Optional[datetime] = FieldInfo(alias="completedAt", default=None)

    phone_number_id: Optional[str] = FieldInfo(alias="phoneNumberId", default=None)
    """ID of a pre-assigned Zavu phone number for WhatsApp registration."""

    sender_id: Optional[str] = FieldInfo(alias="senderId", default=None)
    """ID of the sender created when invitation is completed."""

    started_at: Optional[datetime] = FieldInfo(alias="startedAt", default=None)

    viewed_at: Optional[datetime] = FieldInfo(alias="viewedAt", default=None)
