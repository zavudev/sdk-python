# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RequirementAcceptanceCriteria"]


class RequirementAcceptanceCriteria(BaseModel):
    """Acceptance criteria for a requirement."""

    allowed_values: Optional[List[str]] = FieldInfo(alias="allowedValues", default=None)

    max_length: Optional[int] = FieldInfo(alias="maxLength", default=None)

    min_length: Optional[int] = FieldInfo(alias="minLength", default=None)

    regex_pattern: Optional[str] = FieldInfo(alias="regexPattern", default=None)
