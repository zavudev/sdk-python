# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TenDlcCampaign"]


class TenDlcCampaign(BaseModel):
    id: str

    affiliate_marketing: bool = FieldInfo(alias="affiliateMarketing")

    age_gated: bool = FieldInfo(alias="ageGated")

    brand_id: str = FieldInfo(alias="brandId")
    """ID of the brand this campaign belongs to."""

    created_at: datetime = FieldInfo(alias="createdAt")

    description: str
    """Description of the messaging campaign."""

    direct_lending: bool = FieldInfo(alias="directLending")

    embedded_link: bool = FieldInfo(alias="embeddedLink")

    embedded_phone: bool = FieldInfo(alias="embeddedPhone")

    name: str

    number_pooling: bool = FieldInfo(alias="numberPooling")

    sample_messages: List[str] = FieldInfo(alias="sampleMessages")
    """Sample messages representative of campaign content."""

    status: Literal["draft", "pending", "approved", "rejected"]
    """Status of a 10DLC campaign registration."""

    subscriber_help: bool = FieldInfo(alias="subscriberHelp")

    subscriber_opt_in: bool = FieldInfo(alias="subscriberOptIn")

    subscriber_opt_out: bool = FieldInfo(alias="subscriberOptOut")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    use_case: str = FieldInfo(alias="useCase")
    """Campaign use case type."""

    approved_at: Optional[datetime] = FieldInfo(alias="approvedAt", default=None)

    daily_limit: Optional[int] = FieldInfo(alias="dailyLimit", default=None)
    """Daily message limit based on brand trust score."""

    failure_reason: Optional[str] = FieldInfo(alias="failureReason", default=None)

    help_message: Optional[str] = FieldInfo(alias="helpMessage", default=None)

    message_flow: Optional[str] = FieldInfo(alias="messageFlow", default=None)

    monthly_fee_cents: Optional[int] = FieldInfo(alias="monthlyFeeCents", default=None)
    """Recurring monthly fee in cents."""

    opt_in_keywords: Optional[List[str]] = FieldInfo(alias="optInKeywords", default=None)

    opt_out_keywords: Optional[List[str]] = FieldInfo(alias="optOutKeywords", default=None)

    registration_cost_cents: Optional[int] = FieldInfo(alias="registrationCostCents", default=None)
    """One-time registration cost in cents."""

    submitted_at: Optional[datetime] = FieldInfo(alias="submittedAt", default=None)

    sub_use_cases: Optional[List[str]] = FieldInfo(alias="subUseCases", default=None)
