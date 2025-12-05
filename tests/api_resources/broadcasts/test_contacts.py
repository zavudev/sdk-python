# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from zavudev import Zavudev, AsyncZavudev
from tests.utils import assert_matches_type
from zavudev.types import BroadcastContact
from zavudev.pagination import SyncCursor, AsyncCursor
from zavudev.types.broadcasts import ContactAddResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContacts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Zavudev) -> None:
        contact = client.broadcasts.contacts.list(
            broadcast_id="broadcastId",
        )
        assert_matches_type(SyncCursor[BroadcastContact], contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Zavudev) -> None:
        contact = client.broadcasts.contacts.list(
            broadcast_id="broadcastId",
            cursor="cursor",
            limit=100,
            status="pending",
        )
        assert_matches_type(SyncCursor[BroadcastContact], contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Zavudev) -> None:
        response = client.broadcasts.contacts.with_raw_response.list(
            broadcast_id="broadcastId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(SyncCursor[BroadcastContact], contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Zavudev) -> None:
        with client.broadcasts.contacts.with_streaming_response.list(
            broadcast_id="broadcastId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(SyncCursor[BroadcastContact], contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            client.broadcasts.contacts.with_raw_response.list(
                broadcast_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add(self, client: Zavudev) -> None:
        contact = client.broadcasts.contacts.add(
            broadcast_id="broadcastId",
            contacts=[{"recipient": "+14155551234"}, {"recipient": "+14155555678"}],
        )
        assert_matches_type(ContactAddResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: Zavudev) -> None:
        response = client.broadcasts.contacts.with_raw_response.add(
            broadcast_id="broadcastId",
            contacts=[{"recipient": "+14155551234"}, {"recipient": "+14155555678"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactAddResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: Zavudev) -> None:
        with client.broadcasts.contacts.with_streaming_response.add(
            broadcast_id="broadcastId",
            contacts=[{"recipient": "+14155551234"}, {"recipient": "+14155555678"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactAddResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_add(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            client.broadcasts.contacts.with_raw_response.add(
                broadcast_id="",
                contacts=[{"recipient": "+14155551234"}, {"recipient": "+14155555678"}],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_remove(self, client: Zavudev) -> None:
        contact = client.broadcasts.contacts.remove(
            contact_id="contactId",
            broadcast_id="broadcastId",
        )
        assert contact is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: Zavudev) -> None:
        response = client.broadcasts.contacts.with_raw_response.remove(
            contact_id="contactId",
            broadcast_id="broadcastId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert contact is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: Zavudev) -> None:
        with client.broadcasts.contacts.with_streaming_response.remove(
            contact_id="contactId",
            broadcast_id="broadcastId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert contact is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_remove(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            client.broadcasts.contacts.with_raw_response.remove(
                contact_id="contactId",
                broadcast_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            client.broadcasts.contacts.with_raw_response.remove(
                contact_id="",
                broadcast_id="broadcastId",
            )


class TestAsyncContacts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncZavudev) -> None:
        contact = await async_client.broadcasts.contacts.list(
            broadcast_id="broadcastId",
        )
        assert_matches_type(AsyncCursor[BroadcastContact], contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncZavudev) -> None:
        contact = await async_client.broadcasts.contacts.list(
            broadcast_id="broadcastId",
            cursor="cursor",
            limit=100,
            status="pending",
        )
        assert_matches_type(AsyncCursor[BroadcastContact], contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncZavudev) -> None:
        response = await async_client.broadcasts.contacts.with_raw_response.list(
            broadcast_id="broadcastId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(AsyncCursor[BroadcastContact], contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncZavudev) -> None:
        async with async_client.broadcasts.contacts.with_streaming_response.list(
            broadcast_id="broadcastId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(AsyncCursor[BroadcastContact], contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            await async_client.broadcasts.contacts.with_raw_response.list(
                broadcast_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncZavudev) -> None:
        contact = await async_client.broadcasts.contacts.add(
            broadcast_id="broadcastId",
            contacts=[{"recipient": "+14155551234"}, {"recipient": "+14155555678"}],
        )
        assert_matches_type(ContactAddResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncZavudev) -> None:
        response = await async_client.broadcasts.contacts.with_raw_response.add(
            broadcast_id="broadcastId",
            contacts=[{"recipient": "+14155551234"}, {"recipient": "+14155555678"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactAddResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncZavudev) -> None:
        async with async_client.broadcasts.contacts.with_streaming_response.add(
            broadcast_id="broadcastId",
            contacts=[{"recipient": "+14155551234"}, {"recipient": "+14155555678"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactAddResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            await async_client.broadcasts.contacts.with_raw_response.add(
                broadcast_id="",
                contacts=[{"recipient": "+14155551234"}, {"recipient": "+14155555678"}],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncZavudev) -> None:
        contact = await async_client.broadcasts.contacts.remove(
            contact_id="contactId",
            broadcast_id="broadcastId",
        )
        assert contact is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncZavudev) -> None:
        response = await async_client.broadcasts.contacts.with_raw_response.remove(
            contact_id="contactId",
            broadcast_id="broadcastId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert contact is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncZavudev) -> None:
        async with async_client.broadcasts.contacts.with_streaming_response.remove(
            contact_id="contactId",
            broadcast_id="broadcastId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert contact is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            await async_client.broadcasts.contacts.with_raw_response.remove(
                contact_id="contactId",
                broadcast_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            await async_client.broadcasts.contacts.with_raw_response.remove(
                contact_id="",
                broadcast_id="broadcastId",
            )
