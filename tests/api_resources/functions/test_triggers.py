# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from zavudev import Zavudev, AsyncZavudev
from tests.utils import assert_matches_type
from zavudev.types.functions import (
    TriggerListResponse,
    TriggerCreateResponse,
    TriggerUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTriggers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Zavudev) -> None:
        trigger = client.functions.triggers.create(
            function_id="functionId",
            event_types=["message.inbound"],
            sender_ids=[None],
        )
        assert_matches_type(TriggerCreateResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Zavudev) -> None:
        trigger = client.functions.triggers.create(
            function_id="functionId",
            event_types=["message.inbound"],
            sender_ids=[None],
            cron="0 9 * * 1-5",
        )
        assert_matches_type(TriggerCreateResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Zavudev) -> None:
        response = client.functions.triggers.with_raw_response.create(
            function_id="functionId",
            event_types=["message.inbound"],
            sender_ids=[None],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trigger = response.parse()
        assert_matches_type(TriggerCreateResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Zavudev) -> None:
        with client.functions.triggers.with_streaming_response.create(
            function_id="functionId",
            event_types=["message.inbound"],
            sender_ids=[None],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trigger = response.parse()
            assert_matches_type(TriggerCreateResponse, trigger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.functions.triggers.with_raw_response.create(
                function_id="",
                event_types=["message.inbound"],
                sender_ids=[None],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Zavudev) -> None:
        trigger = client.functions.triggers.update(
            trigger_id="triggerId",
            active=True,
        )
        assert_matches_type(TriggerUpdateResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Zavudev) -> None:
        response = client.functions.triggers.with_raw_response.update(
            trigger_id="triggerId",
            active=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trigger = response.parse()
        assert_matches_type(TriggerUpdateResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Zavudev) -> None:
        with client.functions.triggers.with_streaming_response.update(
            trigger_id="triggerId",
            active=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trigger = response.parse()
            assert_matches_type(TriggerUpdateResponse, trigger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trigger_id` but received ''"):
            client.functions.triggers.with_raw_response.update(
                trigger_id="",
                active=True,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Zavudev) -> None:
        trigger = client.functions.triggers.list(
            "functionId",
        )
        assert_matches_type(TriggerListResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Zavudev) -> None:
        response = client.functions.triggers.with_raw_response.list(
            "functionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trigger = response.parse()
        assert_matches_type(TriggerListResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Zavudev) -> None:
        with client.functions.triggers.with_streaming_response.list(
            "functionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trigger = response.parse()
            assert_matches_type(TriggerListResponse, trigger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.functions.triggers.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Zavudev) -> None:
        trigger = client.functions.triggers.delete(
            "triggerId",
        )
        assert trigger is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Zavudev) -> None:
        response = client.functions.triggers.with_raw_response.delete(
            "triggerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trigger = response.parse()
        assert trigger is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Zavudev) -> None:
        with client.functions.triggers.with_streaming_response.delete(
            "triggerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trigger = response.parse()
            assert trigger is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trigger_id` but received ''"):
            client.functions.triggers.with_raw_response.delete(
                "",
            )


class TestAsyncTriggers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncZavudev) -> None:
        trigger = await async_client.functions.triggers.create(
            function_id="functionId",
            event_types=["message.inbound"],
            sender_ids=[None],
        )
        assert_matches_type(TriggerCreateResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncZavudev) -> None:
        trigger = await async_client.functions.triggers.create(
            function_id="functionId",
            event_types=["message.inbound"],
            sender_ids=[None],
            cron="0 9 * * 1-5",
        )
        assert_matches_type(TriggerCreateResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncZavudev) -> None:
        response = await async_client.functions.triggers.with_raw_response.create(
            function_id="functionId",
            event_types=["message.inbound"],
            sender_ids=[None],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trigger = await response.parse()
        assert_matches_type(TriggerCreateResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncZavudev) -> None:
        async with async_client.functions.triggers.with_streaming_response.create(
            function_id="functionId",
            event_types=["message.inbound"],
            sender_ids=[None],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trigger = await response.parse()
            assert_matches_type(TriggerCreateResponse, trigger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.functions.triggers.with_raw_response.create(
                function_id="",
                event_types=["message.inbound"],
                sender_ids=[None],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncZavudev) -> None:
        trigger = await async_client.functions.triggers.update(
            trigger_id="triggerId",
            active=True,
        )
        assert_matches_type(TriggerUpdateResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncZavudev) -> None:
        response = await async_client.functions.triggers.with_raw_response.update(
            trigger_id="triggerId",
            active=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trigger = await response.parse()
        assert_matches_type(TriggerUpdateResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncZavudev) -> None:
        async with async_client.functions.triggers.with_streaming_response.update(
            trigger_id="triggerId",
            active=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trigger = await response.parse()
            assert_matches_type(TriggerUpdateResponse, trigger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trigger_id` but received ''"):
            await async_client.functions.triggers.with_raw_response.update(
                trigger_id="",
                active=True,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncZavudev) -> None:
        trigger = await async_client.functions.triggers.list(
            "functionId",
        )
        assert_matches_type(TriggerListResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncZavudev) -> None:
        response = await async_client.functions.triggers.with_raw_response.list(
            "functionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trigger = await response.parse()
        assert_matches_type(TriggerListResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncZavudev) -> None:
        async with async_client.functions.triggers.with_streaming_response.list(
            "functionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trigger = await response.parse()
            assert_matches_type(TriggerListResponse, trigger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.functions.triggers.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncZavudev) -> None:
        trigger = await async_client.functions.triggers.delete(
            "triggerId",
        )
        assert trigger is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncZavudev) -> None:
        response = await async_client.functions.triggers.with_raw_response.delete(
            "triggerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trigger = await response.parse()
        assert trigger is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncZavudev) -> None:
        async with async_client.functions.triggers.with_streaming_response.delete(
            "triggerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trigger = await response.parse()
            assert trigger is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trigger_id` but received ''"):
            await async_client.functions.triggers.with_raw_response.delete(
                "",
            )
