# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from zavudev import Zavudev, AsyncZavudev
from tests.utils import assert_matches_type
from zavudev.types import (
    EmailDomainListResponse,
    EmailDomainCreateResponse,
    EmailDomainVerifyResponse,
    EmailDomainRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmailDomains:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Zavudev) -> None:
        email_domain = client.email_domains.create(
            domain="example.com",
        )
        assert_matches_type(EmailDomainCreateResponse, email_domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Zavudev) -> None:
        response = client.email_domains.with_raw_response.create(
            domain="example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_domain = response.parse()
        assert_matches_type(EmailDomainCreateResponse, email_domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Zavudev) -> None:
        with client.email_domains.with_streaming_response.create(
            domain="example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_domain = response.parse()
            assert_matches_type(EmailDomainCreateResponse, email_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Zavudev) -> None:
        email_domain = client.email_domains.retrieve(
            "domainId",
        )
        assert_matches_type(EmailDomainRetrieveResponse, email_domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Zavudev) -> None:
        response = client.email_domains.with_raw_response.retrieve(
            "domainId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_domain = response.parse()
        assert_matches_type(EmailDomainRetrieveResponse, email_domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Zavudev) -> None:
        with client.email_domains.with_streaming_response.retrieve(
            "domainId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_domain = response.parse()
            assert_matches_type(EmailDomainRetrieveResponse, email_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_id` but received ''"):
            client.email_domains.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Zavudev) -> None:
        email_domain = client.email_domains.list()
        assert_matches_type(EmailDomainListResponse, email_domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Zavudev) -> None:
        response = client.email_domains.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_domain = response.parse()
        assert_matches_type(EmailDomainListResponse, email_domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Zavudev) -> None:
        with client.email_domains.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_domain = response.parse()
            assert_matches_type(EmailDomainListResponse, email_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Zavudev) -> None:
        email_domain = client.email_domains.delete(
            "domainId",
        )
        assert email_domain is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Zavudev) -> None:
        response = client.email_domains.with_raw_response.delete(
            "domainId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_domain = response.parse()
        assert email_domain is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Zavudev) -> None:
        with client.email_domains.with_streaming_response.delete(
            "domainId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_domain = response.parse()
            assert email_domain is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_id` but received ''"):
            client.email_domains.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_verify(self, client: Zavudev) -> None:
        email_domain = client.email_domains.verify(
            "domainId",
        )
        assert_matches_type(EmailDomainVerifyResponse, email_domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_verify(self, client: Zavudev) -> None:
        response = client.email_domains.with_raw_response.verify(
            "domainId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_domain = response.parse()
        assert_matches_type(EmailDomainVerifyResponse, email_domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_verify(self, client: Zavudev) -> None:
        with client.email_domains.with_streaming_response.verify(
            "domainId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_domain = response.parse()
            assert_matches_type(EmailDomainVerifyResponse, email_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_verify(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_id` but received ''"):
            client.email_domains.with_raw_response.verify(
                "",
            )


class TestAsyncEmailDomains:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncZavudev) -> None:
        email_domain = await async_client.email_domains.create(
            domain="example.com",
        )
        assert_matches_type(EmailDomainCreateResponse, email_domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncZavudev) -> None:
        response = await async_client.email_domains.with_raw_response.create(
            domain="example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_domain = await response.parse()
        assert_matches_type(EmailDomainCreateResponse, email_domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncZavudev) -> None:
        async with async_client.email_domains.with_streaming_response.create(
            domain="example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_domain = await response.parse()
            assert_matches_type(EmailDomainCreateResponse, email_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncZavudev) -> None:
        email_domain = await async_client.email_domains.retrieve(
            "domainId",
        )
        assert_matches_type(EmailDomainRetrieveResponse, email_domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncZavudev) -> None:
        response = await async_client.email_domains.with_raw_response.retrieve(
            "domainId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_domain = await response.parse()
        assert_matches_type(EmailDomainRetrieveResponse, email_domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncZavudev) -> None:
        async with async_client.email_domains.with_streaming_response.retrieve(
            "domainId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_domain = await response.parse()
            assert_matches_type(EmailDomainRetrieveResponse, email_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_id` but received ''"):
            await async_client.email_domains.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncZavudev) -> None:
        email_domain = await async_client.email_domains.list()
        assert_matches_type(EmailDomainListResponse, email_domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncZavudev) -> None:
        response = await async_client.email_domains.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_domain = await response.parse()
        assert_matches_type(EmailDomainListResponse, email_domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncZavudev) -> None:
        async with async_client.email_domains.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_domain = await response.parse()
            assert_matches_type(EmailDomainListResponse, email_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncZavudev) -> None:
        email_domain = await async_client.email_domains.delete(
            "domainId",
        )
        assert email_domain is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncZavudev) -> None:
        response = await async_client.email_domains.with_raw_response.delete(
            "domainId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_domain = await response.parse()
        assert email_domain is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncZavudev) -> None:
        async with async_client.email_domains.with_streaming_response.delete(
            "domainId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_domain = await response.parse()
            assert email_domain is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_id` but received ''"):
            await async_client.email_domains.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_verify(self, async_client: AsyncZavudev) -> None:
        email_domain = await async_client.email_domains.verify(
            "domainId",
        )
        assert_matches_type(EmailDomainVerifyResponse, email_domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_verify(self, async_client: AsyncZavudev) -> None:
        response = await async_client.email_domains.with_raw_response.verify(
            "domainId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_domain = await response.parse()
        assert_matches_type(EmailDomainVerifyResponse, email_domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_verify(self, async_client: AsyncZavudev) -> None:
        async with async_client.email_domains.with_streaming_response.verify(
            "domainId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_domain = await response.parse()
            assert_matches_type(EmailDomainVerifyResponse, email_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_verify(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_id` but received ''"):
            await async_client.email_domains.with_raw_response.verify(
                "",
            )
