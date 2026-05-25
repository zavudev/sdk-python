# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SecretListResponse", "Secret"]


class Secret(BaseModel):
    id: str

    key: str

    value_last4: str = FieldInfo(alias="valueLast4")

    created_at: Optional[float] = FieldInfo(alias="createdAt", default=None)

    synced_to_aws: Optional[bool] = FieldInfo(alias="syncedToAws", default=None)

    updated_at: Optional[float] = FieldInfo(alias="updatedAt", default=None)


class SecretListResponse(BaseModel):
    secrets: List[Secret]
