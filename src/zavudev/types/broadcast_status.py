# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["BroadcastStatus"]

BroadcastStatus: TypeAlias = Literal[
    "draft",
    "pending_review",
    "approved",
    "rejected",
    "escalated",
    "rejected_final",
    "scheduled",
    "sending",
    "paused",
    "completed",
    "cancelled",
    "failed",
]
