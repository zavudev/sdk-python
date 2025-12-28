# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["AgentDocument"]


class AgentDocument(BaseModel):
    id: str

    chunk_count: int = FieldInfo(alias="chunkCount")
    """Number of chunks created from this document."""

    content_length: int = FieldInfo(alias="contentLength")
    """Length of the document content in characters."""

    created_at: datetime = FieldInfo(alias="createdAt")

    is_processed: bool = FieldInfo(alias="isProcessed")
    """Whether the document has been processed for RAG."""

    knowledge_base_id: str = FieldInfo(alias="knowledgeBaseId")

    title: str

    updated_at: datetime = FieldInfo(alias="updatedAt")
