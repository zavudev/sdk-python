# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["CampaignUpdateParams"]


class CampaignUpdateParams(TypedDict, total=False):
    description: str

    help_message: Annotated[str, PropertyInfo(alias="helpMessage")]

    message_flow: Annotated[str, PropertyInfo(alias="messageFlow")]

    name: str

    opt_in_keywords: Annotated[SequenceNotStr[str], PropertyInfo(alias="optInKeywords")]

    opt_out_keywords: Annotated[SequenceNotStr[str], PropertyInfo(alias="optOutKeywords")]

    sample_messages: Annotated[SequenceNotStr[str], PropertyInfo(alias="sampleMessages")]
