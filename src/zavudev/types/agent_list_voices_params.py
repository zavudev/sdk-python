# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AgentListVoicesParams"]


class AgentListVoicesParams(TypedDict, total=False):
    language: str
    """BCP-47 tag (`en`, `es`, `pt-BR`). Omit, or pass `auto`, for every voice."""
