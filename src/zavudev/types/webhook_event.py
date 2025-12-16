# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["WebhookEvent"]

WebhookEvent: TypeAlias = Literal[
    "message.queued",
    "message.sent",
    "message.delivered",
    "message.failed",
    "message.inbound",
    "message.unsupported",
    "conversation.new",
    "template.status_changed",
]
