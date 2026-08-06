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

    enable_sms_oneway: Annotated[bool, PropertyInfo(alias="enableSmsOneway")]
    """Enable the one-way SMS channel (`sms_oneway`).

    Needs nothing else — no phone number, no credential — so it is the fastest way
    to get a sender that can send. Recipients cannot reply. Confirm with
    `sms_oneway` in the `channels` array on the response.
    """

    enable_voice: Annotated[bool, PropertyInfo(alias="enableVoice")]
    """Let this sender place and answer phone calls.

    Requires `phoneNumber`; enabling it without one returns 400. Check the
    `channels` array on the response to confirm `voice` is on.
    """

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """
    Phone number in E.164 format, and it must be a number your project already owns
    (see `GET /v1/phone-numbers`). The number is routed to the sender as part of
    this call, which is what turns the SMS channel on. Passing a number the project
    does not own, or one already attached to another sender, returns 400 rather than
    creating a sender that cannot send. Omit for an email-only sender.
    """

    set_as_default: Annotated[bool, PropertyInfo(alias="setAsDefault")]

    webhook_events: Annotated[List[WebhookEvent], PropertyInfo(alias="webhookEvents")]
    """Events to subscribe to."""

    webhook_url: Annotated[str, PropertyInfo(alias="webhookUrl")]
    """HTTPS URL for webhook events."""
