# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .phone_number_pricing import PhoneNumberPricing
from .phone_number_capabilities import PhoneNumberCapabilities

__all__ = ["AvailablePhoneNumber"]


class AvailablePhoneNumber(BaseModel):
    capabilities: PhoneNumberCapabilities

    phone_number: str = FieldInfo(alias="phoneNumber")

    pricing: PhoneNumberPricing

    friendly_name: Optional[str] = FieldInfo(alias="friendlyName", default=None)

    locality: Optional[str] = None

    region: Optional[str] = None
