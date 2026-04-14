# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ExportCreateParams"]


class ExportCreateParams(TypedDict, total=False):
    data_types: Required[
        Annotated[
            List[Literal["messages", "conversations", "webhookDeliveries", "agentExecutions", "activities"]],
            PropertyInfo(alias="dataTypes"),
        ]
    ]
    """List of data types to include in the export."""

    date_from: Annotated[Union[str, datetime], PropertyInfo(alias="dateFrom", format="iso8601")]
    """Start date for data to export (inclusive)."""

    date_to: Annotated[Union[str, datetime], PropertyInfo(alias="dateTo", format="iso8601")]
    """End date for data to export (inclusive)."""
