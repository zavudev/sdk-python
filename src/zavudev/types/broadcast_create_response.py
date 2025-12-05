# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .broadcast import Broadcast

__all__ = ["BroadcastCreateResponse"]


class BroadcastCreateResponse(BaseModel):
    broadcast: Broadcast
