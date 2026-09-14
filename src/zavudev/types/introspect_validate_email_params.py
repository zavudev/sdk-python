# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["IntrospectValidateEmailParams"]


class IntrospectValidateEmailParams(TypedDict, total=False):
    email: str
    """Single email address to validate."""

    emails: SequenceNotStr[str]
    """Batch of email addresses to validate (max 100)."""
