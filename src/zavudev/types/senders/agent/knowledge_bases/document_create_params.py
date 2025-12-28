# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["DocumentCreateParams"]


class DocumentCreateParams(TypedDict, total=False):
    sender_id: Required[Annotated[str, PropertyInfo(alias="senderId")]]

    content: Required[str]

    title: Required[str]
