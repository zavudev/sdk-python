# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FunctionRollbackDeploymentParams"]


class FunctionRollbackDeploymentParams(TypedDict, total=False):
    deployment_id: Required[Annotated[str, PropertyInfo(alias="deploymentId")]]
    """ID of the deployment to roll back to."""
