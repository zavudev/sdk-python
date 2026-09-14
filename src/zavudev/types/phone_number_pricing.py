# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PhoneNumberPricing"]


class PhoneNumberPricing(BaseModel):
    is_free_eligible: Optional[bool] = FieldInfo(alias="isFreeEligible", default=None)
    """
    Whether this number qualifies as the plan-included number: a US or Canadian
    number (a +1 number) costing $20 a month or less. The benefit is one per
    account: it is never offered again once claimed, not even after the number is
    released.
    """

    monthly_price: Optional[float] = FieldInfo(alias="monthlyPrice", default=None)
    """Monthly price in USD."""

    upfront_price: Optional[float] = FieldInfo(alias="upfrontPrice", default=None)
    """One-time purchase price in USD."""
