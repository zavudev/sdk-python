# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TelegramConnectParams"]


class TelegramConnectParams(TypedDict, total=False):
    bot_token: Required[Annotated[str, PropertyInfo(alias="botToken")]]
    """Bot token from @BotFather."""
