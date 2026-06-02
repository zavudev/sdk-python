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

    template_button_variables: Annotated[Dict[str, str], PropertyInfo(alias="templateButtonVariables")]
    """Per-contact button variables for dynamic URL/OTP buttons.

    Keys are the button index (0, 1, 2).
    """

    template_header_variables: Annotated[Dict[str, str], PropertyInfo(alias="templateHeaderVariables")]
    """Per-contact value for a text-header variable, keyed by `1`.

    If omitted, Zavu resolves the header from `templateVariables` by the header
    placeholder's name.
    """

    template_variables: Annotated[Dict[str, str], PropertyInfo(alias="templateVariables")]
    """Per-contact body variables.

    Key them to match the template body: by position (`1`, `2`, ...) for positional
    templates, or by name (e.g. `customer_name`) for named templates. Zavu detects
    the template's format and sends the correct payload to Meta. Do not mix
    positional and named keys.
    """
