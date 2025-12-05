# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["BroadcastContactStatus"]

BroadcastContactStatus: TypeAlias = Literal["pending", "queued", "sending", "delivered", "failed", "skipped"]
