# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["VerifiedURL"]


class VerifiedURL(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    domain: str
    """Domain extracted from the URL."""

    status: Literal["pending", "approved", "rejected", "malicious"]
    """Status of a verified URL."""

    url: str
    """The verified URL."""

    approval_type: Optional[Literal["manual", "auto_web_risk"]] = FieldInfo(alias="approvalType", default=None)
    """How the URL was approved or rejected."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
