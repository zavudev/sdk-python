# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AgentTestResponse", "ExecutedToolCall"]


class ExecutedToolCall(BaseModel):
    name: str

    ok: bool

    error: Optional[str] = None


class AgentTestResponse(BaseModel):
    error: Optional[str] = None

    input_tokens: int = FieldInfo(alias="inputTokens")

    knowledge_chunks_used: int = FieldInfo(alias="knowledgeChunksUsed")
    """Knowledge-base chunks retrieved for this message.

    Zero means the answer was not grounded in your documents.
    """

    latency_ms: int = FieldInfo(alias="latencyMs")

    output_tokens: int = FieldInfo(alias="outputTokens")

    success: bool

    text: Optional[str] = None
    """What the agent would reply."""

    warnings: List[str]
    """Things that are true of this agent but that a dry run cannot prove.

    Surfaced so a passing dry run is never mistaken for proof that the agent works
    live.

    - The agent being disabled.
    - Enabled tools that were **not offered to the model** here — the model never
      saw them, so a reply that looks like a lookup was invented. Live conversations
      on every channel do offer them; running them here would cause real side
      effects.
    - An agent whose sender has none of the channels it triggers on, which answers
      every dry run and no real message.
    - Contact metadata that exists on a real conversation but not here.
    """

    executed_tool_calls: Optional[List[ExecutedToolCall]] = FieldInfo(alias="executedToolCalls", default=None)
    """Tools that actually ran, in order, when the request set `executeTools`.

    Empty on a normal dry run, where nothing is executed. An entry with `ok: false`
    means the agent saw an error and answered around it, which is what a customer
    would have received.
    """
