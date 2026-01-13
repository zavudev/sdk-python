# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["MessageStatus"]

MessageStatus: TypeAlias = Literal["queued", "sending", "delivered", "failed", "received", "pending_url_verification"]
