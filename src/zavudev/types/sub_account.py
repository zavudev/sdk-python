# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SubAccount"]


class SubAccount(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    name: str

    status: Literal["active", "inactive"]

    total_spent: int = FieldInfo(alias="totalSpent")
    """Total amount spent by this sub-account in cents."""

    api_key: Optional[str] = FieldInfo(alias="apiKey", default=None)
    """API key for the sub-account. Only returned on creation."""

    credit_limit: Optional[int] = FieldInfo(alias="creditLimit", default=None)
    """Spending cap in cents.

    When reached, messages from this sub-account will be blocked.
    """

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """External reference ID set by the parent account."""

    metadata: Optional[Dict[str, object]] = None
