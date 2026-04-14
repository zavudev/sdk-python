# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from .flow_step_param import FlowStepParam
from .flow_trigger_param import FlowTriggerParam

__all__ = ["FlowUpdateParams"]


class FlowUpdateParams(TypedDict, total=False):
    sender_id: Required[Annotated[str, PropertyInfo(alias="senderId")]]

    description: str

    enabled: bool

    name: str

    priority: int

    steps: Iterable[FlowStepParam]

    trigger: FlowTriggerParam
