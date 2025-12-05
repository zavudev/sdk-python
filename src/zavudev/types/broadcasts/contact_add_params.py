# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ContactAddParams", "Contact"]


class ContactAddParams(TypedDict, total=False):
    contacts: Required[Iterable[Contact]]
    """List of contacts to add (max 1000 per request)."""


class Contact(TypedDict, total=False):
    recipient: Required[str]
    """Phone number (E.164) or email address."""

    template_variables: Annotated[Dict[str, str], PropertyInfo(alias="templateVariables")]
    """Per-contact template variables to personalize the message."""
