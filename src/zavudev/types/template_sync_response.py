# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TemplateSyncResponse"]


class TemplateSyncResponse(BaseModel):
    accounts_synced: int = FieldInfo(alias="accountsSynced")
    """WhatsApp Business Accounts reconciled in this call."""

    errors: List[str]
    """Problems hit while syncing.

    Non-empty with a 200 means part of the sync did not complete — the rest still
    did.
    """

    imported: int
    """Templates that existed on Meta and were created in Zavu by this call."""

    linked: int
    """
    Existing Zavu templates that were matched to a Meta template by name and bound
    to its Meta ID.
    """

    skipped: int
    """
    Meta templates left alone: already linked to a Zavu template, or
    rejected/disabled on Meta.
    """

    updated: int
    """Templates whose approval status changed to match Meta."""
