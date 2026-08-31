# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AgentTestParams", "History"]


class AgentTestParams(TypedDict, total=False):
    message: Required[str]
    """What to say to the agent."""

    execute_tools: Annotated[bool, PropertyInfo(alias="executeTools")]
    """Run the tools the agent calls instead of reporting the choice and stopping.

    Off by default because a tool handler talks to the outside world: a rehearsal
    that charges a card is not a rehearsal. Turn it on to exercise the loop that
    actually matters — the model picks a tool, the handler answers, the model
    replies with the result — without sending a message to anyone. What ran comes
    back in `executedToolCalls`.
    """

    history: Iterable[History]
    """
    Prior turns, oldest first, to exercise multi-turn behaviour without persisting a
    thread. Trimmed to the agent's context window.
    """

    use_knowledge_base: Annotated[bool, PropertyInfo(alias="useKnowledgeBase")]
    """
    Set false to skip retrieval and isolate prompt behaviour from the knowledge
    base.
    """


class History(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["user", "assistant"]]
