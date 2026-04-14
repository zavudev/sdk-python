# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from zavudev import Zavudev, AsyncZavudev
from tests.utils import assert_matches_type
from zavudev.types import (
    VerifiedURL,
    URLRetrieveDetailsResponse,
    URLSubmitForVerificationResponse,
)
from zavudev.pagination import SyncCursor, AsyncCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestURLs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_verified(self, client: Zavudev) -> None:
        url = client.urls.list_verified()
        assert_matches_type(SyncCursor[VerifiedURL], url, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_verified_with_all_params(self, client: Zavudev) -> None:
        url = client.urls.list_verified(
            cursor="cursor",
            limit=100,
            status="pending",
        )
        assert_matches_type(SyncCursor[VerifiedURL], url, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_verified(self, client: Zavudev) -> None:
        response = client.urls.with_raw_response.list_verified()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url = response.parse()
        assert_matches_type(SyncCursor[VerifiedURL], url, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_verified(self, client: Zavudev) -> None:
        with client.urls.with_streaming_response.list_verified() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url = response.parse()
            assert_matches_type(SyncCursor[VerifiedURL], url, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_details(self, client: Zavudev) -> None:
        url = client.urls.retrieve_details(
            "urlId",
        )
        assert_matches_type(URLRetrieveDetailsResponse, url, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_details(self, client: Zavudev) -> None:
        response = client.urls.with_raw_response.retrieve_details(
            "urlId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url = response.parse()
        assert_matches_type(URLRetrieveDetailsResponse, url, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_details(self, client: Zavudev) -> None:
        with client.urls.with_streaming_response.retrieve_details(
            "urlId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url = response.parse()
            assert_matches_type(URLRetrieveDetailsResponse, url, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_details(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url_id` but received ''"):
            client.urls.with_raw_response.retrieve_details(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit_for_verification(self, client: Zavudev) -> None:
        url = client.urls.submit_for_verification(
            url="https://example.com/page",
        )
        assert_matches_type(URLSubmitForVerificationResponse, url, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_submit_for_verification(self, client: Zavudev) -> None:
        response = client.urls.with_raw_response.submit_for_verification(
            url="https://example.com/page",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url = response.parse()
        assert_matches_type(URLSubmitForVerificationResponse, url, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_submit_for_verification(self, client: Zavudev) -> None:
        with client.urls.with_streaming_response.submit_for_verification(
            url="https://example.com/page",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url = response.parse()
            assert_matches_type(URLSubmitForVerificationResponse, url, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncURLs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_verified(self, async_client: AsyncZavudev) -> None:
        url = await async_client.urls.list_verified()
        assert_matches_type(AsyncCursor[VerifiedURL], url, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_verified_with_all_params(self, async_client: AsyncZavudev) -> None:
        url = await async_client.urls.list_verified(
            cursor="cursor",
            limit=100,
            status="pending",
        )
        assert_matches_type(AsyncCursor[VerifiedURL], url, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_verified(self, async_client: AsyncZavudev) -> None:
        response = await async_client.urls.with_raw_response.list_verified()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url = await response.parse()
        assert_matches_type(AsyncCursor[VerifiedURL], url, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_verified(self, async_client: AsyncZavudev) -> None:
        async with async_client.urls.with_streaming_response.list_verified() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url = await response.parse()
            assert_matches_type(AsyncCursor[VerifiedURL], url, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_details(self, async_client: AsyncZavudev) -> None:
        url = await async_client.urls.retrieve_details(
            "urlId",
        )
        assert_matches_type(URLRetrieveDetailsResponse, url, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_details(self, async_client: AsyncZavudev) -> None:
        response = await async_client.urls.with_raw_response.retrieve_details(
            "urlId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url = await response.parse()
        assert_matches_type(URLRetrieveDetailsResponse, url, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_details(self, async_client: AsyncZavudev) -> None:
        async with async_client.urls.with_streaming_response.retrieve_details(
            "urlId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url = await response.parse()
            assert_matches_type(URLRetrieveDetailsResponse, url, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_details(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url_id` but received ''"):
            await async_client.urls.with_raw_response.retrieve_details(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit_for_verification(self, async_client: AsyncZavudev) -> None:
        url = await async_client.urls.submit_for_verification(
            url="https://example.com/page",
        )
        assert_matches_type(URLSubmitForVerificationResponse, url, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_submit_for_verification(self, async_client: AsyncZavudev) -> None:
        response = await async_client.urls.with_raw_response.submit_for_verification(
            url="https://example.com/page",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url = await response.parse()
        assert_matches_type(URLSubmitForVerificationResponse, url, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_submit_for_verification(self, async_client: AsyncZavudev) -> None:
        async with async_client.urls.with_streaming_response.submit_for_verification(
            url="https://example.com/page",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url = await response.parse()
            assert_matches_type(URLSubmitForVerificationResponse, url, path=["response"])

        assert cast(Any, response.is_closed) is True
