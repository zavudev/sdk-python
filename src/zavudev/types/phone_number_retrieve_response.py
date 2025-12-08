# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .owned_phone_number import OwnedPhoneNumber

__all__ = ["PhoneNumberRetrieveResponse"]


class PhoneNumberRetrieveResponse(BaseModel):
    phone_number: OwnedPhoneNumber = FieldInfo(alias="phoneNumber")
