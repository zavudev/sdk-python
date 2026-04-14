# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .invitation import Invitation

__all__ = ["InvitationCancelResponse"]


class InvitationCancelResponse(BaseModel):
    invitation: Invitation
