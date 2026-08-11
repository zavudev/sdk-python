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

    entrypoint: str
    """Which file in `files` is the entry point. Defaults to `index.ts`."""

    files: Dict[str, str]
    """The project's source files, keyed by path relative to the project root (e.g.

    `index.ts`, `lib/orders.ts`). Imports between them are resolved when the
    function is built, so a function can be split across as many files as it needs.

    Paths must be relative and use forward slashes; `..`, `node_modules/` and
    `package.json` are rejected. npm packages are not uploaded here — declare them
    under `dependencies` and Zavu installs them. Limits: 200 files and 900,000 bytes
    for the whole tree.
    """

    http_enabled: Annotated[bool, PropertyInfo(alias="httpEnabled")]
    """Whether to expose a public HTTPS URL for this function."""

    memory_mb: Annotated[Literal[128, 256, 512, 1024], PropertyInfo(alias="memoryMb")]

    runtime: Literal["nodejs24"]
    """Runtime the function is deployed on."""

    source_code: Annotated[str, PropertyInfo(alias="sourceCode")]
    """
    Shortcut for a single-file function: exactly equivalent to sending `files` with
    one entry named after `entrypoint` (`index.ts` by default). Fully supported —
    use whichever fits. If both are sent, `files` wins.
    """

    timeout_sec: Annotated[int, PropertyInfo(alias="timeoutSec")]
    """Per-invocation timeout in seconds.

    Event and cron invocations are asynchronous, so a long timeout only bounds cost;
    a tool called during a live conversation holds up the reply, and a function
    exposed over HTTP is additionally bounded by the platform's HTTP response limit.
    """
