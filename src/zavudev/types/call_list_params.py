# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CallListParams"]


class CallListParams(TypedDict, total=False):
    cursor: str

    direction: Literal["inbound", "outbound"]
    """
    Whether the call was placed by Zavu (outbound) or received from a caller
    (inbound).
    """

    limit: int

    status: Literal["queued", "ringing", "in_progress", "completed", "failed", "busy", "no_answer", "canceled"]
    """Lifecycle status of a voice call.

    - `queued`: outbound call created, not yet dialing.
    - `ringing`: dialing (outbound) or received and ringing (inbound).
    - `in_progress`: answered, the agent is connected.
    - `completed`: ended after a conversation.
    - `failed`: could not be completed.
    - `busy`: the line was busy.
    - `no_answer`: rang but was not answered.
    - `canceled`: canceled before it was answered.
    """
