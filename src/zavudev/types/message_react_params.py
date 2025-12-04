# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MessageReactParams"]


class MessageReactParams(TypedDict, total=False):
    emoji: Required[str]
    """Single emoji character to react with."""

    zavu_sender: Annotated[str, PropertyInfo(alias="Zavu-Sender")]
