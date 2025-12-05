# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ContactAddResponse", "Error"]


class Error(BaseModel):
    reason: Optional[str] = None

    recipient: Optional[str] = None


class ContactAddResponse(BaseModel):
    added: int
    """Number of contacts successfully added."""

    duplicates: int
    """Number of duplicate contacts skipped."""

    invalid: int
    """Number of invalid contacts rejected."""

    errors: Optional[List[Error]] = None
    """Details about invalid contacts."""
