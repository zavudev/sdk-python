# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .address_status import AddressStatus

__all__ = ["Address"]


class Address(BaseModel):
    """A regulatory address for phone number requirements."""

    id: str

    country_code: str = FieldInfo(alias="countryCode")

    created_at: datetime = FieldInfo(alias="createdAt")

    locality: str

    postal_code: str = FieldInfo(alias="postalCode")

    status: AddressStatus

    street_address: str = FieldInfo(alias="streetAddress")

    administrative_area: Optional[str] = FieldInfo(alias="administrativeArea", default=None)

    business_name: Optional[str] = FieldInfo(alias="businessName", default=None)

    extended_address: Optional[str] = FieldInfo(alias="extendedAddress", default=None)

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
