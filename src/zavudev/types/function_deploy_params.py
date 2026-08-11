# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FunctionDeployParams"]


class FunctionDeployParams(TypedDict, total=False):
    dependencies: Dict[str, str]
    """New dependency map (replaces existing dependencies)."""

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

    source_code: Annotated[str, PropertyInfo(alias="sourceCode")]
    """
    Shortcut for a single-file function: exactly equivalent to sending `files` with
    one entry named after `entrypoint` (`index.ts` by default). Fully supported —
    use whichever fits. If both are sent, `files` wins.
    """
