# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["APIKeyCreateResponse", "APIKey"]


class APIKey(BaseModel):
    id: str

    environment: Literal["live", "test"]

    key: str

    name: str


class APIKeyCreateResponse(BaseModel):
    api_key: APIKey = FieldInfo(alias="apiKey")
