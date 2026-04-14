# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BrandCreateParams"]


class BrandCreateParams(TypedDict, total=False):
    city: Required[str]

    country: Required[str]
    """Two-letter ISO country code."""

    display_name: Required[Annotated[str, PropertyInfo(alias="displayName")]]
    """Display name of the brand."""

    email: Required[str]

    entity_type: Required[
        Annotated[
            Literal["PRIVATE_PROFIT", "PUBLIC_PROFIT", "NON_PROFIT", "GOVERNMENT", "SOLE_PROPRIETOR"],
            PropertyInfo(alias="entityType"),
        ]
    ]
    """Business entity type for 10DLC brand registration."""

    phone: Required[str]
    """Contact phone in E.164 format."""

    postal_code: Required[Annotated[str, PropertyInfo(alias="postalCode")]]

    state: Required[str]

    street: Required[str]

    vertical: Required[str]
    """Industry vertical."""

    company_name: Annotated[str, PropertyInfo(alias="companyName")]
    """Legal company name."""

    ein: str
    """Employer Identification Number (format: XX-XXXXXXX)."""

    first_name: Annotated[str, PropertyInfo(alias="firstName")]

    last_name: Annotated[str, PropertyInfo(alias="lastName")]

    stock_exchange: Annotated[str, PropertyInfo(alias="stockExchange")]

    stock_symbol: Annotated[str, PropertyInfo(alias="stockSymbol")]

    website: str
