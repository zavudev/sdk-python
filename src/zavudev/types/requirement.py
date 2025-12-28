# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .requirement_type import RequirementType

__all__ = ["Requirement"]


class Requirement(BaseModel):
    """A group of requirements for a specific country/phone type combination."""

    id: str

    action: str

    country_code: str = FieldInfo(alias="countryCode")

    phone_number_type: str = FieldInfo(alias="phoneNumberType")

    requirement_types: List[RequirementType] = FieldInfo(alias="requirementTypes")
