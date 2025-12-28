# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["ToolCreateParams", "Parameters", "ParametersProperties"]


class ToolCreateParams(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    parameters: Required[Parameters]

    webhook_url: Required[Annotated[str, PropertyInfo(alias="webhookUrl")]]
    """Must be HTTPS."""

    enabled: bool

    webhook_secret: Annotated[str, PropertyInfo(alias="webhookSecret")]
    """Optional secret for webhook signature verification."""


class ParametersProperties(TypedDict, total=False):
    description: str

    type: str


class Parameters(TypedDict, total=False):
    properties: Required[Dict[str, ParametersProperties]]

    required: Required[SequenceNotStr[str]]

    type: Required[Literal["object"]]
