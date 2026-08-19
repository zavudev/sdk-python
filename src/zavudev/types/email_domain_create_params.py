# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EmailDomainCreateParams"]


class EmailDomainCreateParams(TypedDict, total=False):
    domain: Required[str]
    """Bare domain, e.g. example.com."""
