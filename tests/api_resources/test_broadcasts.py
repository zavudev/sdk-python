# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from zavudev import Zavudev, AsyncZavudev
from tests.utils import assert_matches_type
from zavudev.types import (
    Broadcast,
    BroadcastProgress,
    BroadcastSendResponse,
    BroadcastCancelResponse,
    BroadcastCreateResponse,
    BroadcastUpdateResponse,
    BroadcastRetrieveResponse,
    BroadcastRescheduleResponse,
)
from zavudev._utils import parse_datetime
from zavudev.pagination import SyncCursor, AsyncCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBroadcasts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Zavudev) -> None:
        broadcast = client.broadcasts.create(
            channel="sms",
            name="Black Friday Sale",
        )
        assert_matches_type(BroadcastCreateResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Zavudev) -> None:
        broadcast = client.broadcasts.create(
            channel="sms",
            name="Black Friday Sale",
            content={
                "filename": "filename",
                "media_id": "mediaId",
                "media_url": "mediaUrl",
                "mime_type": "mimeType",
                "template_id": "templateId",
                "template_variables": {"foo": "string"},
            },
            email_html_body="emailHtmlBody",
            email_subject="emailSubject",
            idempotency_key="idempotencyKey",
            message_type="text",
            metadata={"foo": "string"},
            scheduled_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            sender_id="senderId",
            text="Hi {{name}}, check out our Black Friday deals! Use code FRIDAY20 for 20% off.",
        )
        assert_matches_type(BroadcastCreateResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Zavudev) -> None:
        response = client.broadcasts.with_raw_response.create(
            channel="sms",
            name="Black Friday Sale",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = response.parse()
        assert_matches_type(BroadcastCreateResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Zavudev) -> None:
        with client.broadcasts.with_streaming_response.create(
            channel="sms",
            name="Black Friday Sale",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = response.parse()
            assert_matches_type(BroadcastCreateResponse, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Zavudev) -> None:
        broadcast = client.broadcasts.retrieve(
            "broadcastId",
        )
        assert_matches_type(BroadcastRetrieveResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Zavudev) -> None:
        response = client.broadcasts.with_raw_response.retrieve(
            "broadcastId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = response.parse()
        assert_matches_type(BroadcastRetrieveResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Zavudev) -> None:
        with client.broadcasts.with_streaming_response.retrieve(
            "broadcastId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = response.parse()
            assert_matches_type(BroadcastRetrieveResponse, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            client.broadcasts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Zavudev) -> None:
        broadcast = client.broadcasts.update(
            broadcast_id="broadcastId",
        )
        assert_matches_type(BroadcastUpdateResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Zavudev) -> None:
        broadcast = client.broadcasts.update(
            broadcast_id="broadcastId",
            content={
                "filename": "filename",
                "media_id": "mediaId",
                "media_url": "mediaUrl",
                "mime_type": "mimeType",
                "template_id": "templateId",
                "template_variables": {"foo": "string"},
            },
            email_html_body="emailHtmlBody",
            email_subject="emailSubject",
            metadata={"foo": "string"},
            name="name",
            text="text",
        )
        assert_matches_type(BroadcastUpdateResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Zavudev) -> None:
        response = client.broadcasts.with_raw_response.update(
            broadcast_id="broadcastId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = response.parse()
        assert_matches_type(BroadcastUpdateResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Zavudev) -> None:
        with client.broadcasts.with_streaming_response.update(
            broadcast_id="broadcastId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = response.parse()
            assert_matches_type(BroadcastUpdateResponse, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            client.broadcasts.with_raw_response.update(
                broadcast_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Zavudev) -> None:
        broadcast = client.broadcasts.list()
        assert_matches_type(SyncCursor[Broadcast], broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Zavudev) -> None:
        broadcast = client.broadcasts.list(
            cursor="cursor",
            limit=100,
            status="draft",
        )
        assert_matches_type(SyncCursor[Broadcast], broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Zavudev) -> None:
        response = client.broadcasts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = response.parse()
        assert_matches_type(SyncCursor[Broadcast], broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Zavudev) -> None:
        with client.broadcasts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = response.parse()
            assert_matches_type(SyncCursor[Broadcast], broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Zavudev) -> None:
        broadcast = client.broadcasts.delete(
            "broadcastId",
        )
        assert broadcast is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Zavudev) -> None:
        response = client.broadcasts.with_raw_response.delete(
            "broadcastId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = response.parse()
        assert broadcast is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Zavudev) -> None:
        with client.broadcasts.with_streaming_response.delete(
            "broadcastId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = response.parse()
            assert broadcast is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            client.broadcasts.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel(self, client: Zavudev) -> None:
        broadcast = client.broadcasts.cancel(
            "broadcastId",
        )
        assert_matches_type(BroadcastCancelResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: Zavudev) -> None:
        response = client.broadcasts.with_raw_response.cancel(
            "broadcastId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = response.parse()
        assert_matches_type(BroadcastCancelResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: Zavudev) -> None:
        with client.broadcasts.with_streaming_response.cancel(
            "broadcastId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = response.parse()
            assert_matches_type(BroadcastCancelResponse, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_cancel(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            client.broadcasts.with_raw_response.cancel(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_progress(self, client: Zavudev) -> None:
        broadcast = client.broadcasts.progress(
            "broadcastId",
        )
        assert_matches_type(BroadcastProgress, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_progress(self, client: Zavudev) -> None:
        response = client.broadcasts.with_raw_response.progress(
            "broadcastId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = response.parse()
        assert_matches_type(BroadcastProgress, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_progress(self, client: Zavudev) -> None:
        with client.broadcasts.with_streaming_response.progress(
            "broadcastId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = response.parse()
            assert_matches_type(BroadcastProgress, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_progress(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            client.broadcasts.with_raw_response.progress(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_reschedule(self, client: Zavudev) -> None:
        broadcast = client.broadcasts.reschedule(
            broadcast_id="broadcastId",
            scheduled_at=parse_datetime("2024-01-15T14:00:00Z"),
        )
        assert_matches_type(BroadcastRescheduleResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_reschedule(self, client: Zavudev) -> None:
        response = client.broadcasts.with_raw_response.reschedule(
            broadcast_id="broadcastId",
            scheduled_at=parse_datetime("2024-01-15T14:00:00Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = response.parse()
        assert_matches_type(BroadcastRescheduleResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_reschedule(self, client: Zavudev) -> None:
        with client.broadcasts.with_streaming_response.reschedule(
            broadcast_id="broadcastId",
            scheduled_at=parse_datetime("2024-01-15T14:00:00Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = response.parse()
            assert_matches_type(BroadcastRescheduleResponse, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_reschedule(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            client.broadcasts.with_raw_response.reschedule(
                broadcast_id="",
                scheduled_at=parse_datetime("2024-01-15T14:00:00Z"),
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send(self, client: Zavudev) -> None:
        broadcast = client.broadcasts.send(
            broadcast_id="broadcastId",
        )
        assert_matches_type(BroadcastSendResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_with_all_params(self, client: Zavudev) -> None:
        broadcast = client.broadcasts.send(
            broadcast_id="broadcastId",
            scheduled_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(BroadcastSendResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_send(self, client: Zavudev) -> None:
        response = client.broadcasts.with_raw_response.send(
            broadcast_id="broadcastId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = response.parse()
        assert_matches_type(BroadcastSendResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_send(self, client: Zavudev) -> None:
        with client.broadcasts.with_streaming_response.send(
            broadcast_id="broadcastId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = response.parse()
            assert_matches_type(BroadcastSendResponse, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_send(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            client.broadcasts.with_raw_response.send(
                broadcast_id="",
            )


class TestAsyncBroadcasts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncZavudev) -> None:
        broadcast = await async_client.broadcasts.create(
            channel="sms",
            name="Black Friday Sale",
        )
        assert_matches_type(BroadcastCreateResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncZavudev) -> None:
        broadcast = await async_client.broadcasts.create(
            channel="sms",
            name="Black Friday Sale",
            content={
                "filename": "filename",
                "media_id": "mediaId",
                "media_url": "mediaUrl",
                "mime_type": "mimeType",
                "template_id": "templateId",
                "template_variables": {"foo": "string"},
            },
            email_html_body="emailHtmlBody",
            email_subject="emailSubject",
            idempotency_key="idempotencyKey",
            message_type="text",
            metadata={"foo": "string"},
            scheduled_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            sender_id="senderId",
            text="Hi {{name}}, check out our Black Friday deals! Use code FRIDAY20 for 20% off.",
        )
        assert_matches_type(BroadcastCreateResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncZavudev) -> None:
        response = await async_client.broadcasts.with_raw_response.create(
            channel="sms",
            name="Black Friday Sale",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = await response.parse()
        assert_matches_type(BroadcastCreateResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncZavudev) -> None:
        async with async_client.broadcasts.with_streaming_response.create(
            channel="sms",
            name="Black Friday Sale",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = await response.parse()
            assert_matches_type(BroadcastCreateResponse, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncZavudev) -> None:
        broadcast = await async_client.broadcasts.retrieve(
            "broadcastId",
        )
        assert_matches_type(BroadcastRetrieveResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncZavudev) -> None:
        response = await async_client.broadcasts.with_raw_response.retrieve(
            "broadcastId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = await response.parse()
        assert_matches_type(BroadcastRetrieveResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncZavudev) -> None:
        async with async_client.broadcasts.with_streaming_response.retrieve(
            "broadcastId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = await response.parse()
            assert_matches_type(BroadcastRetrieveResponse, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            await async_client.broadcasts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncZavudev) -> None:
        broadcast = await async_client.broadcasts.update(
            broadcast_id="broadcastId",
        )
        assert_matches_type(BroadcastUpdateResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncZavudev) -> None:
        broadcast = await async_client.broadcasts.update(
            broadcast_id="broadcastId",
            content={
                "filename": "filename",
                "media_id": "mediaId",
                "media_url": "mediaUrl",
                "mime_type": "mimeType",
                "template_id": "templateId",
                "template_variables": {"foo": "string"},
            },
            email_html_body="emailHtmlBody",
            email_subject="emailSubject",
            metadata={"foo": "string"},
            name="name",
            text="text",
        )
        assert_matches_type(BroadcastUpdateResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncZavudev) -> None:
        response = await async_client.broadcasts.with_raw_response.update(
            broadcast_id="broadcastId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = await response.parse()
        assert_matches_type(BroadcastUpdateResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncZavudev) -> None:
        async with async_client.broadcasts.with_streaming_response.update(
            broadcast_id="broadcastId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = await response.parse()
            assert_matches_type(BroadcastUpdateResponse, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            await async_client.broadcasts.with_raw_response.update(
                broadcast_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncZavudev) -> None:
        broadcast = await async_client.broadcasts.list()
        assert_matches_type(AsyncCursor[Broadcast], broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncZavudev) -> None:
        broadcast = await async_client.broadcasts.list(
            cursor="cursor",
            limit=100,
            status="draft",
        )
        assert_matches_type(AsyncCursor[Broadcast], broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncZavudev) -> None:
        response = await async_client.broadcasts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = await response.parse()
        assert_matches_type(AsyncCursor[Broadcast], broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncZavudev) -> None:
        async with async_client.broadcasts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = await response.parse()
            assert_matches_type(AsyncCursor[Broadcast], broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncZavudev) -> None:
        broadcast = await async_client.broadcasts.delete(
            "broadcastId",
        )
        assert broadcast is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncZavudev) -> None:
        response = await async_client.broadcasts.with_raw_response.delete(
            "broadcastId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = await response.parse()
        assert broadcast is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncZavudev) -> None:
        async with async_client.broadcasts.with_streaming_response.delete(
            "broadcastId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = await response.parse()
            assert broadcast is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            await async_client.broadcasts.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncZavudev) -> None:
        broadcast = await async_client.broadcasts.cancel(
            "broadcastId",
        )
        assert_matches_type(BroadcastCancelResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncZavudev) -> None:
        response = await async_client.broadcasts.with_raw_response.cancel(
            "broadcastId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = await response.parse()
        assert_matches_type(BroadcastCancelResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncZavudev) -> None:
        async with async_client.broadcasts.with_streaming_response.cancel(
            "broadcastId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = await response.parse()
            assert_matches_type(BroadcastCancelResponse, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            await async_client.broadcasts.with_raw_response.cancel(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_progress(self, async_client: AsyncZavudev) -> None:
        broadcast = await async_client.broadcasts.progress(
            "broadcastId",
        )
        assert_matches_type(BroadcastProgress, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_progress(self, async_client: AsyncZavudev) -> None:
        response = await async_client.broadcasts.with_raw_response.progress(
            "broadcastId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = await response.parse()
        assert_matches_type(BroadcastProgress, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_progress(self, async_client: AsyncZavudev) -> None:
        async with async_client.broadcasts.with_streaming_response.progress(
            "broadcastId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = await response.parse()
            assert_matches_type(BroadcastProgress, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_progress(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            await async_client.broadcasts.with_raw_response.progress(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_reschedule(self, async_client: AsyncZavudev) -> None:
        broadcast = await async_client.broadcasts.reschedule(
            broadcast_id="broadcastId",
            scheduled_at=parse_datetime("2024-01-15T14:00:00Z"),
        )
        assert_matches_type(BroadcastRescheduleResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_reschedule(self, async_client: AsyncZavudev) -> None:
        response = await async_client.broadcasts.with_raw_response.reschedule(
            broadcast_id="broadcastId",
            scheduled_at=parse_datetime("2024-01-15T14:00:00Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = await response.parse()
        assert_matches_type(BroadcastRescheduleResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_reschedule(self, async_client: AsyncZavudev) -> None:
        async with async_client.broadcasts.with_streaming_response.reschedule(
            broadcast_id="broadcastId",
            scheduled_at=parse_datetime("2024-01-15T14:00:00Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = await response.parse()
            assert_matches_type(BroadcastRescheduleResponse, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_reschedule(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            await async_client.broadcasts.with_raw_response.reschedule(
                broadcast_id="",
                scheduled_at=parse_datetime("2024-01-15T14:00:00Z"),
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send(self, async_client: AsyncZavudev) -> None:
        broadcast = await async_client.broadcasts.send(
            broadcast_id="broadcastId",
        )
        assert_matches_type(BroadcastSendResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_with_all_params(self, async_client: AsyncZavudev) -> None:
        broadcast = await async_client.broadcasts.send(
            broadcast_id="broadcastId",
            scheduled_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(BroadcastSendResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_send(self, async_client: AsyncZavudev) -> None:
        response = await async_client.broadcasts.with_raw_response.send(
            broadcast_id="broadcastId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = await response.parse()
        assert_matches_type(BroadcastSendResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncZavudev) -> None:
        async with async_client.broadcasts.with_streaming_response.send(
            broadcast_id="broadcastId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = await response.parse()
            assert_matches_type(BroadcastSendResponse, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_send(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            await async_client.broadcasts.with_raw_response.send(
                broadcast_id="",
            )
