# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RegulatoryDocumentUploadURLResponse"]


class RegulatoryDocumentUploadURLResponse(BaseModel):
    upload_url: str = FieldInfo(alias="uploadUrl")
    """Pre-signed URL for uploading the file."""
