# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .phone_number_type import PhoneNumberType

__all__ = ["PhoneNumberPurchaseParams", "RegulatoryRequirement"]


class PhoneNumberPurchaseParams(TypedDict, total=False):
    phone_number: Required[Annotated[str, PropertyInfo(alias="phoneNumber")]]
    """Phone number in E.164 format."""

    name: str
    """Optional custom name for the phone number."""

    regulatory_requirements: Annotated[Iterable[RegulatoryRequirement], PropertyInfo(alias="regulatoryRequirements")]
    """Regulatory information, for numbers whose requirements list is not empty.

    Get the list with `GET /v1/phone-numbers/requirements?phoneNumber=...` and send
    one entry per requirement id, except `action` requirements, which take no value.
    Every required id must be present, once, and no unknown id may be sent;
    otherwise the purchase is refused with `400 invalid_request` before anything is
    charged.

    The information is kept for your project under the number's country and `type`.
    A later purchase there may omit this field if what is kept still covers that
    number's requirements. Omit it for numbers without requirements.
    """

    type: PhoneNumberType
    """Type of phone number.

    `mobile` is stocked in countries where no geographic (`local`) or non-geographic
    (`national`) inventory exists, and in several markets it is the only type that
    can receive SMS.
    """


class RegulatoryRequirement(TypedDict, total=False):
    field_value: Required[Annotated[str, PropertyInfo(alias="fieldValue")]]
    """
    Depends on the requirement's `type`: the text itself for `textual`; for
    `address`, the `id` of an address created in this project with
    `POST /v1/addresses`; for `document`, the `id` of a document created with
    `POST /v1/documents`. An address or document from another project, or one
    rejected in review, is refused.
    """

    requirement_type: Required[Annotated[str, PropertyInfo(alias="requirementType")]]
    """A `requirementTypes[].id` from `GET /v1/phone-numbers/requirements`.

    Each id may appear only once.
    """
