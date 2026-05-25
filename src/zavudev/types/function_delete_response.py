# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["FunctionDeleteResponse"]


class FunctionDeleteResponse(BaseModel):
    deleted: bool

    name: Optional[str] = None

    slug: Optional[str] = None
