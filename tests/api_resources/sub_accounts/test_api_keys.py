# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from zavudev import Zavudev, AsyncZavudev
from tests.utils import assert_matches_type
from zavudev.types.sub_accounts import APIKeyListResponse, APIKeyCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAPIKeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Zavudev) -> None:
        api_key = client.sub_accounts.api_keys.create(
            id="id",
            name="Production Key",
        )
        assert_matches_type(APIKeyCreateResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Zavudev) -> None:
        api_key = client.sub_accounts.api_keys.create(
            id="id",
            name="Production Key",
            environment="live",
            permissions=["string"],
        )
        assert_matches_type(APIKeyCreateResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Zavudev) -> None:
        response = client.sub_accounts.api_keys.with_raw_response.create(
            id="id",
            name="Production Key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(APIKeyCreateResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Zavudev) -> None:
        with client.sub_accounts.api_keys.with_streaming_response.create(
            id="id",
            name="Production Key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(APIKeyCreateResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sub_accounts.api_keys.with_raw_response.create(
                id="",
                name="Production Key",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Zavudev) -> None:
        api_key = client.sub_accounts.api_keys.list(
            "id",
        )
        assert_matches_type(APIKeyListResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Zavudev) -> None:
        response = client.sub_accounts.api_keys.with_raw_response.list(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(APIKeyListResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Zavudev) -> None:
        with client.sub_accounts.api_keys.with_streaming_response.list(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(APIKeyListResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sub_accounts.api_keys.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_revoke(self, client: Zavudev) -> None:
        api_key = client.sub_accounts.api_keys.revoke(
            key_id="keyId",
            id="id",
        )
        assert api_key is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_revoke(self, client: Zavudev) -> None:
        response = client.sub_accounts.api_keys.with_raw_response.revoke(
            key_id="keyId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert api_key is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_revoke(self, client: Zavudev) -> None:
        with client.sub_accounts.api_keys.with_streaming_response.revoke(
            key_id="keyId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert api_key is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_revoke(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sub_accounts.api_keys.with_raw_response.revoke(
                key_id="keyId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_id` but received ''"):
            client.sub_accounts.api_keys.with_raw_response.revoke(
                key_id="",
                id="id",
            )


class TestAsyncAPIKeys:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncZavudev) -> None:
        api_key = await async_client.sub_accounts.api_keys.create(
            id="id",
            name="Production Key",
        )
        assert_matches_type(APIKeyCreateResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncZavudev) -> None:
        api_key = await async_client.sub_accounts.api_keys.create(
            id="id",
            name="Production Key",
            environment="live",
            permissions=["string"],
        )
        assert_matches_type(APIKeyCreateResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncZavudev) -> None:
        response = await async_client.sub_accounts.api_keys.with_raw_response.create(
            id="id",
            name="Production Key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(APIKeyCreateResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncZavudev) -> None:
        async with async_client.sub_accounts.api_keys.with_streaming_response.create(
            id="id",
            name="Production Key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(APIKeyCreateResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sub_accounts.api_keys.with_raw_response.create(
                id="",
                name="Production Key",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncZavudev) -> None:
        api_key = await async_client.sub_accounts.api_keys.list(
            "id",
        )
        assert_matches_type(APIKeyListResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncZavudev) -> None:
        response = await async_client.sub_accounts.api_keys.with_raw_response.list(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(APIKeyListResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncZavudev) -> None:
        async with async_client.sub_accounts.api_keys.with_streaming_response.list(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(APIKeyListResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sub_accounts.api_keys.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_revoke(self, async_client: AsyncZavudev) -> None:
        api_key = await async_client.sub_accounts.api_keys.revoke(
            key_id="keyId",
            id="id",
        )
        assert api_key is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_revoke(self, async_client: AsyncZavudev) -> None:
        response = await async_client.sub_accounts.api_keys.with_raw_response.revoke(
            key_id="keyId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert api_key is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_revoke(self, async_client: AsyncZavudev) -> None:
        async with async_client.sub_accounts.api_keys.with_streaming_response.revoke(
            key_id="keyId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert api_key is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_revoke(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sub_accounts.api_keys.with_raw_response.revoke(
                key_id="keyId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_id` but received ''"):
            await async_client.sub_accounts.api_keys.with_raw_response.revoke(
                key_id="",
                id="id",
            )
