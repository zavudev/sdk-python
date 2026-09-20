# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["FlowTriggerParam"]


class FlowTriggerParam(TypedDict, total=False):
    type: Required[Literal["keyword", "intent", "always", "manual"]]
    """What starts a flow.

    - `keyword`: the message contains one of the words listed in `keywords`. Plain
      substring matching, so a word inside another word still counts.
    - `intent`: the message MEANS what `intent` describes, whatever words it uses.
    - `always`: any message starts it.
    - `manual`: reserved. Nothing starts a `manual` flow today — it is accepted and
      stored, and no message or endpoint runs it.
    """

    intent: str
    """One plain sentence describing what the contact wants, for `intent` triggers.

    Any language.

    The message is judged for meaning, not for words, so "kiero saber el presio"
    starts a flow whose intent is "quiere saber precios o cotizar", and "no quiero
    info de precios" starts nothing.

    A `keyword` or `always` flow with a higher `priority` is matched first and wins.
    At most 12 intent flows are considered per message, highest priority first. When
    the classification is unavailable or uncertain, the message is handled as if no
    intent matched, so a flow never starts on a guess.
    """

    keywords: SequenceNotStr[str]
    """Words that start the flow, for `keyword` triggers.

    Matched as substrings, case-insensitively, against the whole message: a flow on
    `info` also starts on "no quiero info". Use `intent` when that matters.
    """
