# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AddressCreateParams"]


class AddressCreateParams(TypedDict, total=False):
    country_code: Required[Annotated[str, PropertyInfo(alias="countryCode")]]

    locality: Required[str]

    postal_code: Required[Annotated[str, PropertyInfo(alias="postalCode")]]

    street_address: Required[Annotated[str, PropertyInfo(alias="streetAddress")]]

    administrative_area: Annotated[str, PropertyInfo(alias="administrativeArea")]

    business_name: Annotated[str, PropertyInfo(alias="businessName")]

    extended_address: Annotated[str, PropertyInfo(alias="extendedAddress")]

    first_name: Annotated[str, PropertyInfo(alias="firstName")]

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
