# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PhoneNumberCapabilities"]


class PhoneNumberCapabilities(BaseModel):
    mms: Optional[bool] = None

    sms: Optional[bool] = None

    voice: Optional[bool] = None
