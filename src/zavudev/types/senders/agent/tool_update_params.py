# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["ToolUpdateParams", "Parameters", "ParametersProperties"]


class ToolUpdateParams(TypedDict, total=False):
    sender_id: Required[Annotated[str, PropertyInfo(alias="senderId")]]

    description: str

    enabled: bool

    name: str

    parameters: Parameters

    webhook_secret: Annotated[Optional[str], PropertyInfo(alias="webhookSecret")]

    webhook_url: Annotated[str, PropertyInfo(alias="webhookUrl")]


class ParametersProperties(TypedDict, total=False):
    description: str

    type: str


class Parameters(TypedDict, total=False):
    properties: Required[Dict[str, ParametersProperties]]

    required: Required[SequenceNotStr[str]]

    type: Required[Literal["object"]]
