# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .broadcast_status import BroadcastStatus

__all__ = ["BroadcastListParams"]


class BroadcastListParams(TypedDict, total=False):
    cursor: str

    limit: int

    status: BroadcastStatus
    """Current status of the broadcast."""
