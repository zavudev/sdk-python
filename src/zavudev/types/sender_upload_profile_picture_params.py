# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SenderUploadProfilePictureParams"]


class SenderUploadProfilePictureParams(TypedDict, total=False):
    image_url: Required[Annotated[str, PropertyInfo(alias="imageUrl")]]
    """URL of the image to upload."""

    mime_type: Required[Annotated[Literal["image/jpeg", "image/png"], PropertyInfo(alias="mimeType")]]
    """MIME type of the image."""
