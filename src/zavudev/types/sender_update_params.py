# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .webhook_event import WebhookEvent

__all__ = ["SenderUpdateParams"]


class SenderUpdateParams(TypedDict, total=False):
    email_address: Annotated[str, PropertyInfo(alias="emailAddress")]
    """Attach or change the sender's email from-address (e.g.

    noreply@yourdomain.com). The domain must be a verified email domain in your
    project.
    """

    email_catch_all_enabled: Annotated[bool, PropertyInfo(alias="emailCatchAllEnabled")]
    """Enable or disable domain catch-all.

    When enabled (with emailReceivingEnabled true), this sender receives email for
    any address at its domain. Ignored (treated as false) if receiving is not
    enabled.
    """

    email_domain_id: Annotated[str, PropertyInfo(alias="emailDomainId")]
    """ID of the verified email domain to attach.

    Optional — resolved from `emailAddress`'s domain when omitted.
    """

    email_from_name: Annotated[str, PropertyInfo(alias="emailFromName")]
    """Display name shown in the recipient's inbox for the email channel."""

    email_receiving_enabled: Annotated[bool, PropertyInfo(alias="emailReceivingEnabled")]
    """Enable or disable inbound email receiving for this sender."""

    name: str

    set_as_default: Annotated[bool, PropertyInfo(alias="setAsDefault")]

    webhook_active: Annotated[bool, PropertyInfo(alias="webhookActive")]
    """Whether the webhook is active."""

    webhook_events: Annotated[List[WebhookEvent], PropertyInfo(alias="webhookEvents")]
    """Events to subscribe to."""

    webhook_url: Annotated[Optional[str], PropertyInfo(alias="webhookUrl")]
    """HTTPS URL for webhook events. Set to null to remove webhook."""
