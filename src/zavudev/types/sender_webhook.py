# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .webhook_event import WebhookEvent

__all__ = ["SenderWebhook"]


class SenderWebhook(BaseModel):
    """Webhook configuration for the sender."""

    active: bool
    """Whether the webhook is active."""

    events: List[WebhookEvent]
    """List of events the webhook is subscribed to."""

    signature_version: Literal["v1", "v1+v2", "v2"] = FieldInfo(alias="signatureVersion")
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

    url: str
    """HTTPS URL that will receive webhook events."""

    secret: Optional[str] = None
    """Webhook secret for signature verification.

    Only returned on create or regenerate.
    """
