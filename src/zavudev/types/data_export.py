# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DataExport"]


class DataExport(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    data_types: List[Literal["messages", "conversations", "webhookDeliveries", "agentExecutions", "activities"]] = (
        FieldInfo(alias="dataTypes")
    )

    expires_at: datetime = FieldInfo(alias="expiresAt")
    """When the export download link expires (24 hours after creation)."""

    status: Literal["pending", "processing", "completed", "failed"]
    """Status of a data export job."""

    completed_at: Optional[datetime] = FieldInfo(alias="completedAt", default=None)

    date_from: Optional[datetime] = FieldInfo(alias="dateFrom", default=None)

    date_to: Optional[datetime] = FieldInfo(alias="dateTo", default=None)

    download_url: Optional[str] = FieldInfo(alias="downloadUrl", default=None)
    """URL to download the export file. Only available when status is 'completed'."""

    error_message: Optional[str] = FieldInfo(alias="errorMessage", default=None)
    """Error message if the export failed."""

    file_size: Optional[int] = FieldInfo(alias="fileSize", default=None)
    """Size of the export file in bytes."""
