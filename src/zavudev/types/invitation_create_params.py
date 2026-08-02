# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["InvitationCreateParams"]


class InvitationCreateParams(TypedDict, total=False):
    allowed_phone_countries: Annotated[SequenceNotStr[str], PropertyInfo(alias="allowedPhoneCountries")]
    """ISO country codes for allowed phone numbers.

    Only valid when `connectionType` is `whatsapp_waba` — sending it with
    `messenger` returns 400.
    """

    client_email: Annotated[str, PropertyInfo(alias="clientEmail")]
    """Email of the client being invited."""

    client_name: Annotated[str, PropertyInfo(alias="clientName")]
    """Name of the client being invited."""

    client_phone: Annotated[str, PropertyInfo(alias="clientPhone")]
    """Phone number of the client in E.164 format."""

    connection_type: Annotated[Literal["whatsapp_waba", "messenger"], PropertyInfo(alias="connectionType")]
    """Which Meta channel the client connects, and how.

    - `whatsapp_waba` (default): Meta's embedded signup links an official WhatsApp
      Business Account. Accepts `phoneNumberId` and `allowedPhoneCountries`.
    - `messenger`: the client authorizes with Facebook and picks a Facebook Page
      they administer. The Page's Messenger inbox — including Marketplace chats — is
      routed to Zavu. They must be an admin of at least one Page. A Page can only be
      connected to one Zavu project at a time: if the client picks a Page that
      another project already connected, the newer connection wins and the older one
      is disconnected.

    One invitation connects one channel. To onboard a client on several channels,
    create one invitation per channel; each completes into its own sender.
    """

    expires_in_days: Annotated[int, PropertyInfo(alias="expiresInDays")]
    """Number of days until the invitation expires."""

    phone_number_id: Annotated[str, PropertyInfo(alias="phoneNumberId")]
    """ID of a Zavu phone number to pre-assign for WhatsApp registration.

    If provided, the client will use this number instead of their own. Only valid
    when `connectionType` is `whatsapp_waba` — sending it with `messenger` returns
    400, since a Facebook Page has no phone number.
    """
