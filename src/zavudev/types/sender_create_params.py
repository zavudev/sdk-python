# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .webhook_event import WebhookEvent

__all__ = ["SenderCreateParams"]


class SenderCreateParams(TypedDict, total=False):
    name: Required[str]

    email_address: Annotated[str, PropertyInfo(alias="emailAddress")]
    """From-address for the email channel (e.g.

    noreply@yourdomain.com). The address's domain must be a verified email domain in
    your project. Setting this attaches the email channel to the sender.
    """

    email_domain_id: Annotated[str, PropertyInfo(alias="emailDomainId")]
    """ID of the verified email domain to attach.

    Optional — resolved from `emailAddress`'s domain when omitted.
    """

    email_from_name: Annotated[str, PropertyInfo(alias="emailFromName")]
    """Display name shown in the recipient's inbox for the email channel."""

    email_receiving_enabled: Annotated[bool, PropertyInfo(alias="emailReceivingEnabled")]
    """Enable inbound email receiving on this sender.

    Requires a verified MX record on the domain; ignored otherwise.
    """

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """Phone number in E.164 format.

    Required for phone-based channels (SMS, WhatsApp). Omit for an email-only
    sender.
    """

    set_as_default: Annotated[bool, PropertyInfo(alias="setAsDefault")]

    webhook_events: Annotated[List[WebhookEvent], PropertyInfo(alias="webhookEvents")]
    """Events to subscribe to."""

    webhook_url: Annotated[str, PropertyInfo(alias="webhookUrl")]
    """HTTPS URL for webhook events."""
