# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from zavudev import Zavudev, AsyncZavudev
from tests.utils import assert_matches_type
from zavudev.types.contacts import (
    ChannelAddResponse,
    ChannelUpdateResponse,
    ChannelSetPrimaryResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChannels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Zavudev) -> None:
        channel = client.contacts.channels.update(
            channel_id="channelId",
            contact_id="contactId",
        )
        assert_matches_type(ChannelUpdateResponse, channel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Zavudev) -> None:
        channel = client.contacts.channels.update(
            channel_id="channelId",
            contact_id="contactId",
            label="label",
            metadata={"foo": "string"},
            verified=True,
        )
        assert_matches_type(ChannelUpdateResponse, channel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Zavudev) -> None:
        response = client.contacts.channels.with_raw_response.update(
            channel_id="channelId",
            contact_id="contactId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = response.parse()
        assert_matches_type(ChannelUpdateResponse, channel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Zavudev) -> None:
        with client.contacts.channels.with_streaming_response.update(
            channel_id="channelId",
            contact_id="contactId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = response.parse()
            assert_matches_type(ChannelUpdateResponse, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            client.contacts.channels.with_raw_response.update(
                channel_id="channelId",
                contact_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.contacts.channels.with_raw_response.update(
                channel_id="",
                contact_id="contactId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add(self, client: Zavudev) -> None:
        channel = client.contacts.channels.add(
            contact_id="contactId",
            channel="email",
            identifier="john.work@company.com",
        )
        assert_matches_type(ChannelAddResponse, channel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_with_all_params(self, client: Zavudev) -> None:
        channel = client.contacts.channels.add(
            contact_id="contactId",
            channel="email",
            identifier="john.work@company.com",
            country_code="US",
            is_primary=True,
            label="work",
        )
        assert_matches_type(ChannelAddResponse, channel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: Zavudev) -> None:
        response = client.contacts.channels.with_raw_response.add(
            contact_id="contactId",
            channel="email",
            identifier="john.work@company.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = response.parse()
        assert_matches_type(ChannelAddResponse, channel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: Zavudev) -> None:
        with client.contacts.channels.with_streaming_response.add(
            contact_id="contactId",
            channel="email",
            identifier="john.work@company.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = response.parse()
            assert_matches_type(ChannelAddResponse, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            client.contacts.channels.with_raw_response.add(
                contact_id="",
                channel="email",
                identifier="john.work@company.com",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove(self, client: Zavudev) -> None:
        channel = client.contacts.channels.remove(
            channel_id="channelId",
            contact_id="contactId",
        )
        assert channel is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: Zavudev) -> None:
        response = client.contacts.channels.with_raw_response.remove(
            channel_id="channelId",
            contact_id="contactId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = response.parse()
        assert channel is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: Zavudev) -> None:
        with client.contacts.channels.with_streaming_response.remove(
            channel_id="channelId",
            contact_id="contactId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = response.parse()
            assert channel is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remove(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            client.contacts.channels.with_raw_response.remove(
                channel_id="channelId",
                contact_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.contacts.channels.with_raw_response.remove(
                channel_id="",
                contact_id="contactId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set_primary(self, client: Zavudev) -> None:
        channel = client.contacts.channels.set_primary(
            channel_id="channelId",
            contact_id="contactId",
        )
        assert_matches_type(ChannelSetPrimaryResponse, channel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_set_primary(self, client: Zavudev) -> None:
        response = client.contacts.channels.with_raw_response.set_primary(
            channel_id="channelId",
            contact_id="contactId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = response.parse()
        assert_matches_type(ChannelSetPrimaryResponse, channel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_set_primary(self, client: Zavudev) -> None:
        with client.contacts.channels.with_streaming_response.set_primary(
            channel_id="channelId",
            contact_id="contactId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = response.parse()
            assert_matches_type(ChannelSetPrimaryResponse, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_set_primary(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            client.contacts.channels.with_raw_response.set_primary(
                channel_id="channelId",
                contact_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.contacts.channels.with_raw_response.set_primary(
                channel_id="",
                contact_id="contactId",
            )


class TestAsyncChannels:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncZavudev) -> None:
        channel = await async_client.contacts.channels.update(
            channel_id="channelId",
            contact_id="contactId",
        )
        assert_matches_type(ChannelUpdateResponse, channel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncZavudev) -> None:
        channel = await async_client.contacts.channels.update(
            channel_id="channelId",
            contact_id="contactId",
            label="label",
            metadata={"foo": "string"},
            verified=True,
        )
        assert_matches_type(ChannelUpdateResponse, channel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncZavudev) -> None:
        response = await async_client.contacts.channels.with_raw_response.update(
            channel_id="channelId",
            contact_id="contactId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = await response.parse()
        assert_matches_type(ChannelUpdateResponse, channel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncZavudev) -> None:
        async with async_client.contacts.channels.with_streaming_response.update(
            channel_id="channelId",
            contact_id="contactId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = await response.parse()
            assert_matches_type(ChannelUpdateResponse, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            await async_client.contacts.channels.with_raw_response.update(
                channel_id="channelId",
                contact_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.contacts.channels.with_raw_response.update(
                channel_id="",
                contact_id="contactId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncZavudev) -> None:
        channel = await async_client.contacts.channels.add(
            contact_id="contactId",
            channel="email",
            identifier="john.work@company.com",
        )
        assert_matches_type(ChannelAddResponse, channel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncZavudev) -> None:
        channel = await async_client.contacts.channels.add(
            contact_id="contactId",
            channel="email",
            identifier="john.work@company.com",
            country_code="US",
            is_primary=True,
            label="work",
        )
        assert_matches_type(ChannelAddResponse, channel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncZavudev) -> None:
        response = await async_client.contacts.channels.with_raw_response.add(
            contact_id="contactId",
            channel="email",
            identifier="john.work@company.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = await response.parse()
        assert_matches_type(ChannelAddResponse, channel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncZavudev) -> None:
        async with async_client.contacts.channels.with_streaming_response.add(
            contact_id="contactId",
            channel="email",
            identifier="john.work@company.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = await response.parse()
            assert_matches_type(ChannelAddResponse, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            await async_client.contacts.channels.with_raw_response.add(
                contact_id="",
                channel="email",
                identifier="john.work@company.com",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncZavudev) -> None:
        channel = await async_client.contacts.channels.remove(
            channel_id="channelId",
            contact_id="contactId",
        )
        assert channel is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncZavudev) -> None:
        response = await async_client.contacts.channels.with_raw_response.remove(
            channel_id="channelId",
            contact_id="contactId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = await response.parse()
        assert channel is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncZavudev) -> None:
        async with async_client.contacts.channels.with_streaming_response.remove(
            channel_id="channelId",
            contact_id="contactId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = await response.parse()
            assert channel is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            await async_client.contacts.channels.with_raw_response.remove(
                channel_id="channelId",
                contact_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.contacts.channels.with_raw_response.remove(
                channel_id="",
                contact_id="contactId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set_primary(self, async_client: AsyncZavudev) -> None:
        channel = await async_client.contacts.channels.set_primary(
            channel_id="channelId",
            contact_id="contactId",
        )
        assert_matches_type(ChannelSetPrimaryResponse, channel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_set_primary(self, async_client: AsyncZavudev) -> None:
        response = await async_client.contacts.channels.with_raw_response.set_primary(
            channel_id="channelId",
            contact_id="contactId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = await response.parse()
        assert_matches_type(ChannelSetPrimaryResponse, channel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_set_primary(self, async_client: AsyncZavudev) -> None:
        async with async_client.contacts.channels.with_streaming_response.set_primary(
            channel_id="channelId",
            contact_id="contactId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = await response.parse()
            assert_matches_type(ChannelSetPrimaryResponse, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_set_primary(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            await async_client.contacts.channels.with_raw_response.set_primary(
                channel_id="channelId",
                contact_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.contacts.channels.with_raw_response.set_primary(
                channel_id="",
                contact_id="contactId",
            )
