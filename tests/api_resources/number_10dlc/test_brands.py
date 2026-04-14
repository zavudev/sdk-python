# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from zavudev import Zavudev, AsyncZavudev
from tests.utils import assert_matches_type
from zavudev.pagination import SyncCursor, AsyncCursor
from zavudev.types.number_10dlc import (
    TenDlcBrand,
    BrandCreateResponse,
    BrandSubmitResponse,
    BrandUpdateResponse,
    BrandRetrieveResponse,
    BrandSyncStatusResponse,
    BrandListUseCasesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBrands:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Zavudev) -> None:
        brand = client.number_10dlc.brands.create(
            city="San Francisco",
            country="US",
            display_name="Acme Corp",
            email="compliance@acme.com",
            entity_type="PRIVATE_PROFIT",
            phone="+14155551234",
            postal_code="94102",
            state="CA",
            street="123 Main St",
            vertical="Technology",
        )
        assert_matches_type(BrandCreateResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Zavudev) -> None:
        brand = client.number_10dlc.brands.create(
            city="San Francisco",
            country="US",
            display_name="Acme Corp",
            email="compliance@acme.com",
            entity_type="PRIVATE_PROFIT",
            phone="+14155551234",
            postal_code="94102",
            state="CA",
            street="123 Main St",
            vertical="Technology",
            company_name="Acme Corporation",
            ein="12-3456789",
            first_name="firstName",
            last_name="lastName",
            stock_exchange="stockExchange",
            stock_symbol="stockSymbol",
            website="https://acme.com",
        )
        assert_matches_type(BrandCreateResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Zavudev) -> None:
        response = client.number_10dlc.brands.with_raw_response.create(
            city="San Francisco",
            country="US",
            display_name="Acme Corp",
            email="compliance@acme.com",
            entity_type="PRIVATE_PROFIT",
            phone="+14155551234",
            postal_code="94102",
            state="CA",
            street="123 Main St",
            vertical="Technology",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(BrandCreateResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Zavudev) -> None:
        with client.number_10dlc.brands.with_streaming_response.create(
            city="San Francisco",
            country="US",
            display_name="Acme Corp",
            email="compliance@acme.com",
            entity_type="PRIVATE_PROFIT",
            phone="+14155551234",
            postal_code="94102",
            state="CA",
            street="123 Main St",
            vertical="Technology",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(BrandCreateResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Zavudev) -> None:
        brand = client.number_10dlc.brands.retrieve(
            "brandId",
        )
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Zavudev) -> None:
        response = client.number_10dlc.brands.with_raw_response.retrieve(
            "brandId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Zavudev) -> None:
        with client.number_10dlc.brands.with_streaming_response.retrieve(
            "brandId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            client.number_10dlc.brands.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Zavudev) -> None:
        brand = client.number_10dlc.brands.update(
            brand_id="brandId",
        )
        assert_matches_type(BrandUpdateResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Zavudev) -> None:
        brand = client.number_10dlc.brands.update(
            brand_id="brandId",
            city="city",
            company_name="companyName",
            country="xx",
            display_name="displayName",
            ein="ein",
            email="dev@stainless.com",
            entity_type="PRIVATE_PROFIT",
            first_name="firstName",
            last_name="lastName",
            phone="phone",
            postal_code="postalCode",
            state="state",
            stock_exchange="stockExchange",
            stock_symbol="stockSymbol",
            street="street",
            vertical="vertical",
            website="https://example.com",
        )
        assert_matches_type(BrandUpdateResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Zavudev) -> None:
        response = client.number_10dlc.brands.with_raw_response.update(
            brand_id="brandId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(BrandUpdateResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Zavudev) -> None:
        with client.number_10dlc.brands.with_streaming_response.update(
            brand_id="brandId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(BrandUpdateResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            client.number_10dlc.brands.with_raw_response.update(
                brand_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Zavudev) -> None:
        brand = client.number_10dlc.brands.list()
        assert_matches_type(SyncCursor[TenDlcBrand], brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Zavudev) -> None:
        brand = client.number_10dlc.brands.list(
            cursor="cursor",
            limit=100,
        )
        assert_matches_type(SyncCursor[TenDlcBrand], brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Zavudev) -> None:
        response = client.number_10dlc.brands.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(SyncCursor[TenDlcBrand], brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Zavudev) -> None:
        with client.number_10dlc.brands.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(SyncCursor[TenDlcBrand], brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Zavudev) -> None:
        brand = client.number_10dlc.brands.delete(
            "brandId",
        )
        assert brand is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Zavudev) -> None:
        response = client.number_10dlc.brands.with_raw_response.delete(
            "brandId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert brand is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Zavudev) -> None:
        with client.number_10dlc.brands.with_streaming_response.delete(
            "brandId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert brand is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            client.number_10dlc.brands.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_use_cases(self, client: Zavudev) -> None:
        brand = client.number_10dlc.brands.list_use_cases()
        assert_matches_type(BrandListUseCasesResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_use_cases(self, client: Zavudev) -> None:
        response = client.number_10dlc.brands.with_raw_response.list_use_cases()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(BrandListUseCasesResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_use_cases(self, client: Zavudev) -> None:
        with client.number_10dlc.brands.with_streaming_response.list_use_cases() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(BrandListUseCasesResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit(self, client: Zavudev) -> None:
        brand = client.number_10dlc.brands.submit(
            "brandId",
        )
        assert_matches_type(BrandSubmitResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_submit(self, client: Zavudev) -> None:
        response = client.number_10dlc.brands.with_raw_response.submit(
            "brandId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(BrandSubmitResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_submit(self, client: Zavudev) -> None:
        with client.number_10dlc.brands.with_streaming_response.submit(
            "brandId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(BrandSubmitResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_submit(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            client.number_10dlc.brands.with_raw_response.submit(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_sync_status(self, client: Zavudev) -> None:
        brand = client.number_10dlc.brands.sync_status(
            "brandId",
        )
        assert_matches_type(BrandSyncStatusResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_sync_status(self, client: Zavudev) -> None:
        response = client.number_10dlc.brands.with_raw_response.sync_status(
            "brandId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(BrandSyncStatusResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_sync_status(self, client: Zavudev) -> None:
        with client.number_10dlc.brands.with_streaming_response.sync_status(
            "brandId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(BrandSyncStatusResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_sync_status(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            client.number_10dlc.brands.with_raw_response.sync_status(
                "",
            )


class TestAsyncBrands:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncZavudev) -> None:
        brand = await async_client.number_10dlc.brands.create(
            city="San Francisco",
            country="US",
            display_name="Acme Corp",
            email="compliance@acme.com",
            entity_type="PRIVATE_PROFIT",
            phone="+14155551234",
            postal_code="94102",
            state="CA",
            street="123 Main St",
            vertical="Technology",
        )
        assert_matches_type(BrandCreateResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncZavudev) -> None:
        brand = await async_client.number_10dlc.brands.create(
            city="San Francisco",
            country="US",
            display_name="Acme Corp",
            email="compliance@acme.com",
            entity_type="PRIVATE_PROFIT",
            phone="+14155551234",
            postal_code="94102",
            state="CA",
            street="123 Main St",
            vertical="Technology",
            company_name="Acme Corporation",
            ein="12-3456789",
            first_name="firstName",
            last_name="lastName",
            stock_exchange="stockExchange",
            stock_symbol="stockSymbol",
            website="https://acme.com",
        )
        assert_matches_type(BrandCreateResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncZavudev) -> None:
        response = await async_client.number_10dlc.brands.with_raw_response.create(
            city="San Francisco",
            country="US",
            display_name="Acme Corp",
            email="compliance@acme.com",
            entity_type="PRIVATE_PROFIT",
            phone="+14155551234",
            postal_code="94102",
            state="CA",
            street="123 Main St",
            vertical="Technology",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(BrandCreateResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncZavudev) -> None:
        async with async_client.number_10dlc.brands.with_streaming_response.create(
            city="San Francisco",
            country="US",
            display_name="Acme Corp",
            email="compliance@acme.com",
            entity_type="PRIVATE_PROFIT",
            phone="+14155551234",
            postal_code="94102",
            state="CA",
            street="123 Main St",
            vertical="Technology",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(BrandCreateResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncZavudev) -> None:
        brand = await async_client.number_10dlc.brands.retrieve(
            "brandId",
        )
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncZavudev) -> None:
        response = await async_client.number_10dlc.brands.with_raw_response.retrieve(
            "brandId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncZavudev) -> None:
        async with async_client.number_10dlc.brands.with_streaming_response.retrieve(
            "brandId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            await async_client.number_10dlc.brands.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncZavudev) -> None:
        brand = await async_client.number_10dlc.brands.update(
            brand_id="brandId",
        )
        assert_matches_type(BrandUpdateResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncZavudev) -> None:
        brand = await async_client.number_10dlc.brands.update(
            brand_id="brandId",
            city="city",
            company_name="companyName",
            country="xx",
            display_name="displayName",
            ein="ein",
            email="dev@stainless.com",
            entity_type="PRIVATE_PROFIT",
            first_name="firstName",
            last_name="lastName",
            phone="phone",
            postal_code="postalCode",
            state="state",
            stock_exchange="stockExchange",
            stock_symbol="stockSymbol",
            street="street",
            vertical="vertical",
            website="https://example.com",
        )
        assert_matches_type(BrandUpdateResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncZavudev) -> None:
        response = await async_client.number_10dlc.brands.with_raw_response.update(
            brand_id="brandId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(BrandUpdateResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncZavudev) -> None:
        async with async_client.number_10dlc.brands.with_streaming_response.update(
            brand_id="brandId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(BrandUpdateResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            await async_client.number_10dlc.brands.with_raw_response.update(
                brand_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncZavudev) -> None:
        brand = await async_client.number_10dlc.brands.list()
        assert_matches_type(AsyncCursor[TenDlcBrand], brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncZavudev) -> None:
        brand = await async_client.number_10dlc.brands.list(
            cursor="cursor",
            limit=100,
        )
        assert_matches_type(AsyncCursor[TenDlcBrand], brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncZavudev) -> None:
        response = await async_client.number_10dlc.brands.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(AsyncCursor[TenDlcBrand], brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncZavudev) -> None:
        async with async_client.number_10dlc.brands.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(AsyncCursor[TenDlcBrand], brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncZavudev) -> None:
        brand = await async_client.number_10dlc.brands.delete(
            "brandId",
        )
        assert brand is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncZavudev) -> None:
        response = await async_client.number_10dlc.brands.with_raw_response.delete(
            "brandId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert brand is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncZavudev) -> None:
        async with async_client.number_10dlc.brands.with_streaming_response.delete(
            "brandId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert brand is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            await async_client.number_10dlc.brands.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_use_cases(self, async_client: AsyncZavudev) -> None:
        brand = await async_client.number_10dlc.brands.list_use_cases()
        assert_matches_type(BrandListUseCasesResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_use_cases(self, async_client: AsyncZavudev) -> None:
        response = await async_client.number_10dlc.brands.with_raw_response.list_use_cases()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(BrandListUseCasesResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_use_cases(self, async_client: AsyncZavudev) -> None:
        async with async_client.number_10dlc.brands.with_streaming_response.list_use_cases() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(BrandListUseCasesResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit(self, async_client: AsyncZavudev) -> None:
        brand = await async_client.number_10dlc.brands.submit(
            "brandId",
        )
        assert_matches_type(BrandSubmitResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_submit(self, async_client: AsyncZavudev) -> None:
        response = await async_client.number_10dlc.brands.with_raw_response.submit(
            "brandId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(BrandSubmitResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_submit(self, async_client: AsyncZavudev) -> None:
        async with async_client.number_10dlc.brands.with_streaming_response.submit(
            "brandId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(BrandSubmitResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_submit(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            await async_client.number_10dlc.brands.with_raw_response.submit(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_sync_status(self, async_client: AsyncZavudev) -> None:
        brand = await async_client.number_10dlc.brands.sync_status(
            "brandId",
        )
        assert_matches_type(BrandSyncStatusResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_sync_status(self, async_client: AsyncZavudev) -> None:
        response = await async_client.number_10dlc.brands.with_raw_response.sync_status(
            "brandId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(BrandSyncStatusResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_sync_status(self, async_client: AsyncZavudev) -> None:
        async with async_client.number_10dlc.brands.with_streaming_response.sync_status(
            "brandId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(BrandSyncStatusResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_sync_status(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            await async_client.number_10dlc.brands.with_raw_response.sync_status(
                "",
            )
