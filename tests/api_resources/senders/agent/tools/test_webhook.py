# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from zavudev import Zavudev, AsyncZavudev
from tests.utils import assert_matches_type
from zavudev.types import WebhookSecretResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhook:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rotate_secret(self, client: Zavudev) -> None:
        webhook = client.senders.agent.tools.webhook.rotate_secret(
            tool_id="toolId",
            sender_id="senderId",
        )
        assert_matches_type(WebhookSecretResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rotate_secret(self, client: Zavudev) -> None:
        response = client.senders.agent.tools.webhook.with_raw_response.rotate_secret(
            tool_id="toolId",
            sender_id="senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookSecretResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rotate_secret(self, client: Zavudev) -> None:
        with client.senders.agent.tools.webhook.with_streaming_response.rotate_secret(
            tool_id="toolId",
            sender_id="senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookSecretResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_rotate_secret(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            client.senders.agent.tools.webhook.with_raw_response.rotate_secret(
                tool_id="toolId",
                sender_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            client.senders.agent.tools.webhook.with_raw_response.rotate_secret(
                tool_id="",
                sender_id="senderId",
            )


class TestAsyncWebhook:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rotate_secret(self, async_client: AsyncZavudev) -> None:
        webhook = await async_client.senders.agent.tools.webhook.rotate_secret(
            tool_id="toolId",
            sender_id="senderId",
        )
        assert_matches_type(WebhookSecretResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rotate_secret(self, async_client: AsyncZavudev) -> None:
        response = await async_client.senders.agent.tools.webhook.with_raw_response.rotate_secret(
            tool_id="toolId",
            sender_id="senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookSecretResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rotate_secret(self, async_client: AsyncZavudev) -> None:
        async with async_client.senders.agent.tools.webhook.with_streaming_response.rotate_secret(
            tool_id="toolId",
            sender_id="senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookSecretResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_rotate_secret(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            await async_client.senders.agent.tools.webhook.with_raw_response.rotate_secret(
                tool_id="toolId",
                sender_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            await async_client.senders.agent.tools.webhook.with_raw_response.rotate_secret(
                tool_id="",
                sender_id="senderId",
            )
