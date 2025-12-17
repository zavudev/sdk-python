# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .whatsapp_business_profile import WhatsappBusinessProfile

__all__ = ["WhatsappBusinessProfileResponse"]


class WhatsappBusinessProfileResponse(BaseModel):
    profile: WhatsappBusinessProfile
    """WhatsApp Business profile information."""
