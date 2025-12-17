# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from zavudev import Zavudev, AsyncZavudev
from tests.utils import assert_matches_type
from zavudev.types import (
    Sender,
    WebhookSecretResponse,
    SenderUpdateProfileResponse,
    WhatsappBusinessProfileResponse,
    SenderUploadProfilePictureResponse,
)
from zavudev.pagination import SyncCursor, AsyncCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSenders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Zavudev) -> None:
        sender = client.senders.create(
            name="name",
            phone_number="phoneNumber",
        )
        assert_matches_type(Sender, sender, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Zavudev) -> None:
        sender = client.senders.create(
            name="name",
            phone_number="phoneNumber",
            set_as_default=True,
            webhook_events=["message.queued"],
            webhook_url="https://example.com",
        )
        assert_matches_type(Sender, sender, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Zavudev) -> None:
        response = client.senders.with_raw_response.create(
            name="name",
            phone_number="phoneNumber",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sender = response.parse()
        assert_matches_type(Sender, sender, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Zavudev) -> None:
        with client.senders.with_streaming_response.create(
            name="name",
            phone_number="phoneNumber",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sender = response.parse()
            assert_matches_type(Sender, sender, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Zavudev) -> None:
        sender = client.senders.retrieve(
            "senderId",
        )
        assert_matches_type(Sender, sender, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Zavudev) -> None:
        response = client.senders.with_raw_response.retrieve(
            "senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sender = response.parse()
        assert_matches_type(Sender, sender, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Zavudev) -> None:
        with client.senders.with_streaming_response.retrieve(
            "senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sender = response.parse()
            assert_matches_type(Sender, sender, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            client.senders.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Zavudev) -> None:
        sender = client.senders.update(
            sender_id="senderId",
        )
        assert_matches_type(Sender, sender, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Zavudev) -> None:
        sender = client.senders.update(
            sender_id="senderId",
            name="name",
            set_as_default=True,
            webhook_active=True,
            webhook_events=["message.queued"],
            webhook_url="https://example.com",
        )
        assert_matches_type(Sender, sender, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Zavudev) -> None:
        response = client.senders.with_raw_response.update(
            sender_id="senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sender = response.parse()
        assert_matches_type(Sender, sender, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Zavudev) -> None:
        with client.senders.with_streaming_response.update(
            sender_id="senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sender = response.parse()
            assert_matches_type(Sender, sender, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            client.senders.with_raw_response.update(
                sender_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Zavudev) -> None:
        sender = client.senders.list()
        assert_matches_type(SyncCursor[Sender], sender, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Zavudev) -> None:
        sender = client.senders.list(
            cursor="cursor",
            limit=100,
        )
        assert_matches_type(SyncCursor[Sender], sender, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Zavudev) -> None:
        response = client.senders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sender = response.parse()
        assert_matches_type(SyncCursor[Sender], sender, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Zavudev) -> None:
        with client.senders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sender = response.parse()
            assert_matches_type(SyncCursor[Sender], sender, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Zavudev) -> None:
        sender = client.senders.delete(
            "senderId",
        )
        assert sender is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Zavudev) -> None:
        response = client.senders.with_raw_response.delete(
            "senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sender = response.parse()
        assert sender is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Zavudev) -> None:
        with client.senders.with_streaming_response.delete(
            "senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sender = response.parse()
            assert sender is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            client.senders.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_profile(self, client: Zavudev) -> None:
        sender = client.senders.get_profile(
            "senderId",
        )
        assert_matches_type(WhatsappBusinessProfileResponse, sender, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_profile(self, client: Zavudev) -> None:
        response = client.senders.with_raw_response.get_profile(
            "senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sender = response.parse()
        assert_matches_type(WhatsappBusinessProfileResponse, sender, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_profile(self, client: Zavudev) -> None:
        with client.senders.with_streaming_response.get_profile(
            "senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sender = response.parse()
            assert_matches_type(WhatsappBusinessProfileResponse, sender, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_profile(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            client.senders.with_raw_response.get_profile(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_regenerate_webhook_secret(self, client: Zavudev) -> None:
        sender = client.senders.regenerate_webhook_secret(
            "senderId",
        )
        assert_matches_type(WebhookSecretResponse, sender, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_regenerate_webhook_secret(self, client: Zavudev) -> None:
        response = client.senders.with_raw_response.regenerate_webhook_secret(
            "senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sender = response.parse()
        assert_matches_type(WebhookSecretResponse, sender, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_regenerate_webhook_secret(self, client: Zavudev) -> None:
        with client.senders.with_streaming_response.regenerate_webhook_secret(
            "senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sender = response.parse()
            assert_matches_type(WebhookSecretResponse, sender, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_regenerate_webhook_secret(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            client.senders.with_raw_response.regenerate_webhook_secret(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_profile(self, client: Zavudev) -> None:
        sender = client.senders.update_profile(
            sender_id="senderId",
        )
        assert_matches_type(SenderUpdateProfileResponse, sender, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_profile_with_all_params(self, client: Zavudev) -> None:
        sender = client.senders.update_profile(
            sender_id="senderId",
            about="Succulent specialists!",
            address="address",
            description="We specialize in providing high-quality succulents.",
            email="contact@example.com",
            vertical="RETAIL",
            websites=["https://www.example.com"],
        )
        assert_matches_type(SenderUpdateProfileResponse, sender, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_profile(self, client: Zavudev) -> None:
        response = client.senders.with_raw_response.update_profile(
            sender_id="senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sender = response.parse()
        assert_matches_type(SenderUpdateProfileResponse, sender, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_profile(self, client: Zavudev) -> None:
        with client.senders.with_streaming_response.update_profile(
            sender_id="senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sender = response.parse()
            assert_matches_type(SenderUpdateProfileResponse, sender, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_profile(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            client.senders.with_raw_response.update_profile(
                sender_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload_profile_picture(self, client: Zavudev) -> None:
        sender = client.senders.upload_profile_picture(
            sender_id="senderId",
            image_url="https://example.com/profile.jpg",
            mime_type="image/jpeg",
        )
        assert_matches_type(SenderUploadProfilePictureResponse, sender, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upload_profile_picture(self, client: Zavudev) -> None:
        response = client.senders.with_raw_response.upload_profile_picture(
            sender_id="senderId",
            image_url="https://example.com/profile.jpg",
            mime_type="image/jpeg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sender = response.parse()
        assert_matches_type(SenderUploadProfilePictureResponse, sender, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upload_profile_picture(self, client: Zavudev) -> None:
        with client.senders.with_streaming_response.upload_profile_picture(
            sender_id="senderId",
            image_url="https://example.com/profile.jpg",
            mime_type="image/jpeg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sender = response.parse()
            assert_matches_type(SenderUploadProfilePictureResponse, sender, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_upload_profile_picture(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            client.senders.with_raw_response.upload_profile_picture(
                sender_id="",
                image_url="https://example.com/profile.jpg",
                mime_type="image/jpeg",
            )


class TestAsyncSenders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncZavudev) -> None:
        sender = await async_client.senders.create(
            name="name",
            phone_number="phoneNumber",
        )
        assert_matches_type(Sender, sender, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncZavudev) -> None:
        sender = await async_client.senders.create(
            name="name",
            phone_number="phoneNumber",
            set_as_default=True,
            webhook_events=["message.queued"],
            webhook_url="https://example.com",
        )
        assert_matches_type(Sender, sender, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncZavudev) -> None:
        response = await async_client.senders.with_raw_response.create(
            name="name",
            phone_number="phoneNumber",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sender = await response.parse()
        assert_matches_type(Sender, sender, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncZavudev) -> None:
        async with async_client.senders.with_streaming_response.create(
            name="name",
            phone_number="phoneNumber",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sender = await response.parse()
            assert_matches_type(Sender, sender, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncZavudev) -> None:
        sender = await async_client.senders.retrieve(
            "senderId",
        )
        assert_matches_type(Sender, sender, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncZavudev) -> None:
        response = await async_client.senders.with_raw_response.retrieve(
            "senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sender = await response.parse()
        assert_matches_type(Sender, sender, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncZavudev) -> None:
        async with async_client.senders.with_streaming_response.retrieve(
            "senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sender = await response.parse()
            assert_matches_type(Sender, sender, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            await async_client.senders.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncZavudev) -> None:
        sender = await async_client.senders.update(
            sender_id="senderId",
        )
        assert_matches_type(Sender, sender, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncZavudev) -> None:
        sender = await async_client.senders.update(
            sender_id="senderId",
            name="name",
            set_as_default=True,
            webhook_active=True,
            webhook_events=["message.queued"],
            webhook_url="https://example.com",
        )
        assert_matches_type(Sender, sender, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncZavudev) -> None:
        response = await async_client.senders.with_raw_response.update(
            sender_id="senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sender = await response.parse()
        assert_matches_type(Sender, sender, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncZavudev) -> None:
        async with async_client.senders.with_streaming_response.update(
            sender_id="senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sender = await response.parse()
            assert_matches_type(Sender, sender, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            await async_client.senders.with_raw_response.update(
                sender_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncZavudev) -> None:
        sender = await async_client.senders.list()
        assert_matches_type(AsyncCursor[Sender], sender, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncZavudev) -> None:
        sender = await async_client.senders.list(
            cursor="cursor",
            limit=100,
        )
        assert_matches_type(AsyncCursor[Sender], sender, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncZavudev) -> None:
        response = await async_client.senders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sender = await response.parse()
        assert_matches_type(AsyncCursor[Sender], sender, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncZavudev) -> None:
        async with async_client.senders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sender = await response.parse()
            assert_matches_type(AsyncCursor[Sender], sender, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncZavudev) -> None:
        sender = await async_client.senders.delete(
            "senderId",
        )
        assert sender is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncZavudev) -> None:
        response = await async_client.senders.with_raw_response.delete(
            "senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sender = await response.parse()
        assert sender is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncZavudev) -> None:
        async with async_client.senders.with_streaming_response.delete(
            "senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sender = await response.parse()
            assert sender is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            await async_client.senders.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_profile(self, async_client: AsyncZavudev) -> None:
        sender = await async_client.senders.get_profile(
            "senderId",
        )
        assert_matches_type(WhatsappBusinessProfileResponse, sender, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_profile(self, async_client: AsyncZavudev) -> None:
        response = await async_client.senders.with_raw_response.get_profile(
            "senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sender = await response.parse()
        assert_matches_type(WhatsappBusinessProfileResponse, sender, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_profile(self, async_client: AsyncZavudev) -> None:
        async with async_client.senders.with_streaming_response.get_profile(
            "senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sender = await response.parse()
            assert_matches_type(WhatsappBusinessProfileResponse, sender, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_profile(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            await async_client.senders.with_raw_response.get_profile(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_regenerate_webhook_secret(self, async_client: AsyncZavudev) -> None:
        sender = await async_client.senders.regenerate_webhook_secret(
            "senderId",
        )
        assert_matches_type(WebhookSecretResponse, sender, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_regenerate_webhook_secret(self, async_client: AsyncZavudev) -> None:
        response = await async_client.senders.with_raw_response.regenerate_webhook_secret(
            "senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sender = await response.parse()
        assert_matches_type(WebhookSecretResponse, sender, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_regenerate_webhook_secret(self, async_client: AsyncZavudev) -> None:
        async with async_client.senders.with_streaming_response.regenerate_webhook_secret(
            "senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sender = await response.parse()
            assert_matches_type(WebhookSecretResponse, sender, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_regenerate_webhook_secret(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            await async_client.senders.with_raw_response.regenerate_webhook_secret(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_profile(self, async_client: AsyncZavudev) -> None:
        sender = await async_client.senders.update_profile(
            sender_id="senderId",
        )
        assert_matches_type(SenderUpdateProfileResponse, sender, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_profile_with_all_params(self, async_client: AsyncZavudev) -> None:
        sender = await async_client.senders.update_profile(
            sender_id="senderId",
            about="Succulent specialists!",
            address="address",
            description="We specialize in providing high-quality succulents.",
            email="contact@example.com",
            vertical="RETAIL",
            websites=["https://www.example.com"],
        )
        assert_matches_type(SenderUpdateProfileResponse, sender, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_profile(self, async_client: AsyncZavudev) -> None:
        response = await async_client.senders.with_raw_response.update_profile(
            sender_id="senderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sender = await response.parse()
        assert_matches_type(SenderUpdateProfileResponse, sender, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_profile(self, async_client: AsyncZavudev) -> None:
        async with async_client.senders.with_streaming_response.update_profile(
            sender_id="senderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sender = await response.parse()
            assert_matches_type(SenderUpdateProfileResponse, sender, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_profile(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            await async_client.senders.with_raw_response.update_profile(
                sender_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload_profile_picture(self, async_client: AsyncZavudev) -> None:
        sender = await async_client.senders.upload_profile_picture(
            sender_id="senderId",
            image_url="https://example.com/profile.jpg",
            mime_type="image/jpeg",
        )
        assert_matches_type(SenderUploadProfilePictureResponse, sender, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upload_profile_picture(self, async_client: AsyncZavudev) -> None:
        response = await async_client.senders.with_raw_response.upload_profile_picture(
            sender_id="senderId",
            image_url="https://example.com/profile.jpg",
            mime_type="image/jpeg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sender = await response.parse()
        assert_matches_type(SenderUploadProfilePictureResponse, sender, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upload_profile_picture(self, async_client: AsyncZavudev) -> None:
        async with async_client.senders.with_streaming_response.upload_profile_picture(
            sender_id="senderId",
            image_url="https://example.com/profile.jpg",
            mime_type="image/jpeg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sender = await response.parse()
            assert_matches_type(SenderUploadProfilePictureResponse, sender, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_upload_profile_picture(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            await async_client.senders.with_raw_response.upload_profile_picture(
                sender_id="",
                image_url="https://example.com/profile.jpg",
                mime_type="image/jpeg",
            )
