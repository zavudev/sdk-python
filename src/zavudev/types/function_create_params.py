# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FunctionCreateParams"]


class FunctionCreateParams(TypedDict, total=False):
    name: Required[str]

    slug: Required[str]
    """URL-safe identifier (lowercase, digits, hyphens). Must be unique per project."""

    dependencies: Dict[str, str]
    """npm dependencies. Keys are package names, values are semver ranges."""

    description: str

    http_enabled: Annotated[bool, PropertyInfo(alias="httpEnabled")]
    """Whether to expose a public HTTPS URL for this function."""

    memory_mb: Annotated[Literal[128, 256, 512, 1024], PropertyInfo(alias="memoryMb")]

    runtime: Literal["nodejs24"]
    """Runtime the function is deployed on."""

    source_code: Annotated[str, PropertyInfo(alias="sourceCode")]
    """TypeScript source code for the function entry point (max ~900KB)."""

    timeout_sec: Annotated[int, PropertyInfo(alias="timeoutSec")]
