# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from zavudev import Zavudev, AsyncZavudev
from tests.utils import assert_matches_type
from zavudev.types import (
    RegulatoryDocument,
    RegulatoryDocumentCreateResponse,
    RegulatoryDocumentRetrieveResponse,
    RegulatoryDocumentUploadURLResponse,
)
from zavudev.pagination import SyncCursor, AsyncCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRegulatoryDocuments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Zavudev) -> None:
        regulatory_document = client.regulatory_documents.create(
            document_type="passport",
            file_size=102400,
            mime_type="image/jpeg",
            name="Passport Scan",
            storage_id="kg2abc123...",
        )
        assert_matches_type(RegulatoryDocumentCreateResponse, regulatory_document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Zavudev) -> None:
        response = client.regulatory_documents.with_raw_response.create(
            document_type="passport",
            file_size=102400,
            mime_type="image/jpeg",
            name="Passport Scan",
            storage_id="kg2abc123...",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        regulatory_document = response.parse()
        assert_matches_type(RegulatoryDocumentCreateResponse, regulatory_document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Zavudev) -> None:
        with client.regulatory_documents.with_streaming_response.create(
            document_type="passport",
            file_size=102400,
            mime_type="image/jpeg",
            name="Passport Scan",
            storage_id="kg2abc123...",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            regulatory_document = response.parse()
            assert_matches_type(RegulatoryDocumentCreateResponse, regulatory_document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Zavudev) -> None:
        regulatory_document = client.regulatory_documents.retrieve(
            "documentId",
        )
        assert_matches_type(RegulatoryDocumentRetrieveResponse, regulatory_document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Zavudev) -> None:
        response = client.regulatory_documents.with_raw_response.retrieve(
            "documentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        regulatory_document = response.parse()
        assert_matches_type(RegulatoryDocumentRetrieveResponse, regulatory_document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Zavudev) -> None:
        with client.regulatory_documents.with_streaming_response.retrieve(
            "documentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            regulatory_document = response.parse()
            assert_matches_type(RegulatoryDocumentRetrieveResponse, regulatory_document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            client.regulatory_documents.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Zavudev) -> None:
        regulatory_document = client.regulatory_documents.list()
        assert_matches_type(SyncCursor[RegulatoryDocument], regulatory_document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Zavudev) -> None:
        regulatory_document = client.regulatory_documents.list(
            cursor="cursor",
            limit=100,
        )
        assert_matches_type(SyncCursor[RegulatoryDocument], regulatory_document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Zavudev) -> None:
        response = client.regulatory_documents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        regulatory_document = response.parse()
        assert_matches_type(SyncCursor[RegulatoryDocument], regulatory_document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Zavudev) -> None:
        with client.regulatory_documents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            regulatory_document = response.parse()
            assert_matches_type(SyncCursor[RegulatoryDocument], regulatory_document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Zavudev) -> None:
        regulatory_document = client.regulatory_documents.delete(
            "documentId",
        )
        assert regulatory_document is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Zavudev) -> None:
        response = client.regulatory_documents.with_raw_response.delete(
            "documentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        regulatory_document = response.parse()
        assert regulatory_document is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Zavudev) -> None:
        with client.regulatory_documents.with_streaming_response.delete(
            "documentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            regulatory_document = response.parse()
            assert regulatory_document is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Zavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            client.regulatory_documents.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload_url(self, client: Zavudev) -> None:
        regulatory_document = client.regulatory_documents.upload_url()
        assert_matches_type(RegulatoryDocumentUploadURLResponse, regulatory_document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upload_url(self, client: Zavudev) -> None:
        response = client.regulatory_documents.with_raw_response.upload_url()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        regulatory_document = response.parse()
        assert_matches_type(RegulatoryDocumentUploadURLResponse, regulatory_document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upload_url(self, client: Zavudev) -> None:
        with client.regulatory_documents.with_streaming_response.upload_url() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            regulatory_document = response.parse()
            assert_matches_type(RegulatoryDocumentUploadURLResponse, regulatory_document, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRegulatoryDocuments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncZavudev) -> None:
        regulatory_document = await async_client.regulatory_documents.create(
            document_type="passport",
            file_size=102400,
            mime_type="image/jpeg",
            name="Passport Scan",
            storage_id="kg2abc123...",
        )
        assert_matches_type(RegulatoryDocumentCreateResponse, regulatory_document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncZavudev) -> None:
        response = await async_client.regulatory_documents.with_raw_response.create(
            document_type="passport",
            file_size=102400,
            mime_type="image/jpeg",
            name="Passport Scan",
            storage_id="kg2abc123...",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        regulatory_document = await response.parse()
        assert_matches_type(RegulatoryDocumentCreateResponse, regulatory_document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncZavudev) -> None:
        async with async_client.regulatory_documents.with_streaming_response.create(
            document_type="passport",
            file_size=102400,
            mime_type="image/jpeg",
            name="Passport Scan",
            storage_id="kg2abc123...",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            regulatory_document = await response.parse()
            assert_matches_type(RegulatoryDocumentCreateResponse, regulatory_document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncZavudev) -> None:
        regulatory_document = await async_client.regulatory_documents.retrieve(
            "documentId",
        )
        assert_matches_type(RegulatoryDocumentRetrieveResponse, regulatory_document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncZavudev) -> None:
        response = await async_client.regulatory_documents.with_raw_response.retrieve(
            "documentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        regulatory_document = await response.parse()
        assert_matches_type(RegulatoryDocumentRetrieveResponse, regulatory_document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncZavudev) -> None:
        async with async_client.regulatory_documents.with_streaming_response.retrieve(
            "documentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            regulatory_document = await response.parse()
            assert_matches_type(RegulatoryDocumentRetrieveResponse, regulatory_document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            await async_client.regulatory_documents.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncZavudev) -> None:
        regulatory_document = await async_client.regulatory_documents.list()
        assert_matches_type(AsyncCursor[RegulatoryDocument], regulatory_document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncZavudev) -> None:
        regulatory_document = await async_client.regulatory_documents.list(
            cursor="cursor",
            limit=100,
        )
        assert_matches_type(AsyncCursor[RegulatoryDocument], regulatory_document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncZavudev) -> None:
        response = await async_client.regulatory_documents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        regulatory_document = await response.parse()
        assert_matches_type(AsyncCursor[RegulatoryDocument], regulatory_document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncZavudev) -> None:
        async with async_client.regulatory_documents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            regulatory_document = await response.parse()
            assert_matches_type(AsyncCursor[RegulatoryDocument], regulatory_document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncZavudev) -> None:
        regulatory_document = await async_client.regulatory_documents.delete(
            "documentId",
        )
        assert regulatory_document is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncZavudev) -> None:
        response = await async_client.regulatory_documents.with_raw_response.delete(
            "documentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        regulatory_document = await response.parse()
        assert regulatory_document is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncZavudev) -> None:
        async with async_client.regulatory_documents.with_streaming_response.delete(
            "documentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            regulatory_document = await response.parse()
            assert regulatory_document is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncZavudev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            await async_client.regulatory_documents.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload_url(self, async_client: AsyncZavudev) -> None:
        regulatory_document = await async_client.regulatory_documents.upload_url()
        assert_matches_type(RegulatoryDocumentUploadURLResponse, regulatory_document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upload_url(self, async_client: AsyncZavudev) -> None:
        response = await async_client.regulatory_documents.with_raw_response.upload_url()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        regulatory_document = await response.parse()
        assert_matches_type(RegulatoryDocumentUploadURLResponse, regulatory_document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upload_url(self, async_client: AsyncZavudev) -> None:
        async with async_client.regulatory_documents.with_streaming_response.upload_url() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            regulatory_document = await response.parse()
            assert_matches_type(RegulatoryDocumentUploadURLResponse, regulatory_document, path=["response"])

        assert cast(Any, response.is_closed) is True
