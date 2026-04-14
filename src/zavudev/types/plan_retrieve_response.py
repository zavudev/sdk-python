# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PlanRetrieveResponse", "Limits"]


class Limits(BaseModel):
    broadcasts: Optional[bool] = None

    emails: Optional[int] = None
    """Monthly email limit."""

    messages_a2_p: Optional[int] = FieldInfo(alias="messagesA2P", default=None)
    """Monthly A2P message limit."""

    phone_numbers: Optional[int] = FieldInfo(alias="phoneNumbers", default=None)

    senders: Optional[int] = None

    sub_accounts: Optional[bool] = FieldInfo(alias="subAccounts", default=None)

    waba_connections: Optional[int] = FieldInfo(alias="wabaConnections", default=None)


class PlanRetrieveResponse(BaseModel):
    billing_interval: Literal["monthly", "annual"] = FieldInfo(alias="billingInterval")

    status: Literal["active", "past_due", "canceled", "trialing"]

    tier: Literal["free", "pro", "scale", "enterprise"]
    """Current subscription tier."""

    cancel_at_period_end: Optional[bool] = FieldInfo(alias="cancelAtPeriodEnd", default=None)

    current_period_end: Optional[datetime] = FieldInfo(alias="currentPeriodEnd", default=None)

    current_period_start: Optional[datetime] = FieldInfo(alias="currentPeriodStart", default=None)

    limits: Optional[Limits] = None
