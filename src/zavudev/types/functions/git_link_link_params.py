# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["GitLinkLinkParams"]


class GitLinkLinkParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    auto_deploy: Annotated[bool, PropertyInfo(alias="autoDeploy")]

    branch: str

    root_dir: Annotated[str, PropertyInfo(alias="rootDir")]
    """Subdirectory holding the project, for monorepos."""
