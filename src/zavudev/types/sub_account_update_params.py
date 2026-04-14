# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SubAccountUpdateParams"]


class SubAccountUpdateParams(TypedDict, total=False):
    credit_limit: Annotated[Optional[int], PropertyInfo(alias="creditLimit")]

    external_id: Annotated[str, PropertyInfo(alias="externalId")]

    metadata: Dict[str, object]

    name: str

    status: Literal["active", "inactive"]
