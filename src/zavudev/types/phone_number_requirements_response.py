# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .requirement import Requirement

__all__ = ["PhoneNumberRequirementsResponse"]


class PhoneNumberRequirementsResponse(BaseModel):
    items: List[Requirement]
