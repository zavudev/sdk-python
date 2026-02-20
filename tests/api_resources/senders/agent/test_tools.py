# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from zavudev import Zavudev, AsyncZavudev
from tests.utils import assert_matches_type
from zavudev.pagination import SyncCursor, AsyncCursor
from zavudev.types.senders.agent import (
    AgentTool,
    ToolTestResponse,
    ToolCreateResponse,
    ToolUpdateResponse,
    ToolRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTools:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Zavudev) -> None:
        tool = client.senders.agent.tools.create(
            sender_id="senderId",
            description="Get the status of a customer order",
            name="get_order_status",
            parameters={
                "properties": {"order_id": {}},
                "required": ["order_id"],
                "type": "object",
            },
            webhook_url="https://api.example.com/webhooks/order-status",
        )
        assert_matches_type(ToolCreateResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Zavudev) -> None:
        tool = client.senders.agent.tools.create(
            sender_id="senderId",
            description="Get the status of a customer order",
            name="get_order_status",
            parameters={
                "properties": {
                    "order_id": {
                        "description": "The order ID to look up",
                        "type": "string",
                    }
                },
                "required": ["order_id"],
                "type": "object",
            },
            webhook_url="https://api.example.com/webhooks/order-status",
            enabled=True,
            webhook_secret="whsec_...",
        )
        assert_matches_type(ToolCreateResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Zavudev) -> None:
        response = client.senders.agent.tools.with_raw_response.create(
            sender_id="senderId",
            description="Get the status of a customer order",
            name="get_order_status",
            parameters={
                "properties": {"order_id": {}},
                "required": ["order_id"],
                "type": "object",
            },
            webhook_url="https://api.example.com/webhooks/order-status",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolCreateResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Zavudev) -> None:
        with client.senders.agent.tools.with_streaming_response.create(
            sender_id="senderId",
            description="Get the status of a customer order",
            name="get_order_status",
            parameters={
                "properties": {"order_id": {}},
                "required": ["order_id"],
                "type": "object",
            },
            webhook_url="https://api.example.com/webhooks/order-status",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolCreateResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            client.senders.agent.tools.with_raw_response.create(
                sender_id="",
                description="Get the status of a customer order",
                name="get_order_status",
                parameters={
                    "properties": {"order_id": {}},
                    "required": ["order_id"],
                    "type": "object",
                },
                webhook_url="https://api.example.com/webhooks/order-status",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Zavudev) -> None:
        tool = client.senders.agent.tools.retrieve(
            tool_id="toolId",
            sender_id="senderId",
        )
        assert_matches_type(ToolRetrieveResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Zavudev) -> None:
        response = client.senders.agent.tools.with_raw_response.retrieve(
            tool_id="toolId",
            sender_id="senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolRetrieveResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Zavudev) -> None:
        with client.senders.agent.tools.with_streaming_response.retrieve(
            tool_id="toolId",
            sender_id="senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolRetrieveResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            client.senders.agent.tools.with_raw_response.retrieve(
                tool_id="toolId",
                sender_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            client.senders.agent.tools.with_raw_response.retrieve(
                tool_id="",
                sender_id="senderId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Zavudev) -> None:
        tool = client.senders.agent.tools.update(
            tool_id="toolId",
            sender_id="senderId",
        )
        assert_matches_type(ToolUpdateResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Zavudev) -> None:
        tool = client.senders.agent.tools.update(
            tool_id="toolId",
            sender_id="senderId",
            description="description",
            enabled=True,
            name="name",
            parameters={
                "properties": {
                    "foo": {
                        "description": "description",
                        "type": "type",
                    }
                },
                "required": ["string"],
                "type": "object",
            },
            webhook_secret="webhookSecret",
            webhook_url="https://example.com",
        )
        assert_matches_type(ToolUpdateResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Zavudev) -> None:
        response = client.senders.agent.tools.with_raw_response.update(
            tool_id="toolId",
            sender_id="senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolUpdateResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Zavudev) -> None:
        with client.senders.agent.tools.with_streaming_response.update(
            tool_id="toolId",
            sender_id="senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolUpdateResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            client.senders.agent.tools.with_raw_response.update(
                tool_id="toolId",
                sender_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            client.senders.agent.tools.with_raw_response.update(
                tool_id="",
                sender_id="senderId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Zavudev) -> None:
        tool = client.senders.agent.tools.list(
            sender_id="senderId",
        )
        assert_matches_type(SyncCursor[AgentTool], tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Zavudev) -> None:
        tool = client.senders.agent.tools.list(
            sender_id="senderId",
            cursor="cursor",
            enabled=True,
            limit=100,
        )
        assert_matches_type(SyncCursor[AgentTool], tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Zavudev) -> None:
        response = client.senders.agent.tools.with_raw_response.list(
            sender_id="senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(SyncCursor[AgentTool], tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Zavudev) -> None:
        with client.senders.agent.tools.with_streaming_response.list(
            sender_id="senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(SyncCursor[AgentTool], tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            client.senders.agent.tools.with_raw_response.list(
                sender_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Zavudev) -> None:
        tool = client.senders.agent.tools.delete(
            tool_id="toolId",
            sender_id="senderId",
        )
        assert tool is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Zavudev) -> None:
        response = client.senders.agent.tools.with_raw_response.delete(
            tool_id="toolId",
            sender_id="senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert tool is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Zavudev) -> None:
        with client.senders.agent.tools.with_streaming_response.delete(
            tool_id="toolId",
            sender_id="senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert tool is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            client.senders.agent.tools.with_raw_response.delete(
                tool_id="toolId",
                sender_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            client.senders.agent.tools.with_raw_response.delete(
                tool_id="",
                sender_id="senderId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_test(self, client: Zavudev) -> None:
        tool = client.senders.agent.tools.test(
            tool_id="toolId",
            sender_id="senderId",
            test_params={"order_id": "bar"},
        )
        assert_matches_type(ToolTestResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_test(self, client: Zavudev) -> None:
        response = client.senders.agent.tools.with_raw_response.test(
            tool_id="toolId",
            sender_id="senderId",
            test_params={"order_id": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolTestResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_test(self, client: Zavudev) -> None:
        with client.senders.agent.tools.with_streaming_response.test(
            tool_id="toolId",
            sender_id="senderId",
            test_params={"order_id": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolTestResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_test(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            client.senders.agent.tools.with_raw_response.test(
                tool_id="toolId",
                sender_id="",
                test_params={"order_id": "bar"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            client.senders.agent.tools.with_raw_response.test(
                tool_id="",
                sender_id="senderId",
                test_params={"order_id": "bar"},
            )


class TestAsyncTools:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncZavudev) -> None:
        tool = await async_client.senders.agent.tools.create(
            sender_id="senderId",
            description="Get the status of a customer order",
            name="get_order_status",
            parameters={
                "properties": {"order_id": {}},
                "required": ["order_id"],
                "type": "object",
            },
            webhook_url="https://api.example.com/webhooks/order-status",
        )
        assert_matches_type(ToolCreateResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncZavudev) -> None:
        tool = await async_client.senders.agent.tools.create(
            sender_id="senderId",
            description="Get the status of a customer order",
            name="get_order_status",
            parameters={
                "properties": {
                    "order_id": {
                        "description": "The order ID to look up",
                        "type": "string",
                    }
                },
                "required": ["order_id"],
                "type": "object",
            },
            webhook_url="https://api.example.com/webhooks/order-status",
            enabled=True,
            webhook_secret="whsec_...",
        )
        assert_matches_type(ToolCreateResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncZavudev) -> None:
        response = await async_client.senders.agent.tools.with_raw_response.create(
            sender_id="senderId",
            description="Get the status of a customer order",
            name="get_order_status",
            parameters={
                "properties": {"order_id": {}},
                "required": ["order_id"],
                "type": "object",
            },
            webhook_url="https://api.example.com/webhooks/order-status",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolCreateResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncZavudev) -> None:
        async with async_client.senders.agent.tools.with_streaming_response.create(
            sender_id="senderId",
            description="Get the status of a customer order",
            name="get_order_status",
            parameters={
                "properties": {"order_id": {}},
                "required": ["order_id"],
                "type": "object",
            },
            webhook_url="https://api.example.com/webhooks/order-status",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolCreateResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            await async_client.senders.agent.tools.with_raw_response.create(
                sender_id="",
                description="Get the status of a customer order",
                name="get_order_status",
                parameters={
                    "properties": {"order_id": {}},
                    "required": ["order_id"],
                    "type": "object",
                },
                webhook_url="https://api.example.com/webhooks/order-status",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncZavudev) -> None:
        tool = await async_client.senders.agent.tools.retrieve(
            tool_id="toolId",
            sender_id="senderId",
        )
        assert_matches_type(ToolRetrieveResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncZavudev) -> None:
        response = await async_client.senders.agent.tools.with_raw_response.retrieve(
            tool_id="toolId",
            sender_id="senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolRetrieveResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncZavudev) -> None:
        async with async_client.senders.agent.tools.with_streaming_response.retrieve(
            tool_id="toolId",
            sender_id="senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolRetrieveResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            await async_client.senders.agent.tools.with_raw_response.retrieve(
                tool_id="toolId",
                sender_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            await async_client.senders.agent.tools.with_raw_response.retrieve(
                tool_id="",
                sender_id="senderId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncZavudev) -> None:
        tool = await async_client.senders.agent.tools.update(
            tool_id="toolId",
            sender_id="senderId",
        )
        assert_matches_type(ToolUpdateResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncZavudev) -> None:
        tool = await async_client.senders.agent.tools.update(
            tool_id="toolId",
            sender_id="senderId",
            description="description",
            enabled=True,
            name="name",
            parameters={
                "properties": {
                    "foo": {
                        "description": "description",
                        "type": "type",
                    }
                },
                "required": ["string"],
                "type": "object",
            },
            webhook_secret="webhookSecret",
            webhook_url="https://example.com",
        )
        assert_matches_type(ToolUpdateResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncZavudev) -> None:
        response = await async_client.senders.agent.tools.with_raw_response.update(
            tool_id="toolId",
            sender_id="senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolUpdateResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncZavudev) -> None:
        async with async_client.senders.agent.tools.with_streaming_response.update(
            tool_id="toolId",
            sender_id="senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolUpdateResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            await async_client.senders.agent.tools.with_raw_response.update(
                tool_id="toolId",
                sender_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            await async_client.senders.agent.tools.with_raw_response.update(
                tool_id="",
                sender_id="senderId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncZavudev) -> None:
        tool = await async_client.senders.agent.tools.list(
            sender_id="senderId",
        )
        assert_matches_type(AsyncCursor[AgentTool], tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncZavudev) -> None:
        tool = await async_client.senders.agent.tools.list(
            sender_id="senderId",
            cursor="cursor",
            enabled=True,
            limit=100,
        )
        assert_matches_type(AsyncCursor[AgentTool], tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncZavudev) -> None:
        response = await async_client.senders.agent.tools.with_raw_response.list(
            sender_id="senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(AsyncCursor[AgentTool], tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncZavudev) -> None:
        async with async_client.senders.agent.tools.with_streaming_response.list(
            sender_id="senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(AsyncCursor[AgentTool], tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            await async_client.senders.agent.tools.with_raw_response.list(
                sender_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncZavudev) -> None:
        tool = await async_client.senders.agent.tools.delete(
            tool_id="toolId",
            sender_id="senderId",
        )
        assert tool is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncZavudev) -> None:
        response = await async_client.senders.agent.tools.with_raw_response.delete(
            tool_id="toolId",
            sender_id="senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert tool is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncZavudev) -> None:
        async with async_client.senders.agent.tools.with_streaming_response.delete(
            tool_id="toolId",
            sender_id="senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert tool is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            await async_client.senders.agent.tools.with_raw_response.delete(
                tool_id="toolId",
                sender_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            await async_client.senders.agent.tools.with_raw_response.delete(
                tool_id="",
                sender_id="senderId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_test(self, async_client: AsyncZavudev) -> None:
        tool = await async_client.senders.agent.tools.test(
            tool_id="toolId",
            sender_id="senderId",
            test_params={"order_id": "bar"},
        )
        assert_matches_type(ToolTestResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_test(self, async_client: AsyncZavudev) -> None:
        response = await async_client.senders.agent.tools.with_raw_response.test(
            tool_id="toolId",
            sender_id="senderId",
            test_params={"order_id": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolTestResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_test(self, async_client: AsyncZavudev) -> None:
        async with async_client.senders.agent.tools.with_streaming_response.test(
            tool_id="toolId",
            sender_id="senderId",
            test_params={"order_id": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolTestResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_test(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            await async_client.senders.agent.tools.with_raw_response.test(
                tool_id="toolId",
                sender_id="",
                test_params={"order_id": "bar"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            await async_client.senders.agent.tools.with_raw_response.test(
                tool_id="",
                sender_id="senderId",
                test_params={"order_id": "bar"},
            )
