# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TemplateSyncParams"]


class TemplateSyncParams(TypedDict, total=False):
    sender_id: Annotated[str, PropertyInfo(alias="senderId")]
    """Sync only the WhatsApp Business Account attached to this sender.

    If omitted, every WhatsApp sender in the project is synced.
    """
