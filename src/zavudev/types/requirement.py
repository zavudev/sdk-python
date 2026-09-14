# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .requirement_type import RequirementType

__all__ = ["Requirement"]


class Requirement(BaseModel):
    """
    The requirements for ordering a number: for a country and number type, or for one specific number when requested with `phoneNumber` (then `id` is that phone number and `countryCode` is taken from it).
    """

    id: str

    action: str

    country_code: str = FieldInfo(alias="countryCode")

    phone_number_type: str = FieldInfo(alias="phoneNumberType")

    requirement_types: List[RequirementType] = FieldInfo(alias="requirementTypes")
