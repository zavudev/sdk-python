# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ChannelUpdateParams"]


class ChannelUpdateParams(TypedDict, total=False):
    contact_id: Required[Annotated[str, PropertyInfo(alias="contactId")]]

    label: Optional[str]
    """Optional label for the channel. Set to null to clear."""

    metadata: Dict[str, str]

    verified: bool
    """Whether the channel is verified."""
