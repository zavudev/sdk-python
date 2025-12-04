# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SenderUpdateParams"]


class SenderUpdateParams(TypedDict, total=False):
    name: str

    set_as_default: Annotated[bool, PropertyInfo(alias="setAsDefault")]
