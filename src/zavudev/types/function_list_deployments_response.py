# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["FunctionListDeploymentsResponse", "Deployment"]


class Deployment(BaseModel):
    id: Optional[str] = None

    bundle_size_bytes: Optional[int] = FieldInfo(alias="bundleSizeBytes", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    deployed_at: Optional[datetime] = FieldInfo(alias="deployedAt", default=None)

    error_message: Optional[str] = FieldInfo(alias="errorMessage", default=None)

    is_active: Optional[bool] = FieldInfo(alias="isActive", default=None)

    status: Optional[Literal["pending", "bundling", "uploading", "publishing", "active", "failed", "superseded"]] = None
    """Stage of a function deployment."""

    version: Optional[int] = None


class FunctionListDeploymentsResponse(BaseModel):
    deployments: List[Deployment]
