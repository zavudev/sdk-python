# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["CampaignCreateParams"]


class CampaignCreateParams(TypedDict, total=False):
    affiliate_marketing: Required[Annotated[bool, PropertyInfo(alias="affiliateMarketing")]]

    age_gated: Required[Annotated[bool, PropertyInfo(alias="ageGated")]]

    brand_id: Required[Annotated[str, PropertyInfo(alias="brandId")]]
    """ID of the brand to create this campaign under."""

    description: Required[str]

    direct_lending: Required[Annotated[bool, PropertyInfo(alias="directLending")]]

    embedded_link: Required[Annotated[bool, PropertyInfo(alias="embeddedLink")]]

    embedded_phone: Required[Annotated[bool, PropertyInfo(alias="embeddedPhone")]]

    name: Required[str]

    number_pooling: Required[Annotated[bool, PropertyInfo(alias="numberPooling")]]

    sample_messages: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="sampleMessages")]]

    subscriber_help: Required[Annotated[bool, PropertyInfo(alias="subscriberHelp")]]

    subscriber_opt_in: Required[Annotated[bool, PropertyInfo(alias="subscriberOptIn")]]

    subscriber_opt_out: Required[Annotated[bool, PropertyInfo(alias="subscriberOptOut")]]

    use_case: Required[Annotated[str, PropertyInfo(alias="useCase")]]
    """Campaign use case (e.g., ACCOUNT_NOTIFICATION, MARKETING, 2FA)."""

    help_message: Annotated[str, PropertyInfo(alias="helpMessage")]

    message_flow: Annotated[str, PropertyInfo(alias="messageFlow")]

    opt_in_keywords: Annotated[SequenceNotStr[str], PropertyInfo(alias="optInKeywords")]

    opt_out_keywords: Annotated[SequenceNotStr[str], PropertyInfo(alias="optOutKeywords")]

    sub_use_cases: Annotated[SequenceNotStr[str], PropertyInfo(alias="subUseCases")]
