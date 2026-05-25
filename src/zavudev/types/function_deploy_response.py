# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["FunctionDeployResponse", "Deployment"]


class Deployment(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    function_id: str = FieldInfo(alias="functionId")

    status: Literal["pending", "bundling", "uploading", "publishing", "active", "failed", "superseded"]
    """Stage of a function deployment."""

    version: int
    """Monotonically increasing deployment version, starting at 1."""

    bundle_bytes: Optional[int] = FieldInfo(alias="bundleBytes", default=None)

    deployed_at: Optional[datetime] = FieldInfo(alias="deployedAt", default=None)

    error_message: Optional[str] = FieldInfo(alias="errorMessage", default=None)
    """Failure reason when status is 'failed'."""

    source_code_bytes: Optional[int] = FieldInfo(alias="sourceCodeBytes", default=None)


class FunctionDeployResponse(BaseModel):
    deployment: Deployment
