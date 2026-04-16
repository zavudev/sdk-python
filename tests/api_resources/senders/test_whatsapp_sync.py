# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from zavudev import Zavudev, AsyncZavudev
from tests.utils import assert_matches_type
from zavudev.types.senders import (
    WhatsappSyncRetrieveResponse,
    WhatsappSyncStartHistorySyncResponse,
    WhatsappSyncStartContactsSyncResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWhatsappSync:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Zavudev) -> None:
        whatsapp_sync = client.senders.whatsapp_sync.retrieve(
            "senderId",
        )
        assert_matches_type(WhatsappSyncRetrieveResponse, whatsapp_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Zavudev) -> None:
        response = client.senders.whatsapp_sync.with_raw_response.retrieve(
            "senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        whatsapp_sync = response.parse()
        assert_matches_type(WhatsappSyncRetrieveResponse, whatsapp_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Zavudev) -> None:
        with client.senders.whatsapp_sync.with_streaming_response.retrieve(
            "senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            whatsapp_sync = response.parse()
            assert_matches_type(WhatsappSyncRetrieveResponse, whatsapp_sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            client.senders.whatsapp_sync.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_start_contacts_sync(self, client: Zavudev) -> None:
        whatsapp_sync = client.senders.whatsapp_sync.start_contacts_sync(
            "senderId",
        )
        assert_matches_type(WhatsappSyncStartContactsSyncResponse, whatsapp_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_start_contacts_sync(self, client: Zavudev) -> None:
        response = client.senders.whatsapp_sync.with_raw_response.start_contacts_sync(
            "senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        whatsapp_sync = response.parse()
        assert_matches_type(WhatsappSyncStartContactsSyncResponse, whatsapp_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_start_contacts_sync(self, client: Zavudev) -> None:
        with client.senders.whatsapp_sync.with_streaming_response.start_contacts_sync(
            "senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            whatsapp_sync = response.parse()
            assert_matches_type(WhatsappSyncStartContactsSyncResponse, whatsapp_sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_start_contacts_sync(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            client.senders.whatsapp_sync.with_raw_response.start_contacts_sync(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_start_history_sync(self, client: Zavudev) -> None:
        whatsapp_sync = client.senders.whatsapp_sync.start_history_sync(
            "senderId",
        )
        assert_matches_type(WhatsappSyncStartHistorySyncResponse, whatsapp_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_start_history_sync(self, client: Zavudev) -> None:
        response = client.senders.whatsapp_sync.with_raw_response.start_history_sync(
            "senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        whatsapp_sync = response.parse()
        assert_matches_type(WhatsappSyncStartHistorySyncResponse, whatsapp_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_start_history_sync(self, client: Zavudev) -> None:
        with client.senders.whatsapp_sync.with_streaming_response.start_history_sync(
            "senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            whatsapp_sync = response.parse()
            assert_matches_type(WhatsappSyncStartHistorySyncResponse, whatsapp_sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_start_history_sync(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            client.senders.whatsapp_sync.with_raw_response.start_history_sync(
                "",
            )


class TestAsyncWhatsappSync:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncZavudev) -> None:
        whatsapp_sync = await async_client.senders.whatsapp_sync.retrieve(
            "senderId",
        )
        assert_matches_type(WhatsappSyncRetrieveResponse, whatsapp_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncZavudev) -> None:
        response = await async_client.senders.whatsapp_sync.with_raw_response.retrieve(
            "senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        whatsapp_sync = await response.parse()
        assert_matches_type(WhatsappSyncRetrieveResponse, whatsapp_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncZavudev) -> None:
        async with async_client.senders.whatsapp_sync.with_streaming_response.retrieve(
            "senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            whatsapp_sync = await response.parse()
            assert_matches_type(WhatsappSyncRetrieveResponse, whatsapp_sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            await async_client.senders.whatsapp_sync.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_start_contacts_sync(self, async_client: AsyncZavudev) -> None:
        whatsapp_sync = await async_client.senders.whatsapp_sync.start_contacts_sync(
            "senderId",
        )
        assert_matches_type(WhatsappSyncStartContactsSyncResponse, whatsapp_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_start_contacts_sync(self, async_client: AsyncZavudev) -> None:
        response = await async_client.senders.whatsapp_sync.with_raw_response.start_contacts_sync(
            "senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        whatsapp_sync = await response.parse()
        assert_matches_type(WhatsappSyncStartContactsSyncResponse, whatsapp_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_start_contacts_sync(self, async_client: AsyncZavudev) -> None:
        async with async_client.senders.whatsapp_sync.with_streaming_response.start_contacts_sync(
            "senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            whatsapp_sync = await response.parse()
            assert_matches_type(WhatsappSyncStartContactsSyncResponse, whatsapp_sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_start_contacts_sync(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            await async_client.senders.whatsapp_sync.with_raw_response.start_contacts_sync(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_start_history_sync(self, async_client: AsyncZavudev) -> None:
        whatsapp_sync = await async_client.senders.whatsapp_sync.start_history_sync(
            "senderId",
        )
        assert_matches_type(WhatsappSyncStartHistorySyncResponse, whatsapp_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_start_history_sync(self, async_client: AsyncZavudev) -> None:
        response = await async_client.senders.whatsapp_sync.with_raw_response.start_history_sync(
            "senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        whatsapp_sync = await response.parse()
        assert_matches_type(WhatsappSyncStartHistorySyncResponse, whatsapp_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_start_history_sync(self, async_client: AsyncZavudev) -> None:
        async with async_client.senders.whatsapp_sync.with_streaming_response.start_history_sync(
            "senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            whatsapp_sync = await response.parse()
            assert_matches_type(WhatsappSyncStartHistorySyncResponse, whatsapp_sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_start_history_sync(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            await async_client.senders.whatsapp_sync.with_raw_response.start_history_sync(
                "",
            )
