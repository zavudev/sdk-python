# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FunctionUpdateParams"]


class FunctionUpdateParams(TypedDict, total=False):
    dependencies: Dict[str, str]
    """New dependency map (replaces existing dependencies)."""

    http_enabled: Annotated[bool, PropertyInfo(alias="httpEnabled")]
    """Expose the function on its public HTTPS URL, or take it down.

    Applies to the already-deployed function without redeploying; the URL is
    returned as `publicUrl`.
    """

    source_code: Annotated[str, PropertyInfo(alias="sourceCode")]
    """New source code for the draft (replaces it)."""
