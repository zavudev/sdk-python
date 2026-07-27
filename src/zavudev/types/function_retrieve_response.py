# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["FunctionRetrieveResponse", "Function"]


class Function(BaseModel):
    """
    A Zavu Function — user-supplied TypeScript that runs in Zavu Cloud and reacts to messaging events or HTTP requests.
    """

    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    dependencies: Dict[str, str]
    """npm dependencies installed in the function bundle.

    Keys are package names, values are semver ranges.
    """

    http_enabled: bool = FieldInfo(alias="httpEnabled")
    """Whether the function can be invoked over HTTPS via its public URL."""

    memory_mb: int = FieldInfo(alias="memoryMb")
    """Memory allocation in MB."""

    name: str

    runtime: Literal["nodejs24"]
    """Runtime the function is deployed on."""

    slug: str
    """URL-safe identifier, unique per project."""

    status: Literal["draft", "bundling", "deploying", "active", "failed", "disabled"]
    """Lifecycle status of a Zavu Function."""

    timeout_sec: int = FieldInfo(alias="timeoutSec")
    """Per-invocation timeout in seconds."""

    updated_at: datetime = FieldInfo(alias="updatedAt")

    active_deployment_id: Optional[str] = FieldInfo(alias="activeDeploymentId", default=None)
    """ID of the deployment currently serving traffic."""

    description: Optional[str] = None

    public_url: Optional[str] = FieldInfo(alias="publicUrl", default=None)
    """HTTPS endpoint, present only while httpEnabled is true.

    Null otherwise, including for a function that was previously exposed — the
    stored URL stops serving the moment HTTP is turned off, so it is never returned.
    """


class FunctionRetrieveResponse(BaseModel):
    function: Function
    """
    A Zavu Function — user-supplied TypeScript that runs in Zavu Cloud and reacts to
    messaging events or HTTP requests.
    """
