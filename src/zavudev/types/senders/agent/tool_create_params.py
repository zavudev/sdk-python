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
    """Signing secret for the webhook.

    Optional: Zavu generates one when omitted and returns it on this response only.
    Supply your own if you already have a secret you want reused.
    """
