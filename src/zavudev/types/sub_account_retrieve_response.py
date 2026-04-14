# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .sub_account import SubAccount

__all__ = ["SubAccountRetrieveResponse"]


class SubAccountRetrieveResponse(BaseModel):
    sub_account: SubAccount = FieldInfo(alias="subAccount")
