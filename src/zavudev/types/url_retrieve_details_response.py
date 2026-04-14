# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .verified_url import VerifiedURL

__all__ = ["URLRetrieveDetailsResponse"]


class URLRetrieveDetailsResponse(BaseModel):
    url: VerifiedURL
