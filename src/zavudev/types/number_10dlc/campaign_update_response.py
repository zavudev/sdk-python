# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .ten_dlc_campaign import TenDlcCampaign

__all__ = ["CampaignUpdateResponse"]


class CampaignUpdateResponse(BaseModel):
    campaign: TenDlcCampaign
