# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from .tool_parameters_param import ToolParametersParam

__all__ = ["ToolCreateParams"]


class ToolCreateParams(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    parameters: Required[ToolParametersParam]

    webhook_url: Required[Annotated[str, PropertyInfo(alias="webhookUrl")]]
    """Must be HTTPS."""

    enabled: bool

    webhook_secret: Annotated[str, PropertyInfo(alias="webhookSecret")]
    """Optional secret for webhook signature verification."""
