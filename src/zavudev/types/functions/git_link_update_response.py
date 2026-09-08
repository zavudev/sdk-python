# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["GitLinkUpdateResponse", "Link"]


class Link(BaseModel):
    """A GitHub repository bound to a function.

    A push to `branch` deploys the function. A function holds at most one link.
    """

    id: str

    auto_deploy: bool = FieldInfo(alias="autoDeploy")
    """When false the link is kept and pushes are ignored."""

    branch: str
    """Only pushes to this branch deploy."""

    connection: Literal["app", "manual"]
    """How this link authenticates, decided by the server rather than by the caller.

    - `app`: the Zavu GitHub App is installed on the account. Pushes arrive on the
      app's webhook and private repositories work. Nothing to configure in the
      repository.
    - `manual`: no installation. The link carries its own secret and you add the
      webhook to the repository yourself.
    """

    created_at: datetime = FieldInfo(alias="createdAt")

    function_id: str = FieldInfo(alias="functionId")

    owner: str

    provider: Literal["github"]

    repo: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    last_commit_message: Optional[str] = FieldInfo(alias="lastCommitMessage", default=None)

    last_commit_sha: Optional[str] = FieldInfo(alias="lastCommitSha", default=None)

    last_deploy_at: Optional[datetime] = FieldInfo(alias="lastDeployAt", default=None)

    last_error: Optional[str] = FieldInfo(alias="lastError", default=None)
    """Why the last deploy failed. Null otherwise."""

    last_status: Optional[Literal["deploying", "deployed", "failed"]] = FieldInfo(alias="lastStatus", default=None)

    root_dir: Optional[str] = FieldInfo(alias="rootDir", default=None)
    """Subdirectory holding the project, for monorepos.

    Null when the project is at the repository root.
    """


class GitLinkUpdateResponse(BaseModel):
    link: Link
    """A GitHub repository bound to a function.

    A push to `branch` deploys the function. A function holds at most one link.
    """

    webhook_url: str = FieldInfo(alias="webhookUrl")
    """Endpoint that receives GitHub's push deliveries.

    Only needed on a `manual` link, where you add it to the repository yourself.
    """

    webhook_secret: Optional[str] = FieldInfo(alias="webhookSecret", default=None)
    """Shared secret for the repository's webhook.

    **Returned only when creating a `manual` link, and only there** — every later
    read strips it, and re-linking mints a new one. Absent entirely on an `app`
    link, which needs no secret of its own.
    """
