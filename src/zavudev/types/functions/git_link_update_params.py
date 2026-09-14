# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["GitLinkUpdateParams"]


class GitLinkUpdateParams(TypedDict, total=False):
    auto_deploy: Annotated[bool, PropertyInfo(alias="autoDeploy")]

    branch: str

    root_dir: Annotated[Optional[str], PropertyInfo(alias="rootDir")]
