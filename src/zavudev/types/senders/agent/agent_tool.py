# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .tool_parameters import ToolParameters

__all__ = ["AgentTool"]


class AgentTool(BaseModel):
    id: str

    agent_id: str = FieldInfo(alias="agentId")

    created_at: datetime = FieldInfo(alias="createdAt")

    description: str
    """Description for the LLM to understand when to use this tool."""

    enabled: bool

    name: str

    parameters: ToolParameters

    updated_at: datetime = FieldInfo(alias="updatedAt")

    webhook_url: str = FieldInfo(alias="webhookUrl")
    """HTTPS URL to call when the tool is executed."""

    webhook_secret: Optional[str] = FieldInfo(alias="webhookSecret", default=None)
    """Signing secret for this tool's webhook.

    **Returned only when the tool is created**, never on a later read.

    Zavu generates one if you do not supply it, and signs every call to this tool
    with it: `X-Zavu-Signature: <hex>`, the HMAC-SHA256 of the request body. Verify
    it before trusting the call. Lost it? Rotate with
    `POST /v1/senders/{senderId}/agent/tools/{toolId}/webhook/secret`.
    """
