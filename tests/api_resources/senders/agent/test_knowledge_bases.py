# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from zavudev import Zavudev, AsyncZavudev
from tests.utils import assert_matches_type
from zavudev.pagination import SyncCursor, AsyncCursor
from zavudev.types.senders.agent import (
    AgentKnowledgeBase,
    KnowledgeBaseCreateResponse,
    KnowledgeBaseUpdateResponse,
    KnowledgeBaseRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKnowledgeBases:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Zavudev) -> None:
        knowledge_base = client.senders.agent.knowledge_bases.create(
            sender_id="senderId",
            name="Product FAQ",
        )
        assert_matches_type(KnowledgeBaseCreateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Zavudev) -> None:
        knowledge_base = client.senders.agent.knowledge_bases.create(
            sender_id="senderId",
            name="Product FAQ",
            description="Frequently asked questions about our products",
        )
        assert_matches_type(KnowledgeBaseCreateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Zavudev) -> None:
        response = client.senders.agent.knowledge_bases.with_raw_response.create(
            sender_id="senderId",
            name="Product FAQ",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = response.parse()
        assert_matches_type(KnowledgeBaseCreateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Zavudev) -> None:
        with client.senders.agent.knowledge_bases.with_streaming_response.create(
            sender_id="senderId",
            name="Product FAQ",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = response.parse()
            assert_matches_type(KnowledgeBaseCreateResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            client.senders.agent.knowledge_bases.with_raw_response.create(
                sender_id="",
                name="Product FAQ",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Zavudev) -> None:
        knowledge_base = client.senders.agent.knowledge_bases.retrieve(
            kb_id="kbId",
            sender_id="senderId",
        )
        assert_matches_type(KnowledgeBaseRetrieveResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Zavudev) -> None:
        response = client.senders.agent.knowledge_bases.with_raw_response.retrieve(
            kb_id="kbId",
            sender_id="senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = response.parse()
        assert_matches_type(KnowledgeBaseRetrieveResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Zavudev) -> None:
        with client.senders.agent.knowledge_bases.with_streaming_response.retrieve(
            kb_id="kbId",
            sender_id="senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = response.parse()
            assert_matches_type(KnowledgeBaseRetrieveResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            client.senders.agent.knowledge_bases.with_raw_response.retrieve(
                kb_id="kbId",
                sender_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `kb_id` but received ''"):
            client.senders.agent.knowledge_bases.with_raw_response.retrieve(
                kb_id="",
                sender_id="senderId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Zavudev) -> None:
        knowledge_base = client.senders.agent.knowledge_bases.update(
            kb_id="kbId",
            sender_id="senderId",
        )
        assert_matches_type(KnowledgeBaseUpdateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Zavudev) -> None:
        knowledge_base = client.senders.agent.knowledge_bases.update(
            kb_id="kbId",
            sender_id="senderId",
            description="description",
            name="name",
        )
        assert_matches_type(KnowledgeBaseUpdateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Zavudev) -> None:
        response = client.senders.agent.knowledge_bases.with_raw_response.update(
            kb_id="kbId",
            sender_id="senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = response.parse()
        assert_matches_type(KnowledgeBaseUpdateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Zavudev) -> None:
        with client.senders.agent.knowledge_bases.with_streaming_response.update(
            kb_id="kbId",
            sender_id="senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = response.parse()
            assert_matches_type(KnowledgeBaseUpdateResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            client.senders.agent.knowledge_bases.with_raw_response.update(
                kb_id="kbId",
                sender_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `kb_id` but received ''"):
            client.senders.agent.knowledge_bases.with_raw_response.update(
                kb_id="",
                sender_id="senderId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Zavudev) -> None:
        knowledge_base = client.senders.agent.knowledge_bases.list(
            sender_id="senderId",
        )
        assert_matches_type(SyncCursor[AgentKnowledgeBase], knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Zavudev) -> None:
        knowledge_base = client.senders.agent.knowledge_bases.list(
            sender_id="senderId",
            cursor="cursor",
            limit=100,
        )
        assert_matches_type(SyncCursor[AgentKnowledgeBase], knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Zavudev) -> None:
        response = client.senders.agent.knowledge_bases.with_raw_response.list(
            sender_id="senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = response.parse()
        assert_matches_type(SyncCursor[AgentKnowledgeBase], knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Zavudev) -> None:
        with client.senders.agent.knowledge_bases.with_streaming_response.list(
            sender_id="senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = response.parse()
            assert_matches_type(SyncCursor[AgentKnowledgeBase], knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            client.senders.agent.knowledge_bases.with_raw_response.list(
                sender_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Zavudev) -> None:
        knowledge_base = client.senders.agent.knowledge_bases.delete(
            kb_id="kbId",
            sender_id="senderId",
        )
        assert knowledge_base is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Zavudev) -> None:
        response = client.senders.agent.knowledge_bases.with_raw_response.delete(
            kb_id="kbId",
            sender_id="senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = response.parse()
        assert knowledge_base is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Zavudev) -> None:
        with client.senders.agent.knowledge_bases.with_streaming_response.delete(
            kb_id="kbId",
            sender_id="senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = response.parse()
            assert knowledge_base is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            client.senders.agent.knowledge_bases.with_raw_response.delete(
                kb_id="kbId",
                sender_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `kb_id` but received ''"):
            client.senders.agent.knowledge_bases.with_raw_response.delete(
                kb_id="",
                sender_id="senderId",
            )


class TestAsyncKnowledgeBases:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncZavudev) -> None:
        knowledge_base = await async_client.senders.agent.knowledge_bases.create(
            sender_id="senderId",
            name="Product FAQ",
        )
        assert_matches_type(KnowledgeBaseCreateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncZavudev) -> None:
        knowledge_base = await async_client.senders.agent.knowledge_bases.create(
            sender_id="senderId",
            name="Product FAQ",
            description="Frequently asked questions about our products",
        )
        assert_matches_type(KnowledgeBaseCreateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncZavudev) -> None:
        response = await async_client.senders.agent.knowledge_bases.with_raw_response.create(
            sender_id="senderId",
            name="Product FAQ",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = await response.parse()
        assert_matches_type(KnowledgeBaseCreateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncZavudev) -> None:
        async with async_client.senders.agent.knowledge_bases.with_streaming_response.create(
            sender_id="senderId",
            name="Product FAQ",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = await response.parse()
            assert_matches_type(KnowledgeBaseCreateResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            await async_client.senders.agent.knowledge_bases.with_raw_response.create(
                sender_id="",
                name="Product FAQ",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncZavudev) -> None:
        knowledge_base = await async_client.senders.agent.knowledge_bases.retrieve(
            kb_id="kbId",
            sender_id="senderId",
        )
        assert_matches_type(KnowledgeBaseRetrieveResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncZavudev) -> None:
        response = await async_client.senders.agent.knowledge_bases.with_raw_response.retrieve(
            kb_id="kbId",
            sender_id="senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = await response.parse()
        assert_matches_type(KnowledgeBaseRetrieveResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncZavudev) -> None:
        async with async_client.senders.agent.knowledge_bases.with_streaming_response.retrieve(
            kb_id="kbId",
            sender_id="senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = await response.parse()
            assert_matches_type(KnowledgeBaseRetrieveResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            await async_client.senders.agent.knowledge_bases.with_raw_response.retrieve(
                kb_id="kbId",
                sender_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `kb_id` but received ''"):
            await async_client.senders.agent.knowledge_bases.with_raw_response.retrieve(
                kb_id="",
                sender_id="senderId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncZavudev) -> None:
        knowledge_base = await async_client.senders.agent.knowledge_bases.update(
            kb_id="kbId",
            sender_id="senderId",
        )
        assert_matches_type(KnowledgeBaseUpdateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncZavudev) -> None:
        knowledge_base = await async_client.senders.agent.knowledge_bases.update(
            kb_id="kbId",
            sender_id="senderId",
            description="description",
            name="name",
        )
        assert_matches_type(KnowledgeBaseUpdateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncZavudev) -> None:
        response = await async_client.senders.agent.knowledge_bases.with_raw_response.update(
            kb_id="kbId",
            sender_id="senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = await response.parse()
        assert_matches_type(KnowledgeBaseUpdateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncZavudev) -> None:
        async with async_client.senders.agent.knowledge_bases.with_streaming_response.update(
            kb_id="kbId",
            sender_id="senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = await response.parse()
            assert_matches_type(KnowledgeBaseUpdateResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            await async_client.senders.agent.knowledge_bases.with_raw_response.update(
                kb_id="kbId",
                sender_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `kb_id` but received ''"):
            await async_client.senders.agent.knowledge_bases.with_raw_response.update(
                kb_id="",
                sender_id="senderId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncZavudev) -> None:
        knowledge_base = await async_client.senders.agent.knowledge_bases.list(
            sender_id="senderId",
        )
        assert_matches_type(AsyncCursor[AgentKnowledgeBase], knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncZavudev) -> None:
        knowledge_base = await async_client.senders.agent.knowledge_bases.list(
            sender_id="senderId",
            cursor="cursor",
            limit=100,
        )
        assert_matches_type(AsyncCursor[AgentKnowledgeBase], knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncZavudev) -> None:
        response = await async_client.senders.agent.knowledge_bases.with_raw_response.list(
            sender_id="senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = await response.parse()
        assert_matches_type(AsyncCursor[AgentKnowledgeBase], knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncZavudev) -> None:
        async with async_client.senders.agent.knowledge_bases.with_streaming_response.list(
            sender_id="senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = await response.parse()
            assert_matches_type(AsyncCursor[AgentKnowledgeBase], knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            await async_client.senders.agent.knowledge_bases.with_raw_response.list(
                sender_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncZavudev) -> None:
        knowledge_base = await async_client.senders.agent.knowledge_bases.delete(
            kb_id="kbId",
            sender_id="senderId",
        )
        assert knowledge_base is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncZavudev) -> None:
        response = await async_client.senders.agent.knowledge_bases.with_raw_response.delete(
            kb_id="kbId",
            sender_id="senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = await response.parse()
        assert knowledge_base is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncZavudev) -> None:
        async with async_client.senders.agent.knowledge_bases.with_streaming_response.delete(
            kb_id="kbId",
            sender_id="senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = await response.parse()
            assert knowledge_base is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            await async_client.senders.agent.knowledge_bases.with_raw_response.delete(
                kb_id="kbId",
                sender_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `kb_id` but received ''"):
            await async_client.senders.agent.knowledge_bases.with_raw_response.delete(
                kb_id="",
                sender_id="senderId",
            )
