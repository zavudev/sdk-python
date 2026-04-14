# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from ..contact_channel import ContactChannel

__all__ = ["ChannelUpdateResponse"]


class ChannelUpdateResponse(BaseModel):
    channel: ContactChannel
    """A communication channel for a contact."""
