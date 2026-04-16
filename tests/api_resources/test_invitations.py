# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from zavudev import Zavudev, AsyncZavudev
from tests.utils import assert_matches_type
from zavudev.types import (
    Invitation,
    InvitationCancelResponse,
    InvitationCreateResponse,
    InvitationRetrieveResponse,
)
from zavudev.pagination import SyncCursor, AsyncCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInvitations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Zavudev) -> None:
        invitation = client.invitations.create()
        assert_matches_type(InvitationCreateResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Zavudev) -> None:
        invitation = client.invitations.create(
            allowed_phone_countries=["US", "MX"],
            client_email="contact@acme.com",
            client_name="Acme Corp",
            client_phone="+14155551234",
            expires_in_days=1,
            phone_number_id="pn_abc123",
        )
        assert_matches_type(InvitationCreateResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Zavudev) -> None:
        response = client.invitations.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invitation = response.parse()
        assert_matches_type(InvitationCreateResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Zavudev) -> None:
        with client.invitations.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invitation = response.parse()
            assert_matches_type(InvitationCreateResponse, invitation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Zavudev) -> None:
        invitation = client.invitations.retrieve(
            "invitationId",
        )
        assert_matches_type(InvitationRetrieveResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Zavudev) -> None:
        response = client.invitations.with_raw_response.retrieve(
            "invitationId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invitation = response.parse()
        assert_matches_type(InvitationRetrieveResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Zavudev) -> None:
        with client.invitations.with_streaming_response.retrieve(
            "invitationId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invitation = response.parse()
            assert_matches_type(InvitationRetrieveResponse, invitation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invitation_id` but received ''"):
            client.invitations.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Zavudev) -> None:
        invitation = client.invitations.list()
        assert_matches_type(SyncCursor[Invitation], invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Zavudev) -> None:
        invitation = client.invitations.list(
            cursor="cursor",
            limit=100,
            status="pending",
        )
        assert_matches_type(SyncCursor[Invitation], invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Zavudev) -> None:
        response = client.invitations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invitation = response.parse()
        assert_matches_type(SyncCursor[Invitation], invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Zavudev) -> None:
        with client.invitations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invitation = response.parse()
            assert_matches_type(SyncCursor[Invitation], invitation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel(self, client: Zavudev) -> None:
        invitation = client.invitations.cancel(
            "invitationId",
        )
        assert_matches_type(InvitationCancelResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: Zavudev) -> None:
        response = client.invitations.with_raw_response.cancel(
            "invitationId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invitation = response.parse()
        assert_matches_type(InvitationCancelResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: Zavudev) -> None:
        with client.invitations.with_streaming_response.cancel(
            "invitationId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invitation = response.parse()
            assert_matches_type(InvitationCancelResponse, invitation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_cancel(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invitation_id` but received ''"):
            client.invitations.with_raw_response.cancel(
                "",
            )


class TestAsyncInvitations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncZavudev) -> None:
        invitation = await async_client.invitations.create()
        assert_matches_type(InvitationCreateResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncZavudev) -> None:
        invitation = await async_client.invitations.create(
            allowed_phone_countries=["US", "MX"],
            client_email="contact@acme.com",
            client_name="Acme Corp",
            client_phone="+14155551234",
            expires_in_days=1,
            phone_number_id="pn_abc123",
        )
        assert_matches_type(InvitationCreateResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncZavudev) -> None:
        response = await async_client.invitations.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invitation = await response.parse()
        assert_matches_type(InvitationCreateResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncZavudev) -> None:
        async with async_client.invitations.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invitation = await response.parse()
            assert_matches_type(InvitationCreateResponse, invitation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncZavudev) -> None:
        invitation = await async_client.invitations.retrieve(
            "invitationId",
        )
        assert_matches_type(InvitationRetrieveResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncZavudev) -> None:
        response = await async_client.invitations.with_raw_response.retrieve(
            "invitationId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invitation = await response.parse()
        assert_matches_type(InvitationRetrieveResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncZavudev) -> None:
        async with async_client.invitations.with_streaming_response.retrieve(
            "invitationId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invitation = await response.parse()
            assert_matches_type(InvitationRetrieveResponse, invitation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invitation_id` but received ''"):
            await async_client.invitations.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncZavudev) -> None:
        invitation = await async_client.invitations.list()
        assert_matches_type(AsyncCursor[Invitation], invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncZavudev) -> None:
        invitation = await async_client.invitations.list(
            cursor="cursor",
            limit=100,
            status="pending",
        )
        assert_matches_type(AsyncCursor[Invitation], invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncZavudev) -> None:
        response = await async_client.invitations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invitation = await response.parse()
        assert_matches_type(AsyncCursor[Invitation], invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncZavudev) -> None:
        async with async_client.invitations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invitation = await response.parse()
            assert_matches_type(AsyncCursor[Invitation], invitation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncZavudev) -> None:
        invitation = await async_client.invitations.cancel(
            "invitationId",
        )
        assert_matches_type(InvitationCancelResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncZavudev) -> None:
        response = await async_client.invitations.with_raw_response.cancel(
            "invitationId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invitation = await response.parse()
        assert_matches_type(InvitationCancelResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncZavudev) -> None:
        async with async_client.invitations.with_streaming_response.cancel(
            "invitationId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invitation = await response.parse()
            assert_matches_type(InvitationCancelResponse, invitation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invitation_id` but received ''"):
            await async_client.invitations.with_raw_response.cancel(
                "",
            )
