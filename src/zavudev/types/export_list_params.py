# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ExportListParams"]


class ExportListParams(TypedDict, total=False):
    cursor: str

    limit: int

    status: Literal["pending", "processing", "completed", "failed"]
    """Status of a data export job."""
