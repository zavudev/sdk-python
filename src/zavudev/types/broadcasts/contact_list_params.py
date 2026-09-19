# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..broadcast_contact_status import BroadcastContactStatus

__all__ = ["ContactListParams"]


class ContactListParams(TypedDict, total=False):
    cursor: str

    limit: int

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
