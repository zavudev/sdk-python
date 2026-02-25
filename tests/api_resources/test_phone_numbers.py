# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from zavudev import Zavudev, AsyncZavudev
from tests.utils import assert_matches_type
from zavudev.types import (
    OwnedPhoneNumber,
    PhoneNumberUpdateResponse,
    PhoneNumberPurchaseResponse,
    PhoneNumberRetrieveResponse,
    PhoneNumberRequirementsResponse,
    PhoneNumberSearchAvailableResponse,
)
from zavudev.pagination import SyncCursor, AsyncCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPhoneNumbers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Zavudev) -> None:
        phone_number = client.phone_numbers.retrieve(
            "phoneNumberId",
        )
        assert_matches_type(PhoneNumberRetrieveResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Zavudev) -> None:
        response = client.phone_numbers.with_raw_response.retrieve(
            "phoneNumberId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert_matches_type(PhoneNumberRetrieveResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Zavudev) -> None:
        with client.phone_numbers.with_streaming_response.retrieve(
            "phoneNumberId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert_matches_type(PhoneNumberRetrieveResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number_id` but received ''"):
            client.phone_numbers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Zavudev) -> None:
        phone_number = client.phone_numbers.update(
            phone_number_id="phoneNumberId",
        )
        assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Zavudev) -> None:
        phone_number = client.phone_numbers.update(
            phone_number_id="phoneNumberId",
            name="Support Line",
            sender_id="senderId",
        )
        assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Zavudev) -> None:
        response = client.phone_numbers.with_raw_response.update(
            phone_number_id="phoneNumberId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Zavudev) -> None:
        with client.phone_numbers.with_streaming_response.update(
            phone_number_id="phoneNumberId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number_id` but received ''"):
            client.phone_numbers.with_raw_response.update(
                phone_number_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Zavudev) -> None:
        phone_number = client.phone_numbers.list()
        assert_matches_type(SyncCursor[OwnedPhoneNumber], phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Zavudev) -> None:
        phone_number = client.phone_numbers.list(
            cursor="cursor",
            limit=100,
            status="active",
        )
        assert_matches_type(SyncCursor[OwnedPhoneNumber], phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Zavudev) -> None:
        response = client.phone_numbers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert_matches_type(SyncCursor[OwnedPhoneNumber], phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Zavudev) -> None:
        with client.phone_numbers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert_matches_type(SyncCursor[OwnedPhoneNumber], phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_purchase(self, client: Zavudev) -> None:
        phone_number = client.phone_numbers.purchase(
            phone_number="+15551234567",
        )
        assert_matches_type(PhoneNumberPurchaseResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_purchase_with_all_params(self, client: Zavudev) -> None:
        phone_number = client.phone_numbers.purchase(
            phone_number="+15551234567",
            name="Primary Line",
        )
        assert_matches_type(PhoneNumberPurchaseResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_purchase(self, client: Zavudev) -> None:
        response = client.phone_numbers.with_raw_response.purchase(
            phone_number="+15551234567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert_matches_type(PhoneNumberPurchaseResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_purchase(self, client: Zavudev) -> None:
        with client.phone_numbers.with_streaming_response.purchase(
            phone_number="+15551234567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert_matches_type(PhoneNumberPurchaseResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_release(self, client: Zavudev) -> None:
        phone_number = client.phone_numbers.release(
            "phoneNumberId",
        )
        assert phone_number is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_release(self, client: Zavudev) -> None:
        response = client.phone_numbers.with_raw_response.release(
            "phoneNumberId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert phone_number is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_release(self, client: Zavudev) -> None:
        with client.phone_numbers.with_streaming_response.release(
            "phoneNumberId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert phone_number is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_release(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number_id` but received ''"):
            client.phone_numbers.with_raw_response.release(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_requirements(self, client: Zavudev) -> None:
        phone_number = client.phone_numbers.requirements(
            country_code="xx",
        )
        assert_matches_type(PhoneNumberRequirementsResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_requirements_with_all_params(self, client: Zavudev) -> None:
        phone_number = client.phone_numbers.requirements(
            country_code="xx",
            type="local",
        )
        assert_matches_type(PhoneNumberRequirementsResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_requirements(self, client: Zavudev) -> None:
        response = client.phone_numbers.with_raw_response.requirements(
            country_code="xx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert_matches_type(PhoneNumberRequirementsResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_requirements(self, client: Zavudev) -> None:
        with client.phone_numbers.with_streaming_response.requirements(
            country_code="xx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert_matches_type(PhoneNumberRequirementsResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_available(self, client: Zavudev) -> None:
        phone_number = client.phone_numbers.search_available(
            country_code="xx",
        )
        assert_matches_type(PhoneNumberSearchAvailableResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_available_with_all_params(self, client: Zavudev) -> None:
        phone_number = client.phone_numbers.search_available(
            country_code="xx",
            contains="contains",
            limit=50,
            type="local",
        )
        assert_matches_type(PhoneNumberSearchAvailableResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search_available(self, client: Zavudev) -> None:
        response = client.phone_numbers.with_raw_response.search_available(
            country_code="xx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert_matches_type(PhoneNumberSearchAvailableResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search_available(self, client: Zavudev) -> None:
        with client.phone_numbers.with_streaming_response.search_available(
            country_code="xx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert_matches_type(PhoneNumberSearchAvailableResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPhoneNumbers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncZavudev) -> None:
        phone_number = await async_client.phone_numbers.retrieve(
            "phoneNumberId",
        )
        assert_matches_type(PhoneNumberRetrieveResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncZavudev) -> None:
        response = await async_client.phone_numbers.with_raw_response.retrieve(
            "phoneNumberId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert_matches_type(PhoneNumberRetrieveResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncZavudev) -> None:
        async with async_client.phone_numbers.with_streaming_response.retrieve(
            "phoneNumberId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert_matches_type(PhoneNumberRetrieveResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number_id` but received ''"):
            await async_client.phone_numbers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncZavudev) -> None:
        phone_number = await async_client.phone_numbers.update(
            phone_number_id="phoneNumberId",
        )
        assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncZavudev) -> None:
        phone_number = await async_client.phone_numbers.update(
            phone_number_id="phoneNumberId",
            name="Support Line",
            sender_id="senderId",
        )
        assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncZavudev) -> None:
        response = await async_client.phone_numbers.with_raw_response.update(
            phone_number_id="phoneNumberId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncZavudev) -> None:
        async with async_client.phone_numbers.with_streaming_response.update(
            phone_number_id="phoneNumberId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number_id` but received ''"):
            await async_client.phone_numbers.with_raw_response.update(
                phone_number_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncZavudev) -> None:
        phone_number = await async_client.phone_numbers.list()
        assert_matches_type(AsyncCursor[OwnedPhoneNumber], phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncZavudev) -> None:
        phone_number = await async_client.phone_numbers.list(
            cursor="cursor",
            limit=100,
            status="active",
        )
        assert_matches_type(AsyncCursor[OwnedPhoneNumber], phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncZavudev) -> None:
        response = await async_client.phone_numbers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert_matches_type(AsyncCursor[OwnedPhoneNumber], phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncZavudev) -> None:
        async with async_client.phone_numbers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert_matches_type(AsyncCursor[OwnedPhoneNumber], phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_purchase(self, async_client: AsyncZavudev) -> None:
        phone_number = await async_client.phone_numbers.purchase(
            phone_number="+15551234567",
        )
        assert_matches_type(PhoneNumberPurchaseResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_purchase_with_all_params(self, async_client: AsyncZavudev) -> None:
        phone_number = await async_client.phone_numbers.purchase(
            phone_number="+15551234567",
            name="Primary Line",
        )
        assert_matches_type(PhoneNumberPurchaseResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_purchase(self, async_client: AsyncZavudev) -> None:
        response = await async_client.phone_numbers.with_raw_response.purchase(
            phone_number="+15551234567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert_matches_type(PhoneNumberPurchaseResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_purchase(self, async_client: AsyncZavudev) -> None:
        async with async_client.phone_numbers.with_streaming_response.purchase(
            phone_number="+15551234567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert_matches_type(PhoneNumberPurchaseResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_release(self, async_client: AsyncZavudev) -> None:
        phone_number = await async_client.phone_numbers.release(
            "phoneNumberId",
        )
        assert phone_number is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_release(self, async_client: AsyncZavudev) -> None:
        response = await async_client.phone_numbers.with_raw_response.release(
            "phoneNumberId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert phone_number is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_release(self, async_client: AsyncZavudev) -> None:
        async with async_client.phone_numbers.with_streaming_response.release(
            "phoneNumberId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert phone_number is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_release(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number_id` but received ''"):
            await async_client.phone_numbers.with_raw_response.release(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_requirements(self, async_client: AsyncZavudev) -> None:
        phone_number = await async_client.phone_numbers.requirements(
            country_code="xx",
        )
        assert_matches_type(PhoneNumberRequirementsResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_requirements_with_all_params(self, async_client: AsyncZavudev) -> None:
        phone_number = await async_client.phone_numbers.requirements(
            country_code="xx",
            type="local",
        )
        assert_matches_type(PhoneNumberRequirementsResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_requirements(self, async_client: AsyncZavudev) -> None:
        response = await async_client.phone_numbers.with_raw_response.requirements(
            country_code="xx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert_matches_type(PhoneNumberRequirementsResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_requirements(self, async_client: AsyncZavudev) -> None:
        async with async_client.phone_numbers.with_streaming_response.requirements(
            country_code="xx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert_matches_type(PhoneNumberRequirementsResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_available(self, async_client: AsyncZavudev) -> None:
        phone_number = await async_client.phone_numbers.search_available(
            country_code="xx",
        )
        assert_matches_type(PhoneNumberSearchAvailableResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_available_with_all_params(self, async_client: AsyncZavudev) -> None:
        phone_number = await async_client.phone_numbers.search_available(
            country_code="xx",
            contains="contains",
            limit=50,
            type="local",
        )
        assert_matches_type(PhoneNumberSearchAvailableResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search_available(self, async_client: AsyncZavudev) -> None:
        response = await async_client.phone_numbers.with_raw_response.search_available(
            country_code="xx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert_matches_type(PhoneNumberSearchAvailableResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search_available(self, async_client: AsyncZavudev) -> None:
        async with async_client.phone_numbers.with_streaming_response.search_available(
            country_code="xx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert_matches_type(PhoneNumberSearchAvailableResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True
