# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Invitation", "ConnectedAccount"]


class ConnectedAccount(BaseModel):
    """The account the client linked, populated once the invitation is `completed`.

    Null before that. Use it to show the partner what was connected without fetching the sender.
    """

    id: str
    """
    Provider-side identifier: the WhatsApp phone number ID, or the Facebook Page ID.
    """

    channel: Literal["whatsapp", "messenger"]

    name: Optional[str] = None
    """
    Display name of the connected account: the WhatsApp verified name, or the
    Facebook Page name.
    """


class Invitation(BaseModel):
    id: str

    token: str
    """Unique invitation token."""

    created_at: datetime = FieldInfo(alias="createdAt")

    expires_at: datetime = FieldInfo(alias="expiresAt")

    status: Literal["pending", "in_progress", "completed", "expired", "cancelled", "failed"]
    """Current status of the partner invitation.

    `failed` means the client started the connection and it did not finish (they
    cancelled Meta's dialog, denied a permission, or abandoned the tab). A failed
    invitation is still usable: the same link can be retried, and it moves back to
    `in_progress` when the client tries again.
    """

    updated_at: datetime = FieldInfo(alias="updatedAt")

    url: str
    """Full URL to share with the client."""

    client_email: Optional[str] = FieldInfo(alias="clientEmail", default=None)

    client_name: Optional[str] = FieldInfo(alias="clientName", default=None)

    client_phone: Optional[str] = FieldInfo(alias="clientPhone", default=None)

    completed_at: Optional[datetime] = FieldInfo(alias="completedAt", default=None)

    connected_account: Optional[ConnectedAccount] = FieldInfo(alias="connectedAccount", default=None)
    """The account the client linked, populated once the invitation is `completed`.

    Null before that. Use it to show the partner what was connected without fetching
    the sender.
    """

    connection_type: Optional[Literal["whatsapp_waba", "messenger"]] = FieldInfo(alias="connectionType", default=None)
    """
    Which Meta channel the client connects: `whatsapp_waba` (official WhatsApp Cloud
    API via embedded signup) or `messenger` (a Facebook Page's Messenger inbox,
    including Marketplace chats).
    """

    failed_at: Optional[datetime] = FieldInfo(alias="failedAt", default=None)

    failure_reason: Optional[str] = FieldInfo(alias="failureReason", default=None)
    """Stable code for why the last attempt failed, present when `status` is `failed`.

    Values include `fb_cancelled` (client closed Meta's dialog), `fb_not_authorized`
    (permission denied), `signup_abandoned` (started but never finished),
    `meta_no_pages` (the client administers no Facebook Page), and `internal_error`.
    Treat unknown codes as a generic failure.
    """

    phone_number_id: Optional[str] = FieldInfo(alias="phoneNumberId", default=None)
    """ID of a pre-assigned Zavu phone number for WhatsApp registration.

    Always null for `messenger` invitations.
    """

    sender_id: Optional[str] = FieldInfo(alias="senderId", default=None)
    """ID of the sender created when invitation is completed."""

    started_at: Optional[datetime] = FieldInfo(alias="startedAt", default=None)

    viewed_at: Optional[datetime] = FieldInfo(alias="viewedAt", default=None)
