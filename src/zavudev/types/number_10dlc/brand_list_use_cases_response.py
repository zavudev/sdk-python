# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["BrandListUseCasesResponse", "UseCase"]


class UseCase(BaseModel):
    description: Optional[str] = None

    name: Optional[str] = None


class BrandListUseCasesResponse(BaseModel):
    use_cases: List[UseCase] = FieldInfo(alias="useCases")
