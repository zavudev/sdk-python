# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BrandUpdateParams"]


class BrandUpdateParams(TypedDict, total=False):
    city: str

    company_name: Annotated[str, PropertyInfo(alias="companyName")]

    country: str

    display_name: Annotated[str, PropertyInfo(alias="displayName")]

    ein: str

    email: str

    entity_type: Annotated[
        Literal["PRIVATE_PROFIT", "PUBLIC_PROFIT", "NON_PROFIT", "GOVERNMENT", "SOLE_PROPRIETOR"],
        PropertyInfo(alias="entityType"),
    ]
    """Business entity type for 10DLC brand registration."""

    first_name: Annotated[str, PropertyInfo(alias="firstName")]

    last_name: Annotated[str, PropertyInfo(alias="lastName")]

    phone: str

    postal_code: Annotated[str, PropertyInfo(alias="postalCode")]

    state: str

    stock_exchange: Annotated[str, PropertyInfo(alias="stockExchange")]

    stock_symbol: Annotated[str, PropertyInfo(alias="stockSymbol")]

    street: str

    vertical: str

    website: str
