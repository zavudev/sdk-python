# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MeRetrieveResponse", "APIKey", "Project", "Team"]


class APIKey(BaseModel):
    id: str


class Project(BaseModel):
    id: str

    is_sub_account: bool = FieldInfo(alias="isSubAccount")

    name: Optional[str] = None


class Team(BaseModel):
    id: str

    name: Optional[str] = None


class MeRetrieveResponse(BaseModel):
    api_key: APIKey = FieldInfo(alias="apiKey")

    is_test_mode: bool = FieldInfo(alias="isTestMode")

    project: Project

    team: Team
