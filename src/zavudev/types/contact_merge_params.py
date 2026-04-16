# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ContactMergeParams"]


class ContactMergeParams(TypedDict, total=False):
    source_contact_id: Required[Annotated[str, PropertyInfo(alias="sourceContactId")]]
    """ID of the contact to merge into the target contact.

    The source contact will be marked as merged.
    """
