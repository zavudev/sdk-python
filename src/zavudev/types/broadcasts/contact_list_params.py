# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..broadcast_contact_status import BroadcastContactStatus

__all__ = ["ContactListParams"]


class ContactListParams(TypedDict, total=False):
    cursor: str

    limit: int

    status: BroadcastContactStatus
    """Status of a contact within a broadcast."""
