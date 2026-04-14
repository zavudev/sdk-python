# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SubAccountCreateParams"]


class SubAccountCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the sub-account."""

    credit_limit: Annotated[int, PropertyInfo(alias="creditLimit")]
    """Spending cap in cents.

    When reached, messages from this sub-account will be blocked. Omit or set to 0
    for no limit.
    """

    external_id: Annotated[str, PropertyInfo(alias="externalId")]
    """External reference ID for your own tracking."""

    metadata: Dict[str, object]
