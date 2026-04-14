# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SubAccountDeactivateResponse"]


class SubAccountDeactivateResponse(BaseModel):
    keys_revoked: int = FieldInfo(alias="keysRevoked")
    """Number of API keys revoked."""

    message: str
