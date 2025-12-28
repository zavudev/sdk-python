# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RegulatoryDocument"]


class RegulatoryDocument(BaseModel):
    """A regulatory document for phone number requirements."""

    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    document_type: Literal[
        "passport",
        "national_id",
        "drivers_license",
        "utility_bill",
        "tax_id",
        "business_registration",
        "proof_of_address",
        "other",
    ] = FieldInfo(alias="documentType")

    name: str

    status: Literal["pending", "uploaded", "verified", "rejected"]

    file_size: Optional[int] = FieldInfo(alias="fileSize", default=None)

    mime_type: Optional[str] = FieldInfo(alias="mimeType", default=None)

    rejection_reason: Optional[str] = FieldInfo(alias="rejectionReason", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
