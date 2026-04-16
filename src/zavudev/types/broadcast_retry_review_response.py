# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .broadcast import Broadcast

__all__ = ["BroadcastRetryReviewResponse"]


class BroadcastRetryReviewResponse(BaseModel):
    broadcast: Broadcast
