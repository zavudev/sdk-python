# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ContactListParams"]


class ContactListParams(TypedDict, total=False):
    cursor: str
    """Opaque cursor from a previous response's `nextCursor`. Do not construct it."""

    limit: int

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """Exact match on the contact's primary phone number, in E.164."""

    search: str
    """
    Free-text match over the contact's name (`displayName` and the WhatsApp profile
    name), phone numbers and email addresses. Case- and accent-insensitive. A phone
    number matches on a trailing fragment too, so `5551234` finds `+14155551234`.

    Contacts created automatically from an inbound message have no `displayName` —
    they are matched by their identifier until you set one with
    `PATCH /v1/contacts/{contactId}`.

    Results come back in relevance order rather than newest-first. `cursor` is
    opaque in both modes; pass back exactly what the previous response returned, and
    start a new pagination run when the search term changes.
    """

    tag: SequenceNotStr[str]
    """Tag name.

    Repeatable: `?tag=vip&tag=chile` returns contacts carrying **every** tag given,
    not any of them — the same rule the dashboard filter applies.

    Tags are matched by name, case-insensitively. An unknown tag returns 400 rather
    than being ignored, because a typo that silently matched every contact would be
    a worse answer than an error.
    """
