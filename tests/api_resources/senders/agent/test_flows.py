# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from zavudev import Zavudev, AsyncZavudev
from tests.utils import assert_matches_type
from zavudev.pagination import SyncCursor, AsyncCursor
from zavudev.types.senders.agent import (
    AgentFlow,
    FlowCreateResponse,
    FlowUpdateResponse,
    FlowRetrieveResponse,
    FlowDuplicateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFlows:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Zavudev) -> None:
        flow = client.senders.agent.flows.create(
            sender_id="senderId",
            name="Lead Capture",
            steps=[
                {
                    "id": "welcome",
                    "config": {"text": "bar"},
                    "type": "message",
                },
                {
                    "id": "ask_name",
                    "config": {
                        "variable": "bar",
                        "prompt": "bar",
                    },
                    "type": "collect",
                },
            ],
            trigger={"type": "keyword"},
        )
        assert_matches_type(FlowCreateResponse, flow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Zavudev) -> None:
        flow = client.senders.agent.flows.create(
            sender_id="senderId",
            name="Lead Capture",
            steps=[
                {
                    "id": "welcome",
                    "config": {"text": "bar"},
                    "type": "message",
                    "next_step_id": "ask_name",
                },
                {
                    "id": "ask_name",
                    "config": {
                        "variable": "bar",
                        "prompt": "bar",
                    },
                    "type": "collect",
                    "next_step_id": "nextStepId",
                },
            ],
            trigger={
                "type": "keyword",
                "intent": "intent",
                "keywords": ["info", "pricing", "demo"],
            },
            description="Capture lead information",
            enabled=True,
            priority=0,
        )
        assert_matches_type(FlowCreateResponse, flow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Zavudev) -> None:
        response = client.senders.agent.flows.with_raw_response.create(
            sender_id="senderId",
            name="Lead Capture",
            steps=[
                {
                    "id": "welcome",
                    "config": {"text": "bar"},
                    "type": "message",
                },
                {
                    "id": "ask_name",
                    "config": {
                        "variable": "bar",
                        "prompt": "bar",
                    },
                    "type": "collect",
                },
            ],
            trigger={"type": "keyword"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flow = response.parse()
        assert_matches_type(FlowCreateResponse, flow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Zavudev) -> None:
        with client.senders.agent.flows.with_streaming_response.create(
            sender_id="senderId",
            name="Lead Capture",
            steps=[
                {
                    "id": "welcome",
                    "config": {"text": "bar"},
                    "type": "message",
                },
                {
                    "id": "ask_name",
                    "config": {
                        "variable": "bar",
                        "prompt": "bar",
                    },
                    "type": "collect",
                },
            ],
            trigger={"type": "keyword"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flow = response.parse()
            assert_matches_type(FlowCreateResponse, flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            client.senders.agent.flows.with_raw_response.create(
                sender_id="",
                name="Lead Capture",
                steps=[
                    {
                        "id": "welcome",
                        "config": {"text": "bar"},
                        "type": "message",
                    },
                    {
                        "id": "ask_name",
                        "config": {
                            "variable": "bar",
                            "prompt": "bar",
                        },
                        "type": "collect",
                    },
                ],
                trigger={"type": "keyword"},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Zavudev) -> None:
        flow = client.senders.agent.flows.retrieve(
            flow_id="flowId",
            sender_id="senderId",
        )
        assert_matches_type(FlowRetrieveResponse, flow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Zavudev) -> None:
        response = client.senders.agent.flows.with_raw_response.retrieve(
            flow_id="flowId",
            sender_id="senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flow = response.parse()
        assert_matches_type(FlowRetrieveResponse, flow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Zavudev) -> None:
        with client.senders.agent.flows.with_streaming_response.retrieve(
            flow_id="flowId",
            sender_id="senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flow = response.parse()
            assert_matches_type(FlowRetrieveResponse, flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            client.senders.agent.flows.with_raw_response.retrieve(
                flow_id="flowId",
                sender_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            client.senders.agent.flows.with_raw_response.retrieve(
                flow_id="",
                sender_id="senderId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Zavudev) -> None:
        flow = client.senders.agent.flows.update(
            flow_id="flowId",
            sender_id="senderId",
        )
        assert_matches_type(FlowUpdateResponse, flow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Zavudev) -> None:
        flow = client.senders.agent.flows.update(
            flow_id="flowId",
            sender_id="senderId",
            description="description",
            enabled=True,
            name="name",
            priority=0,
            steps=[
                {
                    "id": "id",
                    "config": {"foo": "bar"},
                    "type": "message",
                    "next_step_id": "nextStepId",
                }
            ],
            trigger={
                "type": "keyword",
                "intent": "intent",
                "keywords": ["string"],
            },
        )
        assert_matches_type(FlowUpdateResponse, flow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Zavudev) -> None:
        response = client.senders.agent.flows.with_raw_response.update(
            flow_id="flowId",
            sender_id="senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flow = response.parse()
        assert_matches_type(FlowUpdateResponse, flow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Zavudev) -> None:
        with client.senders.agent.flows.with_streaming_response.update(
            flow_id="flowId",
            sender_id="senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flow = response.parse()
            assert_matches_type(FlowUpdateResponse, flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            client.senders.agent.flows.with_raw_response.update(
                flow_id="flowId",
                sender_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            client.senders.agent.flows.with_raw_response.update(
                flow_id="",
                sender_id="senderId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Zavudev) -> None:
        flow = client.senders.agent.flows.list(
            sender_id="senderId",
        )
        assert_matches_type(SyncCursor[AgentFlow], flow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Zavudev) -> None:
        flow = client.senders.agent.flows.list(
            sender_id="senderId",
            cursor="cursor",
            enabled=True,
            limit=100,
        )
        assert_matches_type(SyncCursor[AgentFlow], flow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Zavudev) -> None:
        response = client.senders.agent.flows.with_raw_response.list(
            sender_id="senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flow = response.parse()
        assert_matches_type(SyncCursor[AgentFlow], flow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Zavudev) -> None:
        with client.senders.agent.flows.with_streaming_response.list(
            sender_id="senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flow = response.parse()
            assert_matches_type(SyncCursor[AgentFlow], flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            client.senders.agent.flows.with_raw_response.list(
                sender_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Zavudev) -> None:
        flow = client.senders.agent.flows.delete(
            flow_id="flowId",
            sender_id="senderId",
        )
        assert flow is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Zavudev) -> None:
        response = client.senders.agent.flows.with_raw_response.delete(
            flow_id="flowId",
            sender_id="senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flow = response.parse()
        assert flow is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Zavudev) -> None:
        with client.senders.agent.flows.with_streaming_response.delete(
            flow_id="flowId",
            sender_id="senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flow = response.parse()
            assert flow is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            client.senders.agent.flows.with_raw_response.delete(
                flow_id="flowId",
                sender_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            client.senders.agent.flows.with_raw_response.delete(
                flow_id="",
                sender_id="senderId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_duplicate(self, client: Zavudev) -> None:
        flow = client.senders.agent.flows.duplicate(
            flow_id="flowId",
            sender_id="senderId",
            new_name="Lead Capture (Copy)",
        )
        assert_matches_type(FlowDuplicateResponse, flow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_duplicate(self, client: Zavudev) -> None:
        response = client.senders.agent.flows.with_raw_response.duplicate(
            flow_id="flowId",
            sender_id="senderId",
            new_name="Lead Capture (Copy)",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flow = response.parse()
        assert_matches_type(FlowDuplicateResponse, flow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_duplicate(self, client: Zavudev) -> None:
        with client.senders.agent.flows.with_streaming_response.duplicate(
            flow_id="flowId",
            sender_id="senderId",
            new_name="Lead Capture (Copy)",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flow = response.parse()
            assert_matches_type(FlowDuplicateResponse, flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_duplicate(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            client.senders.agent.flows.with_raw_response.duplicate(
                flow_id="flowId",
                sender_id="",
                new_name="Lead Capture (Copy)",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            client.senders.agent.flows.with_raw_response.duplicate(
                flow_id="",
                sender_id="senderId",
                new_name="Lead Capture (Copy)",
            )


class TestAsyncFlows:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncZavudev) -> None:
        flow = await async_client.senders.agent.flows.create(
            sender_id="senderId",
            name="Lead Capture",
            steps=[
                {
                    "id": "welcome",
                    "config": {"text": "bar"},
                    "type": "message",
                },
                {
                    "id": "ask_name",
                    "config": {
                        "variable": "bar",
                        "prompt": "bar",
                    },
                    "type": "collect",
                },
            ],
            trigger={"type": "keyword"},
        )
        assert_matches_type(FlowCreateResponse, flow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncZavudev) -> None:
        flow = await async_client.senders.agent.flows.create(
            sender_id="senderId",
            name="Lead Capture",
            steps=[
                {
                    "id": "welcome",
                    "config": {"text": "bar"},
                    "type": "message",
                    "next_step_id": "ask_name",
                },
                {
                    "id": "ask_name",
                    "config": {
                        "variable": "bar",
                        "prompt": "bar",
                    },
                    "type": "collect",
                    "next_step_id": "nextStepId",
                },
            ],
            trigger={
                "type": "keyword",
                "intent": "intent",
                "keywords": ["info", "pricing", "demo"],
            },
            description="Capture lead information",
            enabled=True,
            priority=0,
        )
        assert_matches_type(FlowCreateResponse, flow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncZavudev) -> None:
        response = await async_client.senders.agent.flows.with_raw_response.create(
            sender_id="senderId",
            name="Lead Capture",
            steps=[
                {
                    "id": "welcome",
                    "config": {"text": "bar"},
                    "type": "message",
                },
                {
                    "id": "ask_name",
                    "config": {
                        "variable": "bar",
                        "prompt": "bar",
                    },
                    "type": "collect",
                },
            ],
            trigger={"type": "keyword"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flow = await response.parse()
        assert_matches_type(FlowCreateResponse, flow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncZavudev) -> None:
        async with async_client.senders.agent.flows.with_streaming_response.create(
            sender_id="senderId",
            name="Lead Capture",
            steps=[
                {
                    "id": "welcome",
                    "config": {"text": "bar"},
                    "type": "message",
                },
                {
                    "id": "ask_name",
                    "config": {
                        "variable": "bar",
                        "prompt": "bar",
                    },
                    "type": "collect",
                },
            ],
            trigger={"type": "keyword"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flow = await response.parse()
            assert_matches_type(FlowCreateResponse, flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            await async_client.senders.agent.flows.with_raw_response.create(
                sender_id="",
                name="Lead Capture",
                steps=[
                    {
                        "id": "welcome",
                        "config": {"text": "bar"},
                        "type": "message",
                    },
                    {
                        "id": "ask_name",
                        "config": {
                            "variable": "bar",
                            "prompt": "bar",
                        },
                        "type": "collect",
                    },
                ],
                trigger={"type": "keyword"},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncZavudev) -> None:
        flow = await async_client.senders.agent.flows.retrieve(
            flow_id="flowId",
            sender_id="senderId",
        )
        assert_matches_type(FlowRetrieveResponse, flow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncZavudev) -> None:
        response = await async_client.senders.agent.flows.with_raw_response.retrieve(
            flow_id="flowId",
            sender_id="senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flow = await response.parse()
        assert_matches_type(FlowRetrieveResponse, flow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncZavudev) -> None:
        async with async_client.senders.agent.flows.with_streaming_response.retrieve(
            flow_id="flowId",
            sender_id="senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flow = await response.parse()
            assert_matches_type(FlowRetrieveResponse, flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            await async_client.senders.agent.flows.with_raw_response.retrieve(
                flow_id="flowId",
                sender_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            await async_client.senders.agent.flows.with_raw_response.retrieve(
                flow_id="",
                sender_id="senderId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncZavudev) -> None:
        flow = await async_client.senders.agent.flows.update(
            flow_id="flowId",
            sender_id="senderId",
        )
        assert_matches_type(FlowUpdateResponse, flow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncZavudev) -> None:
        flow = await async_client.senders.agent.flows.update(
            flow_id="flowId",
            sender_id="senderId",
            description="description",
            enabled=True,
            name="name",
            priority=0,
            steps=[
                {
                    "id": "id",
                    "config": {"foo": "bar"},
                    "type": "message",
                    "next_step_id": "nextStepId",
                }
            ],
            trigger={
                "type": "keyword",
                "intent": "intent",
                "keywords": ["string"],
            },
        )
        assert_matches_type(FlowUpdateResponse, flow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncZavudev) -> None:
        response = await async_client.senders.agent.flows.with_raw_response.update(
            flow_id="flowId",
            sender_id="senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flow = await response.parse()
        assert_matches_type(FlowUpdateResponse, flow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncZavudev) -> None:
        async with async_client.senders.agent.flows.with_streaming_response.update(
            flow_id="flowId",
            sender_id="senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flow = await response.parse()
            assert_matches_type(FlowUpdateResponse, flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            await async_client.senders.agent.flows.with_raw_response.update(
                flow_id="flowId",
                sender_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            await async_client.senders.agent.flows.with_raw_response.update(
                flow_id="",
                sender_id="senderId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncZavudev) -> None:
        flow = await async_client.senders.agent.flows.list(
            sender_id="senderId",
        )
        assert_matches_type(AsyncCursor[AgentFlow], flow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncZavudev) -> None:
        flow = await async_client.senders.agent.flows.list(
            sender_id="senderId",
            cursor="cursor",
            enabled=True,
            limit=100,
        )
        assert_matches_type(AsyncCursor[AgentFlow], flow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncZavudev) -> None:
        response = await async_client.senders.agent.flows.with_raw_response.list(
            sender_id="senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flow = await response.parse()
        assert_matches_type(AsyncCursor[AgentFlow], flow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncZavudev) -> None:
        async with async_client.senders.agent.flows.with_streaming_response.list(
            sender_id="senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flow = await response.parse()
            assert_matches_type(AsyncCursor[AgentFlow], flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            await async_client.senders.agent.flows.with_raw_response.list(
                sender_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncZavudev) -> None:
        flow = await async_client.senders.agent.flows.delete(
            flow_id="flowId",
            sender_id="senderId",
        )
        assert flow is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncZavudev) -> None:
        response = await async_client.senders.agent.flows.with_raw_response.delete(
            flow_id="flowId",
            sender_id="senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flow = await response.parse()
        assert flow is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncZavudev) -> None:
        async with async_client.senders.agent.flows.with_streaming_response.delete(
            flow_id="flowId",
            sender_id="senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flow = await response.parse()
            assert flow is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            await async_client.senders.agent.flows.with_raw_response.delete(
                flow_id="flowId",
                sender_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            await async_client.senders.agent.flows.with_raw_response.delete(
                flow_id="",
                sender_id="senderId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_duplicate(self, async_client: AsyncZavudev) -> None:
        flow = await async_client.senders.agent.flows.duplicate(
            flow_id="flowId",
            sender_id="senderId",
            new_name="Lead Capture (Copy)",
        )
        assert_matches_type(FlowDuplicateResponse, flow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_duplicate(self, async_client: AsyncZavudev) -> None:
        response = await async_client.senders.agent.flows.with_raw_response.duplicate(
            flow_id="flowId",
            sender_id="senderId",
            new_name="Lead Capture (Copy)",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flow = await response.parse()
        assert_matches_type(FlowDuplicateResponse, flow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_duplicate(self, async_client: AsyncZavudev) -> None:
        async with async_client.senders.agent.flows.with_streaming_response.duplicate(
            flow_id="flowId",
            sender_id="senderId",
            new_name="Lead Capture (Copy)",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flow = await response.parse()
            assert_matches_type(FlowDuplicateResponse, flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_duplicate(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            await async_client.senders.agent.flows.with_raw_response.duplicate(
                flow_id="flowId",
                sender_id="",
                new_name="Lead Capture (Copy)",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            await async_client.senders.agent.flows.with_raw_response.duplicate(
                flow_id="",
                sender_id="senderId",
                new_name="Lead Capture (Copy)",
            )
