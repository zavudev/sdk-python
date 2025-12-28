# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .requirement_field_type import RequirementFieldType
from .requirement_acceptance_criteria import RequirementAcceptanceCriteria

__all__ = ["RequirementType"]


class RequirementType(BaseModel):
    """A specific requirement type within a requirement group."""

    id: str

    description: str

    name: str

    type: RequirementFieldType
    """Type of requirement field."""

    acceptance_criteria: Optional[RequirementAcceptanceCriteria] = FieldInfo(alias="acceptanceCriteria", default=None)
    """Acceptance criteria for a requirement."""

    example: Optional[str] = None
