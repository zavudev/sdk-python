# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CampaignListParams"]


class CampaignListParams(TypedDict, total=False):
    brand_id: Annotated[str, PropertyInfo(alias="brandId")]
    """Filter campaigns by brand ID."""

    cursor: str

    limit: int
