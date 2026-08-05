# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ToolTestResponse", "Run"]


class Run(BaseModel):
    """One run of a tool triggered from the test endpoint.

    Recorded so a test is verifiable after the fact rather than only visible in the response.
    """

    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    duration_ms: int = FieldInfo(alias="durationMs")

    success: bool
    """Whether the tool returned without error.

    A tool that answered with a non-2xx status is a failed run, not an error of this
    endpoint.
    """

    tool_id: str = FieldInfo(alias="toolId")

    error: Optional[str] = None
    """Why the run failed, when it did."""

    params: Optional[Dict[str, object]] = None
    """The parameters the tool was called with."""

    response: Optional[str] = None
    """The tool's response body, truncated."""

    status_code: Optional[int] = FieldInfo(alias="statusCode", default=None)
    """HTTP status the tool's webhook returned.

    Absent for tools that do not go over HTTP.
    """


class ToolTestResponse(BaseModel):
    run: Run
    """One run of a tool triggered from the test endpoint.

    Recorded so a test is verifiable after the fact rather than only visible in the
    response.
    """
