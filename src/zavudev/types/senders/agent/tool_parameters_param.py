# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["ToolParametersParam", "Properties"]


class Properties(TypedDict, total=False):
    description: str

    type: str


class ToolParametersParam(TypedDict, total=False):
    properties: Required[Dict[str, Properties]]

    required: Required[SequenceNotStr[str]]

    type: Required[Literal["object"]]
