# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from zavudev import Zavudev, AsyncZavudev
from tests.utils import assert_matches_type
from zavudev.types.agents import SenderConnectResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSenders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_connect(self, client: Zavudev) -> None:
        sender = client.agents.senders.connect(
            agent_id="agentId",
            sender_id="senderId",
        )
        assert_matches_type(SenderConnectResponse, sender, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_connect(self, client: Zavudev) -> None:
        response = client.agents.senders.with_raw_response.connect(
            agent_id="agentId",
            sender_id="senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sender = response.parse()
        assert_matches_type(SenderConnectResponse, sender, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_connect(self, client: Zavudev) -> None:
        with client.agents.senders.with_streaming_response.connect(
            agent_id="agentId",
            sender_id="senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sender = response.parse()
            assert_matches_type(SenderConnectResponse, sender, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_connect(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.senders.with_raw_response.connect(
                agent_id="",
                sender_id="senderId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_disconnect(self, client: Zavudev) -> None:
        sender = client.agents.senders.disconnect(
            sender_id="senderId",
            agent_id="agentId",
        )
        assert sender is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_disconnect(self, client: Zavudev) -> None:
        response = client.agents.senders.with_raw_response.disconnect(
            sender_id="senderId",
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sender = response.parse()
        assert sender is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_disconnect(self, client: Zavudev) -> None:
        with client.agents.senders.with_streaming_response.disconnect(
            sender_id="senderId",
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sender = response.parse()
            assert sender is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_disconnect(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.senders.with_raw_response.disconnect(
                sender_id="senderId",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            client.agents.senders.with_raw_response.disconnect(
                sender_id="",
                agent_id="agentId",
            )


class TestAsyncSenders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_connect(self, async_client: AsyncZavudev) -> None:
        sender = await async_client.agents.senders.connect(
            agent_id="agentId",
            sender_id="senderId",
        )
        assert_matches_type(SenderConnectResponse, sender, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_connect(self, async_client: AsyncZavudev) -> None:
        response = await async_client.agents.senders.with_raw_response.connect(
            agent_id="agentId",
            sender_id="senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sender = await response.parse()
        assert_matches_type(SenderConnectResponse, sender, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_connect(self, async_client: AsyncZavudev) -> None:
        async with async_client.agents.senders.with_streaming_response.connect(
            agent_id="agentId",
            sender_id="senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sender = await response.parse()
            assert_matches_type(SenderConnectResponse, sender, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_connect(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.senders.with_raw_response.connect(
                agent_id="",
                sender_id="senderId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_disconnect(self, async_client: AsyncZavudev) -> None:
        sender = await async_client.agents.senders.disconnect(
            sender_id="senderId",
            agent_id="agentId",
        )
        assert sender is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_disconnect(self, async_client: AsyncZavudev) -> None:
        response = await async_client.agents.senders.with_raw_response.disconnect(
            sender_id="senderId",
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sender = await response.parse()
        assert sender is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_disconnect(self, async_client: AsyncZavudev) -> None:
        async with async_client.agents.senders.with_streaming_response.disconnect(
            sender_id="senderId",
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sender = await response.parse()
            assert sender is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_disconnect(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.senders.with_raw_response.disconnect(
                sender_id="senderId",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            await async_client.agents.senders.with_raw_response.disconnect(
                sender_id="",
                agent_id="agentId",
            )
