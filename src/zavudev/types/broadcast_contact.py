# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .broadcast_contact_status import BroadcastContactStatus

__all__ = ["BroadcastContact"]


class BroadcastContact(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    recipient: str

    recipient_type: Literal["phone", "email"] = FieldInfo(alias="recipientType")

    status: BroadcastContactStatus
    """Status of a contact within a broadcast.

    - `pending`, `queued`, `sending`: not handed to the provider yet.
    - `sent`: accepted by the provider; delivery is not confirmed yet. Channels that
      never report delivery leave the recipient here.
    - `delivered`: the channel confirmed delivery to the device. A WhatsApp read
      receipt also counts as delivered.
    - `failed`: not delivered. A recipient can move from `sent` or `delivered` to
      `failed` when the provider reports a failure late.
    - `skipped`: not sent, because the recipient opted out of the channel or the
      broadcast was cancelled before reaching it.
    """

    cost: Optional[float] = None

    error_code: Optional[str] = FieldInfo(alias="errorCode", default=None)

    error_message: Optional[str] = FieldInfo(alias="errorMessage", default=None)

    message_id: Optional[str] = FieldInfo(alias="messageId", default=None)
    """Associated message ID after processing."""

    processed_at: Optional[datetime] = FieldInfo(alias="processedAt", default=None)

    template_button_variables: Optional[Dict[str, str]] = FieldInfo(alias="templateButtonVariables", default=None)

    template_header_variables: Optional[Dict[str, str]] = FieldInfo(alias="templateHeaderVariables", default=None)

    template_variables: Optional[Dict[str, str]] = FieldInfo(alias="templateVariables", default=None)
