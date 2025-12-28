# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .address import Address
from .._models import BaseModel

__all__ = ["AddressCreateResponse"]


class AddressCreateResponse(BaseModel):
    address: Address
    """A regulatory address for phone number requirements."""
