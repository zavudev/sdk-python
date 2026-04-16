# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["TenDlcPhoneNumberAssignment"]


class TenDlcPhoneNumberAssignment(BaseModel):
    id: str

    campaign_id: str = FieldInfo(alias="campaignId")

    created_at: datetime = FieldInfo(alias="createdAt")

    phone_number_id: str = FieldInfo(alias="phoneNumberId")

    status: Literal["pending", "active", "failed"]
    """Assignment status."""

    updated_at: datetime = FieldInfo(alias="updatedAt")

    assigned_at: Optional[datetime] = FieldInfo(alias="assignedAt", default=None)

    failure_reason: Optional[str] = FieldInfo(alias="failureReason", default=None)
