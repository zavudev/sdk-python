# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from zavudev import Zavudev, AsyncZavudev
from tests.utils import assert_matches_type
from zavudev.types import IntrospectValidatePhoneResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIntrospect:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_validate_phone(self, client: Zavudev) -> None:
        introspect = client.introspect.validate_phone(
            phone_number="+56912345678",
        )
        assert_matches_type(IntrospectValidatePhoneResponse, introspect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_validate_phone(self, client: Zavudev) -> None:
        response = client.introspect.with_raw_response.validate_phone(
            phone_number="+56912345678",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        introspect = response.parse()
        assert_matches_type(IntrospectValidatePhoneResponse, introspect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_validate_phone(self, client: Zavudev) -> None:
        with client.introspect.with_streaming_response.validate_phone(
            phone_number="+56912345678",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            introspect = response.parse()
            assert_matches_type(IntrospectValidatePhoneResponse, introspect, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIntrospect:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_validate_phone(self, async_client: AsyncZavudev) -> None:
        introspect = await async_client.introspect.validate_phone(
            phone_number="+56912345678",
        )
        assert_matches_type(IntrospectValidatePhoneResponse, introspect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_validate_phone(self, async_client: AsyncZavudev) -> None:
        response = await async_client.introspect.with_raw_response.validate_phone(
            phone_number="+56912345678",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        introspect = await response.parse()
        assert_matches_type(IntrospectValidatePhoneResponse, introspect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_validate_phone(self, async_client: AsyncZavudev) -> None:
        async with async_client.introspect.with_streaming_response.validate_phone(
            phone_number="+56912345678",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            introspect = await response.parse()
            assert_matches_type(IntrospectValidatePhoneResponse, introspect, path=["response"])

        assert cast(Any, response.is_closed) is True
