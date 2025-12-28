# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from zavudev import Zavudev, AsyncZavudev
from tests.utils import assert_matches_type
from zavudev.pagination import SyncCursor, AsyncCursor
from zavudev.types.senders import AgentExecution

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExecutions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Zavudev) -> None:
        execution = client.senders.agent.executions.list(
            sender_id="senderId",
        )
        assert_matches_type(SyncCursor[AgentExecution], execution, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Zavudev) -> None:
        execution = client.senders.agent.executions.list(
            sender_id="senderId",
            cursor="cursor",
            limit=100,
            status="success",
        )
        assert_matches_type(SyncCursor[AgentExecution], execution, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Zavudev) -> None:
        response = client.senders.agent.executions.with_raw_response.list(
            sender_id="senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = response.parse()
        assert_matches_type(SyncCursor[AgentExecution], execution, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Zavudev) -> None:
        with client.senders.agent.executions.with_streaming_response.list(
            sender_id="senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = response.parse()
            assert_matches_type(SyncCursor[AgentExecution], execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            client.senders.agent.executions.with_raw_response.list(
                sender_id="",
            )


class TestAsyncExecutions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncZavudev) -> None:
        execution = await async_client.senders.agent.executions.list(
            sender_id="senderId",
        )
        assert_matches_type(AsyncCursor[AgentExecution], execution, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncZavudev) -> None:
        execution = await async_client.senders.agent.executions.list(
            sender_id="senderId",
            cursor="cursor",
            limit=100,
            status="success",
        )
        assert_matches_type(AsyncCursor[AgentExecution], execution, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncZavudev) -> None:
        response = await async_client.senders.agent.executions.with_raw_response.list(
            sender_id="senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = await response.parse()
        assert_matches_type(AsyncCursor[AgentExecution], execution, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncZavudev) -> None:
        async with async_client.senders.agent.executions.with_streaming_response.list(
            sender_id="senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = await response.parse()
            assert_matches_type(AsyncCursor[AgentExecution], execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            await async_client.senders.agent.executions.with_raw_response.list(
                sender_id="",
            )
