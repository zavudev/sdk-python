# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Annotated, TypedDict

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

    enable_sms_oneway: Annotated[bool, PropertyInfo(alias="enableSmsOneway")]
    """Turn the one-way SMS channel on or off.

    Enabling needs nothing else and takes effect immediately; disabling removes the
    channel from the sender. Confirm with the `channels` array on the response.
    """

    enable_voice: Annotated[bool, PropertyInfo(alias="enableVoice")]
    """Turn the voice channel on or off.

    The sender must already have a phone number provisioned for calls; enabling it
    otherwise returns 400 instead of storing a flag that changes nothing. Confirm
    with the `channels` array on the response.
    """

    name: str

    set_as_default: Annotated[bool, PropertyInfo(alias="setAsDefault")]

    webhook_active: Annotated[bool, PropertyInfo(alias="webhookActive")]
    """Whether the webhook is active."""

    webhook_events: Annotated[List[WebhookEvent], PropertyInfo(alias="webhookEvents")]
    """Events to subscribe to."""

    webhook_signature_version: Annotated[Literal["v1", "v1+v2", "v2"], PropertyInfo(alias="webhookSignatureVersion")]
    """Which `X-Zavu-Signature` scheme this receiver is sent.

    - `v1`: `v1=HMAC_SHA256(secret, body)`. The scheme used before this was
      configurable. Existing webhooks stay on it until you move them.
    - `v2`: `v2=HMAC_SHA256(secret, "{t}.{body}")`. The current scheme, and the
      default for new senders. It signs the timestamp together with the body.
    - `v1+v2`: both signatures, sharing one `t`. The migration setting: a receiver
      reading either one works, so you can deploy and confirm your new verifier
      before switching over.

    Moving from `v1` straight to `v2` returns `400`. Set `v1+v2` first. See
    https://docs.zavu.dev/guides/receiving-messages/signature-migration
    """

    webhook_url: Annotated[Optional[str], PropertyInfo(alias="webhookUrl")]
    """HTTPS URL for webhook events. Set to null to remove webhook."""
