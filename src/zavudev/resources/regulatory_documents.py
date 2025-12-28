# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import regulatory_document_list_params, regulatory_document_create_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncCursor, AsyncCursor
from .._base_client import AsyncPaginator, make_request_options
from ..types.regulatory_document import RegulatoryDocument
from ..types.regulatory_document_create_response import RegulatoryDocumentCreateResponse
from ..types.regulatory_document_retrieve_response import RegulatoryDocumentRetrieveResponse
from ..types.regulatory_document_upload_url_response import RegulatoryDocumentUploadURLResponse

__all__ = ["RegulatoryDocumentsResource", "AsyncRegulatoryDocumentsResource"]


class RegulatoryDocumentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RegulatoryDocumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return RegulatoryDocumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RegulatoryDocumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return RegulatoryDocumentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        document_type: Literal[
            "passport",
            "national_id",
            "drivers_license",
            "utility_bill",
            "tax_id",
            "business_registration",
            "proof_of_address",
            "other",
        ],
        file_size: int,
        mime_type: str,
        name: str,
        storage_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegulatoryDocumentCreateResponse:
        """Create a regulatory document record after uploading the file.

        Use the upload-url
        endpoint first to get an upload URL.

        Args:
          storage_id: Storage ID from the upload-url endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/documents",
            body=maybe_transform(
                {
                    "document_type": document_type,
                    "file_size": file_size,
                    "mime_type": mime_type,
                    "name": name,
                    "storage_id": storage_id,
                },
                regulatory_document_create_params.RegulatoryDocumentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegulatoryDocumentCreateResponse,
        )

    def retrieve(
        self,
        document_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegulatoryDocumentRetrieveResponse:
        """
        Get a specific regulatory document.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return self._get(
            f"/v1/documents/{document_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegulatoryDocumentRetrieveResponse,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursor[RegulatoryDocument]:
        """
        List regulatory documents for this project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/documents",
            page=SyncCursor[RegulatoryDocument],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    regulatory_document_list_params.RegulatoryDocumentListParams,
                ),
            ),
            model=RegulatoryDocument,
        )

    def delete(
        self,
        document_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a regulatory document.

        Cannot delete verified documents.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/documents/{document_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def upload_url(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegulatoryDocumentUploadURLResponse:
        """Get a presigned URL to upload a document file.

        After uploading, use the
        storageId to create the document record.
        """
        return self._post(
            "/v1/documents/upload-url",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegulatoryDocumentUploadURLResponse,
        )


class AsyncRegulatoryDocumentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRegulatoryDocumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRegulatoryDocumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRegulatoryDocumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return AsyncRegulatoryDocumentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        document_type: Literal[
            "passport",
            "national_id",
            "drivers_license",
            "utility_bill",
            "tax_id",
            "business_registration",
            "proof_of_address",
            "other",
        ],
        file_size: int,
        mime_type: str,
        name: str,
        storage_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegulatoryDocumentCreateResponse:
        """Create a regulatory document record after uploading the file.

        Use the upload-url
        endpoint first to get an upload URL.

        Args:
          storage_id: Storage ID from the upload-url endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/documents",
            body=await async_maybe_transform(
                {
                    "document_type": document_type,
                    "file_size": file_size,
                    "mime_type": mime_type,
                    "name": name,
                    "storage_id": storage_id,
                },
                regulatory_document_create_params.RegulatoryDocumentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegulatoryDocumentCreateResponse,
        )

    async def retrieve(
        self,
        document_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegulatoryDocumentRetrieveResponse:
        """
        Get a specific regulatory document.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return await self._get(
            f"/v1/documents/{document_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegulatoryDocumentRetrieveResponse,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[RegulatoryDocument, AsyncCursor[RegulatoryDocument]]:
        """
        List regulatory documents for this project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/documents",
            page=AsyncCursor[RegulatoryDocument],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    regulatory_document_list_params.RegulatoryDocumentListParams,
                ),
            ),
            model=RegulatoryDocument,
        )

    async def delete(
        self,
        document_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a regulatory document.

        Cannot delete verified documents.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/documents/{document_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def upload_url(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegulatoryDocumentUploadURLResponse:
        """Get a presigned URL to upload a document file.

        After uploading, use the
        storageId to create the document record.
        """
        return await self._post(
            "/v1/documents/upload-url",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegulatoryDocumentUploadURLResponse,
        )


class RegulatoryDocumentsResourceWithRawResponse:
    def __init__(self, regulatory_documents: RegulatoryDocumentsResource) -> None:
        self._regulatory_documents = regulatory_documents

        self.create = to_raw_response_wrapper(
            regulatory_documents.create,
        )
        self.retrieve = to_raw_response_wrapper(
            regulatory_documents.retrieve,
        )
        self.list = to_raw_response_wrapper(
            regulatory_documents.list,
        )
        self.delete = to_raw_response_wrapper(
            regulatory_documents.delete,
        )
        self.upload_url = to_raw_response_wrapper(
            regulatory_documents.upload_url,
        )


class AsyncRegulatoryDocumentsResourceWithRawResponse:
    def __init__(self, regulatory_documents: AsyncRegulatoryDocumentsResource) -> None:
        self._regulatory_documents = regulatory_documents

        self.create = async_to_raw_response_wrapper(
            regulatory_documents.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            regulatory_documents.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            regulatory_documents.list,
        )
        self.delete = async_to_raw_response_wrapper(
            regulatory_documents.delete,
        )
        self.upload_url = async_to_raw_response_wrapper(
            regulatory_documents.upload_url,
        )


class RegulatoryDocumentsResourceWithStreamingResponse:
    def __init__(self, regulatory_documents: RegulatoryDocumentsResource) -> None:
        self._regulatory_documents = regulatory_documents

        self.create = to_streamed_response_wrapper(
            regulatory_documents.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            regulatory_documents.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            regulatory_documents.list,
        )
        self.delete = to_streamed_response_wrapper(
            regulatory_documents.delete,
        )
        self.upload_url = to_streamed_response_wrapper(
            regulatory_documents.upload_url,
        )


class AsyncRegulatoryDocumentsResourceWithStreamingResponse:
    def __init__(self, regulatory_documents: AsyncRegulatoryDocumentsResource) -> None:
        self._regulatory_documents = regulatory_documents

        self.create = async_to_streamed_response_wrapper(
            regulatory_documents.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            regulatory_documents.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            regulatory_documents.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            regulatory_documents.delete,
        )
        self.upload_url = async_to_streamed_response_wrapper(
            regulatory_documents.upload_url,
        )
