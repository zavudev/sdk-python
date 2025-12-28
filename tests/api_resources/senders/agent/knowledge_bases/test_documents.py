# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from zavudev import Zavudev, AsyncZavudev
from tests.utils import assert_matches_type
from zavudev.pagination import SyncCursor, AsyncCursor
from zavudev.types.senders.agent import AgentDocument
from zavudev.types.senders.agent.knowledge_bases import (
    DocumentCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDocuments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Zavudev) -> None:
        document = client.senders.agent.knowledge_bases.documents.create(
            kb_id="kbId",
            sender_id="senderId",
            content="Our return policy allows returns within 30 days of purchase...",
            title="Return Policy",
        )
        assert_matches_type(DocumentCreateResponse, document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Zavudev) -> None:
        response = client.senders.agent.knowledge_bases.documents.with_raw_response.create(
            kb_id="kbId",
            sender_id="senderId",
            content="Our return policy allows returns within 30 days of purchase...",
            title="Return Policy",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentCreateResponse, document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Zavudev) -> None:
        with client.senders.agent.knowledge_bases.documents.with_streaming_response.create(
            kb_id="kbId",
            sender_id="senderId",
            content="Our return policy allows returns within 30 days of purchase...",
            title="Return Policy",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentCreateResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            client.senders.agent.knowledge_bases.documents.with_raw_response.create(
                kb_id="kbId",
                sender_id="",
                content="Our return policy allows returns within 30 days of purchase...",
                title="Return Policy",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `kb_id` but received ''"):
            client.senders.agent.knowledge_bases.documents.with_raw_response.create(
                kb_id="",
                sender_id="senderId",
                content="Our return policy allows returns within 30 days of purchase...",
                title="Return Policy",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Zavudev) -> None:
        document = client.senders.agent.knowledge_bases.documents.list(
            kb_id="kbId",
            sender_id="senderId",
        )
        assert_matches_type(SyncCursor[AgentDocument], document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Zavudev) -> None:
        document = client.senders.agent.knowledge_bases.documents.list(
            kb_id="kbId",
            sender_id="senderId",
            cursor="cursor",
            limit=100,
        )
        assert_matches_type(SyncCursor[AgentDocument], document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Zavudev) -> None:
        response = client.senders.agent.knowledge_bases.documents.with_raw_response.list(
            kb_id="kbId",
            sender_id="senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(SyncCursor[AgentDocument], document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Zavudev) -> None:
        with client.senders.agent.knowledge_bases.documents.with_streaming_response.list(
            kb_id="kbId",
            sender_id="senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(SyncCursor[AgentDocument], document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            client.senders.agent.knowledge_bases.documents.with_raw_response.list(
                kb_id="kbId",
                sender_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `kb_id` but received ''"):
            client.senders.agent.knowledge_bases.documents.with_raw_response.list(
                kb_id="",
                sender_id="senderId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Zavudev) -> None:
        document = client.senders.agent.knowledge_bases.documents.delete(
            doc_id="docId",
            sender_id="senderId",
            kb_id="kbId",
        )
        assert document is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Zavudev) -> None:
        response = client.senders.agent.knowledge_bases.documents.with_raw_response.delete(
            doc_id="docId",
            sender_id="senderId",
            kb_id="kbId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert document is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Zavudev) -> None:
        with client.senders.agent.knowledge_bases.documents.with_streaming_response.delete(
            doc_id="docId",
            sender_id="senderId",
            kb_id="kbId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert document is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            client.senders.agent.knowledge_bases.documents.with_raw_response.delete(
                doc_id="docId",
                sender_id="",
                kb_id="kbId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `kb_id` but received ''"):
            client.senders.agent.knowledge_bases.documents.with_raw_response.delete(
                doc_id="docId",
                sender_id="senderId",
                kb_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `doc_id` but received ''"):
            client.senders.agent.knowledge_bases.documents.with_raw_response.delete(
                doc_id="",
                sender_id="senderId",
                kb_id="kbId",
            )


class TestAsyncDocuments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncZavudev) -> None:
        document = await async_client.senders.agent.knowledge_bases.documents.create(
            kb_id="kbId",
            sender_id="senderId",
            content="Our return policy allows returns within 30 days of purchase...",
            title="Return Policy",
        )
        assert_matches_type(DocumentCreateResponse, document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncZavudev) -> None:
        response = await async_client.senders.agent.knowledge_bases.documents.with_raw_response.create(
            kb_id="kbId",
            sender_id="senderId",
            content="Our return policy allows returns within 30 days of purchase...",
            title="Return Policy",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentCreateResponse, document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncZavudev) -> None:
        async with async_client.senders.agent.knowledge_bases.documents.with_streaming_response.create(
            kb_id="kbId",
            sender_id="senderId",
            content="Our return policy allows returns within 30 days of purchase...",
            title="Return Policy",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentCreateResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            await async_client.senders.agent.knowledge_bases.documents.with_raw_response.create(
                kb_id="kbId",
                sender_id="",
                content="Our return policy allows returns within 30 days of purchase...",
                title="Return Policy",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `kb_id` but received ''"):
            await async_client.senders.agent.knowledge_bases.documents.with_raw_response.create(
                kb_id="",
                sender_id="senderId",
                content="Our return policy allows returns within 30 days of purchase...",
                title="Return Policy",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncZavudev) -> None:
        document = await async_client.senders.agent.knowledge_bases.documents.list(
            kb_id="kbId",
            sender_id="senderId",
        )
        assert_matches_type(AsyncCursor[AgentDocument], document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncZavudev) -> None:
        document = await async_client.senders.agent.knowledge_bases.documents.list(
            kb_id="kbId",
            sender_id="senderId",
            cursor="cursor",
            limit=100,
        )
        assert_matches_type(AsyncCursor[AgentDocument], document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncZavudev) -> None:
        response = await async_client.senders.agent.knowledge_bases.documents.with_raw_response.list(
            kb_id="kbId",
            sender_id="senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(AsyncCursor[AgentDocument], document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncZavudev) -> None:
        async with async_client.senders.agent.knowledge_bases.documents.with_streaming_response.list(
            kb_id="kbId",
            sender_id="senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(AsyncCursor[AgentDocument], document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            await async_client.senders.agent.knowledge_bases.documents.with_raw_response.list(
                kb_id="kbId",
                sender_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `kb_id` but received ''"):
            await async_client.senders.agent.knowledge_bases.documents.with_raw_response.list(
                kb_id="",
                sender_id="senderId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncZavudev) -> None:
        document = await async_client.senders.agent.knowledge_bases.documents.delete(
            doc_id="docId",
            sender_id="senderId",
            kb_id="kbId",
        )
        assert document is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncZavudev) -> None:
        response = await async_client.senders.agent.knowledge_bases.documents.with_raw_response.delete(
            doc_id="docId",
            sender_id="senderId",
            kb_id="kbId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert document is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncZavudev) -> None:
        async with async_client.senders.agent.knowledge_bases.documents.with_streaming_response.delete(
            doc_id="docId",
            sender_id="senderId",
            kb_id="kbId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert document is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            await async_client.senders.agent.knowledge_bases.documents.with_raw_response.delete(
                doc_id="docId",
                sender_id="",
                kb_id="kbId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `kb_id` but received ''"):
            await async_client.senders.agent.knowledge_bases.documents.with_raw_response.delete(
                doc_id="docId",
                sender_id="senderId",
                kb_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `doc_id` but received ''"):
            await async_client.senders.agent.knowledge_bases.documents.with_raw_response.delete(
                doc_id="",
                sender_id="senderId",
                kb_id="kbId",
            )
