# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["InvitationListParams"]


class InvitationListParams(TypedDict, total=False):
    cursor: str

    limit: int

    status: Literal["pending", "in_progress", "completed", "expired", "cancelled"]
    """Current status of the partner invitation."""
