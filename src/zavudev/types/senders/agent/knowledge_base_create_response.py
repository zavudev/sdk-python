# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .agent_knowledge_base import AgentKnowledgeBase

__all__ = ["KnowledgeBaseCreateResponse"]


class KnowledgeBaseCreateResponse(BaseModel):
    knowledge_base: AgentKnowledgeBase = FieldInfo(alias="knowledgeBase")
