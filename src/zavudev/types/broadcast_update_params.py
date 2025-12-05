# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .broadcast_content_param import BroadcastContentParam

__all__ = ["BroadcastUpdateParams"]


class BroadcastUpdateParams(TypedDict, total=False):
    content: BroadcastContentParam
    """Content for non-text broadcast message types."""

    email_html_body: Annotated[str, PropertyInfo(alias="emailHtmlBody")]

    email_subject: Annotated[str, PropertyInfo(alias="emailSubject")]

    metadata: Dict[str, str]

    name: str

    text: str
