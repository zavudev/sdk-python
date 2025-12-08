# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["OwnedPhoneNumberPricing"]


class OwnedPhoneNumberPricing(BaseModel):
    is_free_number: Optional[bool] = FieldInfo(alias="isFreeNumber", default=None)
    """Whether this is a free number."""

    monthly_cost: Optional[float] = FieldInfo(alias="monthlyCost", default=None)
    """Monthly cost in cents."""

    monthly_price: Optional[float] = FieldInfo(alias="monthlyPrice", default=None)
    """Monthly price in USD."""

    upfront_cost: Optional[float] = FieldInfo(alias="upfrontCost", default=None)
    """One-time purchase cost in cents."""
