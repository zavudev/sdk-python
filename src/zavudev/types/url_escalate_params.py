# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["URLEscalateParams"]


class URLEscalateParams(TypedDict, total=False):
    reason: Required[str]
    """Why the URL should be reviewed manually."""
