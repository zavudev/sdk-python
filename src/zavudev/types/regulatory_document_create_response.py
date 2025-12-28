# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .regulatory_document import RegulatoryDocument

__all__ = ["RegulatoryDocumentCreateResponse"]


class RegulatoryDocumentCreateResponse(BaseModel):
    document: RegulatoryDocument
    """A regulatory document for phone number requirements."""
