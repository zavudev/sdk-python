# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .flow_step_param import FlowStepParam
from .flow_trigger_param import FlowTriggerParam

__all__ = ["FlowCreateParams"]


class FlowCreateParams(TypedDict, total=False):
    name: Required[str]

    steps: Required[Iterable[FlowStepParam]]

    trigger: Required[FlowTriggerParam]

    description: str

    enabled: bool

    priority: int
