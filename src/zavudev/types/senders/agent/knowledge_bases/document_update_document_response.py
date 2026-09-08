# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel
from ..agent_document import AgentDocument

__all__ = ["DocumentUpdateDocumentResponse"]


class DocumentUpdateDocumentResponse(BaseModel):
    document: AgentDocument
