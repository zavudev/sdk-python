# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .template import Template

__all__ = ["TemplateListResponse"]


class TemplateListResponse(BaseModel):
    items: List[Template]

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
