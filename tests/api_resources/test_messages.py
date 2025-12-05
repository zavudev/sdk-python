# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from zavudev import Zavudev, AsyncZavudev
from tests.utils import assert_matches_type
from zavudev.types import (
    Message,
    MessageResponse,
)
from zavudev.pagination import SyncCursor, AsyncCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Zavudev) -> None:
        message = client.messages.retrieve(
            "messageId",
        )
        assert_matches_type(MessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Zavudev) -> None:
        response = client.messages.with_raw_response.retrieve(
            "messageId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Zavudev) -> None:
        with client.messages.with_streaming_response.retrieve(
            "messageId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.messages.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Zavudev) -> None:
        message = client.messages.list()
        assert_matches_type(SyncCursor[Message], message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Zavudev) -> None:
        message = client.messages.list(
            channel="auto",
            cursor="cursor",
            limit=100,
            status="queued",
            to="to",
        )
        assert_matches_type(SyncCursor[Message], message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Zavudev) -> None:
        response = client.messages.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(SyncCursor[Message], message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Zavudev) -> None:
        with client.messages.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(SyncCursor[Message], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_react(self, client: Zavudev) -> None:
        message = client.messages.react(
            message_id="messageId",
            emoji="👍",
        )
        assert_matches_type(MessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_react_with_all_params(self, client: Zavudev) -> None:
        message = client.messages.react(
            message_id="messageId",
            emoji="👍",
            zavu_sender="sender_12345",
        )
        assert_matches_type(MessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_react(self, client: Zavudev) -> None:
        response = client.messages.with_raw_response.react(
            message_id="messageId",
            emoji="👍",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_react(self, client: Zavudev) -> None:
        with client.messages.with_streaming_response.react(
            message_id="messageId",
            emoji="👍",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_react(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.messages.with_raw_response.react(
                message_id="",
                emoji="👍",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send(self, client: Zavudev) -> None:
        message = client.messages.send(
            to="+56912345678",
        )
        assert_matches_type(MessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_with_all_params(self, client: Zavudev) -> None:
        message = client.messages.send(
            to="+56912345678",
            channel="auto",
            content={
                "buttons": [
                    {
                        "id": "id",
                        "title": "title",
                    }
                ],
                "contacts": [
                    {
                        "name": "name",
                        "phones": ["string"],
                    }
                ],
                "emoji": "emoji",
                "filename": "invoice.pdf",
                "latitude": 0,
                "list_button": "listButton",
                "location_address": "locationAddress",
                "location_name": "locationName",
                "longitude": 0,
                "media_id": "mediaId",
                "media_url": "https://example.com/image.jpg",
                "mime_type": "image/jpeg",
                "react_to_message_id": "reactToMessageId",
                "sections": [
                    {
                        "rows": [
                            {
                                "id": "id",
                                "title": "title",
                                "description": "description",
                            }
                        ],
                        "title": "title",
                    }
                ],
                "template_id": "templateId",
                "template_variables": {
                    "1": "John",
                    "2": "ORD-12345",
                },
            },
            html_body="htmlBody",
            idempotency_key="msg_01HZY4ZP7VQY2J3BRW7Z6G0QGE",
            message_type="text",
            metadata={"foo": "string"},
            reply_to="support@example.com",
            subject="Your order confirmation",
            text="Your verification code is 123456",
            zavu_sender="sender_12345",
        )
        assert_matches_type(MessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_send(self, client: Zavudev) -> None:
        response = client.messages.with_raw_response.send(
            to="+56912345678",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_send(self, client: Zavudev) -> None:
        with client.messages.with_streaming_response.send(
            to="+56912345678",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncZavudev) -> None:
        message = await async_client.messages.retrieve(
            "messageId",
        )
        assert_matches_type(MessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncZavudev) -> None:
        response = await async_client.messages.with_raw_response.retrieve(
            "messageId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncZavudev) -> None:
        async with async_client.messages.with_streaming_response.retrieve(
            "messageId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.messages.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncZavudev) -> None:
        message = await async_client.messages.list()
        assert_matches_type(AsyncCursor[Message], message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncZavudev) -> None:
        message = await async_client.messages.list(
            channel="auto",
            cursor="cursor",
            limit=100,
            status="queued",
            to="to",
        )
        assert_matches_type(AsyncCursor[Message], message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncZavudev) -> None:
        response = await async_client.messages.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(AsyncCursor[Message], message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncZavudev) -> None:
        async with async_client.messages.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(AsyncCursor[Message], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_react(self, async_client: AsyncZavudev) -> None:
        message = await async_client.messages.react(
            message_id="messageId",
            emoji="👍",
        )
        assert_matches_type(MessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_react_with_all_params(self, async_client: AsyncZavudev) -> None:
        message = await async_client.messages.react(
            message_id="messageId",
            emoji="👍",
            zavu_sender="sender_12345",
        )
        assert_matches_type(MessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_react(self, async_client: AsyncZavudev) -> None:
        response = await async_client.messages.with_raw_response.react(
            message_id="messageId",
            emoji="👍",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_react(self, async_client: AsyncZavudev) -> None:
        async with async_client.messages.with_streaming_response.react(
            message_id="messageId",
            emoji="👍",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_react(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.messages.with_raw_response.react(
                message_id="",
                emoji="👍",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send(self, async_client: AsyncZavudev) -> None:
        message = await async_client.messages.send(
            to="+56912345678",
        )
        assert_matches_type(MessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_with_all_params(self, async_client: AsyncZavudev) -> None:
        message = await async_client.messages.send(
            to="+56912345678",
            channel="auto",
            content={
                "buttons": [
                    {
                        "id": "id",
                        "title": "title",
                    }
                ],
                "contacts": [
                    {
                        "name": "name",
                        "phones": ["string"],
                    }
                ],
                "emoji": "emoji",
                "filename": "invoice.pdf",
                "latitude": 0,
                "list_button": "listButton",
                "location_address": "locationAddress",
                "location_name": "locationName",
                "longitude": 0,
                "media_id": "mediaId",
                "media_url": "https://example.com/image.jpg",
                "mime_type": "image/jpeg",
                "react_to_message_id": "reactToMessageId",
                "sections": [
                    {
                        "rows": [
                            {
                                "id": "id",
                                "title": "title",
                                "description": "description",
                            }
                        ],
                        "title": "title",
                    }
                ],
                "template_id": "templateId",
                "template_variables": {
                    "1": "John",
                    "2": "ORD-12345",
                },
            },
            html_body="htmlBody",
            idempotency_key="msg_01HZY4ZP7VQY2J3BRW7Z6G0QGE",
            message_type="text",
            metadata={"foo": "string"},
            reply_to="support@example.com",
            subject="Your order confirmation",
            text="Your verification code is 123456",
            zavu_sender="sender_12345",
        )
        assert_matches_type(MessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_send(self, async_client: AsyncZavudev) -> None:
        response = await async_client.messages.with_raw_response.send(
            to="+56912345678",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncZavudev) -> None:
        async with async_client.messages.with_streaming_response.send(
            to="+56912345678",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True
