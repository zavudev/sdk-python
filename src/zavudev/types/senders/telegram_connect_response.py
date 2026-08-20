# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TelegramConnectResponse", "Telegram"]


class Telegram(BaseModel):
    connected: bool

    bot_id: Optional[str] = FieldInfo(alias="botId", default=None)

    bot_username: Optional[str] = FieldInfo(alias="botUsername", default=None)


class TelegramConnectResponse(BaseModel):
    telegram: Telegram
