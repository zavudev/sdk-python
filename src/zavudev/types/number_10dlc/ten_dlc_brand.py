# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TenDlcBrand"]


class TenDlcBrand(BaseModel):
    id: str

    city: str

    country: str
    """Two-letter ISO country code."""

    created_at: datetime = FieldInfo(alias="createdAt")

    display_name: str = FieldInfo(alias="displayName")
    """Display name of the brand."""

    email: str

    entity_type: Literal["PRIVATE_PROFIT", "PUBLIC_PROFIT", "NON_PROFIT", "GOVERNMENT", "SOLE_PROPRIETOR"] = FieldInfo(
        alias="entityType"
    )
    """Business entity type for 10DLC brand registration."""

    phone: str
    """Contact phone number in E.164 format."""

    postal_code: str = FieldInfo(alias="postalCode")

    state: str

    status: Literal["draft", "pending", "verified", "rejected"]
    """Status of a 10DLC brand registration."""

    street: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    vertical: str
    """Industry vertical."""

    brand_relationship: Optional[str] = FieldInfo(alias="brandRelationship", default=None)

    brand_score: Optional[int] = FieldInfo(alias="brandScore", default=None)
    """Trust score assigned by TCR after vetting."""

    company_name: Optional[str] = FieldInfo(alias="companyName", default=None)
    """Legal company name."""

    ein: Optional[str] = None
    """Employer Identification Number (EIN)."""

    failure_reason: Optional[str] = FieldInfo(alias="failureReason", default=None)
    """Reason for rejection, if applicable."""

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)

    stock_exchange: Optional[str] = FieldInfo(alias="stockExchange", default=None)

    stock_symbol: Optional[str] = FieldInfo(alias="stockSymbol", default=None)

    submitted_at: Optional[datetime] = FieldInfo(alias="submittedAt", default=None)

    verified_at: Optional[datetime] = FieldInfo(alias="verifiedAt", default=None)

    website: Optional[str] = None
