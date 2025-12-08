# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .available_phone_number import AvailablePhoneNumber

__all__ = ["PhoneNumberSearchAvailableResponse"]


class PhoneNumberSearchAvailableResponse(BaseModel):
    items: List[AvailablePhoneNumber]
