# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .ten_dlc_campaign import TenDlcCampaign

__all__ = ["CampaignSubmitResponse"]


class CampaignSubmitResponse(BaseModel):
    campaign: TenDlcCampaign
