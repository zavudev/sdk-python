# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ToolTestParams"]


class ToolTestParams(TypedDict, total=False):
    sender_id: Required[Annotated[str, PropertyInfo(alias="senderId")]]

    test_params: Required[Annotated[Dict[str, object], PropertyInfo(alias="testParams")]]
    """Parameters to pass to the tool for testing."""
