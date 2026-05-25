# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from zavudev import Zavudev, AsyncZavudev
from tests.utils import assert_matches_type
from zavudev.types.functions import SecretListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSecrets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Zavudev) -> None:
        secret = client.functions.secrets.list(
            "functionId",
        )
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Zavudev) -> None:
        response = client.functions.secrets.with_raw_response.list(
            "functionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Zavudev) -> None:
        with client.functions.secrets.with_streaming_response.list(
            "functionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(SecretListResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.functions.secrets.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set(self, client: Zavudev) -> None:
        secret = client.functions.secrets.set(
            key="key",
            function_id="functionId",
            value="value",
        )
        assert_matches_type(object, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_set(self, client: Zavudev) -> None:
        response = client.functions.secrets.with_raw_response.set(
            key="key",
            function_id="functionId",
            value="value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(object, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_set(self, client: Zavudev) -> None:
        with client.functions.secrets.with_streaming_response.set(
            key="key",
            function_id="functionId",
            value="value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(object, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_set(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.functions.secrets.with_raw_response.set(
                key="key",
                function_id="",
                value="value",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.functions.secrets.with_raw_response.set(
                key="",
                function_id="functionId",
                value="value",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unset(self, client: Zavudev) -> None:
        secret = client.functions.secrets.unset(
            key="key",
            function_id="functionId",
        )
        assert secret is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_unset(self, client: Zavudev) -> None:
        response = client.functions.secrets.with_raw_response.unset(
            key="key",
            function_id="functionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert secret is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_unset(self, client: Zavudev) -> None:
        with client.functions.secrets.with_streaming_response.unset(
            key="key",
            function_id="functionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert secret is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_unset(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.functions.secrets.with_raw_response.unset(
                key="key",
                function_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.functions.secrets.with_raw_response.unset(
                key="",
                function_id="functionId",
            )


class TestAsyncSecrets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncZavudev) -> None:
        secret = await async_client.functions.secrets.list(
            "functionId",
        )
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncZavudev) -> None:
        response = await async_client.functions.secrets.with_raw_response.list(
            "functionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncZavudev) -> None:
        async with async_client.functions.secrets.with_streaming_response.list(
            "functionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(SecretListResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.functions.secrets.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set(self, async_client: AsyncZavudev) -> None:
        secret = await async_client.functions.secrets.set(
            key="key",
            function_id="functionId",
            value="value",
        )
        assert_matches_type(object, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_set(self, async_client: AsyncZavudev) -> None:
        response = await async_client.functions.secrets.with_raw_response.set(
            key="key",
            function_id="functionId",
            value="value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(object, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_set(self, async_client: AsyncZavudev) -> None:
        async with async_client.functions.secrets.with_streaming_response.set(
            key="key",
            function_id="functionId",
            value="value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(object, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_set(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.functions.secrets.with_raw_response.set(
                key="key",
                function_id="",
                value="value",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.functions.secrets.with_raw_response.set(
                key="",
                function_id="functionId",
                value="value",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unset(self, async_client: AsyncZavudev) -> None:
        secret = await async_client.functions.secrets.unset(
            key="key",
            function_id="functionId",
        )
        assert secret is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_unset(self, async_client: AsyncZavudev) -> None:
        response = await async_client.functions.secrets.with_raw_response.unset(
            key="key",
            function_id="functionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert secret is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_unset(self, async_client: AsyncZavudev) -> None:
        async with async_client.functions.secrets.with_streaming_response.unset(
            key="key",
            function_id="functionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert secret is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_unset(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.functions.secrets.with_raw_response.unset(
                key="key",
                function_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.functions.secrets.with_raw_response.unset(
                key="",
                function_id="functionId",
            )
