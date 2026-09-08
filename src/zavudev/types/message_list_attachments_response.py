# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MessageListAttachmentsResponse", "Item"]


class Item(BaseModel):
    """A stored file attachment for an email message (inbound or outbound)."""

    id: str

    content_id: Optional[str] = FieldInfo(alias="contentId", default=None)
    """
    Content-ID for inline attachments (referenced in the HTML body as
    `cid:<contentId>`). Null for regular attachments.
    """

    created_at: datetime = FieldInfo(alias="createdAt")

    download_url: Optional[str] = FieldInfo(alias="downloadUrl", default=None)
    """Short-lived signed URL to download the attachment bytes.

    Freshly generated on each request and expires; do not cache it. Null if the
    stored file is no longer available.
    """

    filename: str

    is_inline: bool = FieldInfo(alias="isInline")
    """
    Whether the attachment is inline (embedded in the HTML body) rather than a
    regular attachment.
    """

    mime_type: str = FieldInfo(alias="mimeType")
    """MIME type of the attachment."""

    size: int
    """Size of the attachment in bytes."""


class MessageListAttachmentsResponse(BaseModel):
    items: List[Item]
