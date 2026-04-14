# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from .tool_parameters_param import ToolParametersParam

__all__ = ["ToolUpdateParams"]


class ToolUpdateParams(TypedDict, total=False):
    sender_id: Required[Annotated[str, PropertyInfo(alias="senderId")]]

    description: str

    enabled: bool

    name: str

    parameters: ToolParametersParam

    webhook_secret: Annotated[Optional[str], PropertyInfo(alias="webhookSecret")]

    webhook_url: Annotated[str, PropertyInfo(alias="webhookUrl")]
