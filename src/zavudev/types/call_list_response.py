# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CallListResponse", "Transcript"]


class Transcript(BaseModel):
    """A single turn in a voice call transcript."""

    role: Literal["user", "assistant", "tool"]
    """Who produced the turn.

    `tool` records a tool call the agent made during the conversation.
    """

    seq: int
    """Ordinal position of the turn within the call, starting at 0."""

    text: str
    """
    Transcribed speech for `user` and `assistant` turns, or a JSON summary of the
    tool call for `tool` turns.
    """

    ended_at: Optional[datetime] = FieldInfo(alias="endedAt", default=None)
    """When the turn ended."""

    started_at: Optional[datetime] = FieldInfo(alias="startedAt", default=None)
    """When the turn started."""


class CallListResponse(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    direction: Literal["inbound", "outbound"]
    """
    Whether the call was placed by Zavu (outbound) or received from a caller
    (inbound).
    """

    from_: str = FieldInfo(alias="from")
    """Caller phone number in E.164 format.

    Your sender's number for outbound calls; the caller's number for inbound calls.
    """

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

    to: str
    """Callee phone number in E.164 format."""

    answered_at: Optional[datetime] = FieldInfo(alias="answeredAt", default=None)
    """When the call was answered."""

    cost: Optional[float] = None
    """
    Total cost of the call in USD, combining the managed voice pipeline per-minute
    charge and telephony. Available once the call has ended.
    """

    duration_seconds: Optional[int] = FieldInfo(alias="durationSeconds", default=None)
    """Billable talk time in seconds, measured from answer to hangup."""

    ended_at: Optional[datetime] = FieldInfo(alias="endedAt", default=None)
    """When the call ended."""

    end_reason: Optional[str] = FieldInfo(alias="endReason", default=None)
    """Why the call ended (e.g.

    `agent_ended`, `max_duration`, `transfer`, `hangup`). Present once the call is
    no longer active.
    """

    metadata: Optional[Dict[str, str]] = None
    """Arbitrary metadata you attached when creating the call."""

    transcript: Optional[List[Transcript]] = None
    """Ordered transcript of the call.

    Included when retrieving a single call; omitted from list responses.
    """

    turn_count: Optional[int] = FieldInfo(alias="turnCount", default=None)
    """Number of conversation turns exchanged during the call."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
