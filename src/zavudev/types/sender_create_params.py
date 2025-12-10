# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SenderCreateParams"]


class SenderCreateParams(TypedDict, total=False):
    name: Required[str]

    phone_number: Required[Annotated[str, PropertyInfo(alias="phoneNumber")]]

    set_as_default: Annotated[bool, PropertyInfo(alias="setAsDefault")]

    webhook_events: Annotated[
        List[Literal["message.sent", "message.delivered", "message.failed", "message.inbound", "conversation.new"]],
        PropertyInfo(alias="webhookEvents"),
    ]
    """Events to subscribe to."""

    webhook_url: Annotated[str, PropertyInfo(alias="webhookUrl")]
    """HTTPS URL for webhook events."""
