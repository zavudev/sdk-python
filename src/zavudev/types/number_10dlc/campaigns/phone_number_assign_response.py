# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel
from .ten_dlc_phone_number_assignment import TenDlcPhoneNumberAssignment

__all__ = ["PhoneNumberAssignResponse"]


class PhoneNumberAssignResponse(BaseModel):
    assignment: TenDlcPhoneNumberAssignment
