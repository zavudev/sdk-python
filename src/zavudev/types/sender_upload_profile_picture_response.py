# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .whatsapp_business_profile import WhatsappBusinessProfile

__all__ = ["SenderUploadProfilePictureResponse"]


class SenderUploadProfilePictureResponse(BaseModel):
    profile: WhatsappBusinessProfile
    """WhatsApp Business profile information."""

    success: bool
