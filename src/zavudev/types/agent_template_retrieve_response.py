# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AgentTemplateRetrieveResponse", "Template", "TemplateFile", "TemplateRequiredSecret"]


class TemplateFile(BaseModel):
    content: str
    """File contents to write verbatim."""

    path: str


class TemplateRequiredSecret(BaseModel):
    hint: str

    key: str


class Template(BaseModel):
    """
    A fully rendered factory agent: the function files to scaffold plus the secrets it needs. Returned by GET /v1/agent-templates/{templateId} and consumed by `npx zavudev agents pull`.
    """

    id: str

    category: Literal["sales", "support", "frontDesk", "ops"]

    default_slug: str = FieldInfo(alias="defaultSlug")

    dependencies: Dict[str, str]
    """npm dependencies for the scaffolded function."""

    files: List[TemplateFile]

    name: str

    required_secrets: List[TemplateRequiredSecret] = FieldInfo(alias="requiredSecrets")

    summary: str

    voice: bool


class AgentTemplateRetrieveResponse(BaseModel):
    template: Template
    """
    A fully rendered factory agent: the function files to scaffold plus the secrets
    it needs. Returned by GET /v1/agent-templates/{templateId} and consumed by
    `npx zavudev agents pull`.
    """
