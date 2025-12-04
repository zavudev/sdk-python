# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .message import Message
from .._models import BaseModel

__all__ = ["MessageResponse"]


class MessageResponse(BaseModel):
    message: Message
