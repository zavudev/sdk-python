# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["AgentKnowledgeBase"]


class AgentKnowledgeBase(BaseModel):
    id: str

    agent_id: str = FieldInfo(alias="agentId")

    created_at: datetime = FieldInfo(alias="createdAt")

    document_count: int = FieldInfo(alias="documentCount")

    name: str

    total_chunks: int = FieldInfo(alias="totalChunks")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    description: Optional[str] = None
