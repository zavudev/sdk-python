# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .ten_dlc_phone_number_assignment import TenDlcPhoneNumberAssignment

__all__ = ["PhoneNumberListResponse"]


class PhoneNumberListResponse(BaseModel):
    items: List[TenDlcPhoneNumberAssignment]

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
