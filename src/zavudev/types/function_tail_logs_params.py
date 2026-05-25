# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FunctionTailLogsParams"]


class FunctionTailLogsParams(TypedDict, total=False):
    end_time: Annotated[int, PropertyInfo(alias="endTime")]
    """End of the log window in Unix epoch milliseconds."""

    filter_pattern: Annotated[str, PropertyInfo(alias="filterPattern")]

    limit: int

    next_token: Annotated[str, PropertyInfo(alias="nextToken")]

    start_time: Annotated[int, PropertyInfo(alias="startTime")]
    """Start of the log window in Unix epoch milliseconds."""
