# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["InvitationListParams"]


class InvitationListParams(TypedDict, total=False):
    cursor: str

    limit: int

    status: Literal["pending", "in_progress", "completed", "expired", "cancelled", "failed"]
    """Current status of the partner invitation.

    `failed` means the client started the connection and it did not finish (they
    cancelled Meta's dialog, denied a permission, or abandoned the tab). A failed
    invitation is still usable: the same link can be retried, and it moves back to
    `in_progress` when the client tries again.
    """
