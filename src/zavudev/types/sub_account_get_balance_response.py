# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SubAccountGetBalanceResponse"]


class SubAccountGetBalanceResponse(BaseModel):
    balance: int
    """Team balance in cents. All charges are billed to the parent team."""

    currency: str

    credit_limit: Optional[int] = FieldInfo(alias="creditLimit", default=None)
    """Spending cap in cents (only for sub-accounts)."""

    is_sub_account: Optional[bool] = FieldInfo(alias="isSubAccount", default=None)
    """Whether this API key belongs to a sub-account."""

    total_spent: Optional[int] = FieldInfo(alias="totalSpent", default=None)
    """Total amount spent by this sub-account in cents (only for sub-accounts)."""
