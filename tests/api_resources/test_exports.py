# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from zavudev import Zavudev, AsyncZavudev
from tests.utils import assert_matches_type
from zavudev.types import (
    DataExport,
    ExportCreateResponse,
    ExportRetrieveResponse,
)
from zavudev._utils import parse_datetime
from zavudev.pagination import SyncCursor, AsyncCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExports:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Zavudev) -> None:
        export = client.exports.create(
            data_types=["messages", "conversations"],
        )
        assert_matches_type(ExportCreateResponse, export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Zavudev) -> None:
        export = client.exports.create(
            data_types=["messages", "conversations"],
            date_from=parse_datetime("2024-01-01T00:00:00Z"),
            date_to=parse_datetime("2024-12-31T23:59:59Z"),
        )
        assert_matches_type(ExportCreateResponse, export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Zavudev) -> None:
        response = client.exports.with_raw_response.create(
            data_types=["messages", "conversations"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = response.parse()
        assert_matches_type(ExportCreateResponse, export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Zavudev) -> None:
        with client.exports.with_streaming_response.create(
            data_types=["messages", "conversations"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = response.parse()
            assert_matches_type(ExportCreateResponse, export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Zavudev) -> None:
        export = client.exports.retrieve(
            "exportId",
        )
        assert_matches_type(ExportRetrieveResponse, export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Zavudev) -> None:
        response = client.exports.with_raw_response.retrieve(
            "exportId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = response.parse()
        assert_matches_type(ExportRetrieveResponse, export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Zavudev) -> None:
        with client.exports.with_streaming_response.retrieve(
            "exportId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = response.parse()
            assert_matches_type(ExportRetrieveResponse, export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `export_id` but received ''"):
            client.exports.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Zavudev) -> None:
        export = client.exports.list()
        assert_matches_type(SyncCursor[DataExport], export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Zavudev) -> None:
        export = client.exports.list(
            cursor="cursor",
            limit=100,
            status="pending",
        )
        assert_matches_type(SyncCursor[DataExport], export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Zavudev) -> None:
        response = client.exports.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = response.parse()
        assert_matches_type(SyncCursor[DataExport], export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Zavudev) -> None:
        with client.exports.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = response.parse()
            assert_matches_type(SyncCursor[DataExport], export, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExports:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncZavudev) -> None:
        export = await async_client.exports.create(
            data_types=["messages", "conversations"],
        )
        assert_matches_type(ExportCreateResponse, export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncZavudev) -> None:
        export = await async_client.exports.create(
            data_types=["messages", "conversations"],
            date_from=parse_datetime("2024-01-01T00:00:00Z"),
            date_to=parse_datetime("2024-12-31T23:59:59Z"),
        )
        assert_matches_type(ExportCreateResponse, export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncZavudev) -> None:
        response = await async_client.exports.with_raw_response.create(
            data_types=["messages", "conversations"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = await response.parse()
        assert_matches_type(ExportCreateResponse, export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncZavudev) -> None:
        async with async_client.exports.with_streaming_response.create(
            data_types=["messages", "conversations"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = await response.parse()
            assert_matches_type(ExportCreateResponse, export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncZavudev) -> None:
        export = await async_client.exports.retrieve(
            "exportId",
        )
        assert_matches_type(ExportRetrieveResponse, export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncZavudev) -> None:
        response = await async_client.exports.with_raw_response.retrieve(
            "exportId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = await response.parse()
        assert_matches_type(ExportRetrieveResponse, export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncZavudev) -> None:
        async with async_client.exports.with_streaming_response.retrieve(
            "exportId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = await response.parse()
            assert_matches_type(ExportRetrieveResponse, export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `export_id` but received ''"):
            await async_client.exports.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncZavudev) -> None:
        export = await async_client.exports.list()
        assert_matches_type(AsyncCursor[DataExport], export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncZavudev) -> None:
        export = await async_client.exports.list(
            cursor="cursor",
            limit=100,
            status="pending",
        )
        assert_matches_type(AsyncCursor[DataExport], export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncZavudev) -> None:
        response = await async_client.exports.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = await response.parse()
        assert_matches_type(AsyncCursor[DataExport], export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncZavudev) -> None:
        async with async_client.exports.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = await response.parse()
            assert_matches_type(AsyncCursor[DataExport], export, path=["response"])

        assert cast(Any, response.is_closed) is True
