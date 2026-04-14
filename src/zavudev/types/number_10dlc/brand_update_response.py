# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .ten_dlc_brand import TenDlcBrand

__all__ = ["BrandUpdateResponse"]


class BrandUpdateResponse(BaseModel):
    brand: TenDlcBrand
