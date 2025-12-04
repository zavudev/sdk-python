# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Sender"]


class Sender(BaseModel):
    id: str

    name: str

    phone_number: str = FieldInfo(alias="phoneNumber")
    """Phone number in E.164 format."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    is_default: Optional[bool] = FieldInfo(alias="isDefault", default=None)
    """Whether this sender is the project's default."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
