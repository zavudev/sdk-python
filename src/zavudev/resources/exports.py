# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import export_list_params, export_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
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
from ..types.data_export import DataExport
from ..types.export_create_response import ExportCreateResponse
from ..types.export_retrieve_response import ExportRetrieveResponse

__all__ = ["ExportsResource", "AsyncExportsResource"]


class ExportsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return ExportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return ExportsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        data_types: List[Literal["messages", "conversations", "webhookDeliveries", "agentExecutions", "activities"]],
        date_from: Union[str, datetime] | Omit = omit,
        date_to: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExportCreateResponse:
        """Create a new data export job.

        The export will be processed asynchronously and
        the download URL will be available when status is 'completed'. Export links
        expire after 24 hours.

        Args:
          data_types: List of data types to include in the export.

          date_from: Start date for data to export (inclusive).

          date_to: End date for data to export (inclusive).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/exports",
            body=maybe_transform(
                {
                    "data_types": data_types,
                    "date_from": date_from,
                    "date_to": date_to,
                },
                export_create_params.ExportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExportCreateResponse,
        )

    def retrieve(
        self,
        export_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExportRetrieveResponse:
        """
        Get details of a specific data export, including download URL when completed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not export_id:
            raise ValueError(f"Expected a non-empty value for `export_id` but received {export_id!r}")
        return self._get(
            path_template("/v1/exports/{export_id}", export_id=export_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExportRetrieveResponse,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["pending", "processing", "completed", "failed"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursor[DataExport]:
        """
        List data exports for this project.

        Args:
          status: Status of a data export job.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/exports",
            page=SyncCursor[DataExport],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "status": status,
                    },
                    export_list_params.ExportListParams,
                ),
            ),
            model=DataExport,
        )


class AsyncExportsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return AsyncExportsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        data_types: List[Literal["messages", "conversations", "webhookDeliveries", "agentExecutions", "activities"]],
        date_from: Union[str, datetime] | Omit = omit,
        date_to: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExportCreateResponse:
        """Create a new data export job.

        The export will be processed asynchronously and
        the download URL will be available when status is 'completed'. Export links
        expire after 24 hours.

        Args:
          data_types: List of data types to include in the export.

          date_from: Start date for data to export (inclusive).

          date_to: End date for data to export (inclusive).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/exports",
            body=await async_maybe_transform(
                {
                    "data_types": data_types,
                    "date_from": date_from,
                    "date_to": date_to,
                },
                export_create_params.ExportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExportCreateResponse,
        )

    async def retrieve(
        self,
        export_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExportRetrieveResponse:
        """
        Get details of a specific data export, including download URL when completed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not export_id:
            raise ValueError(f"Expected a non-empty value for `export_id` but received {export_id!r}")
        return await self._get(
            path_template("/v1/exports/{export_id}", export_id=export_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExportRetrieveResponse,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["pending", "processing", "completed", "failed"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[DataExport, AsyncCursor[DataExport]]:
        """
        List data exports for this project.

        Args:
          status: Status of a data export job.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/exports",
            page=AsyncCursor[DataExport],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "status": status,
                    },
                    export_list_params.ExportListParams,
                ),
            ),
            model=DataExport,
        )


class ExportsResourceWithRawResponse:
    def __init__(self, exports: ExportsResource) -> None:
        self._exports = exports

        self.create = to_raw_response_wrapper(
            exports.create,
        )
        self.retrieve = to_raw_response_wrapper(
            exports.retrieve,
        )
        self.list = to_raw_response_wrapper(
            exports.list,
        )


class AsyncExportsResourceWithRawResponse:
    def __init__(self, exports: AsyncExportsResource) -> None:
        self._exports = exports

        self.create = async_to_raw_response_wrapper(
            exports.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            exports.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            exports.list,
        )


class ExportsResourceWithStreamingResponse:
    def __init__(self, exports: ExportsResource) -> None:
        self._exports = exports

        self.create = to_streamed_response_wrapper(
            exports.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            exports.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            exports.list,
        )


class AsyncExportsResourceWithStreamingResponse:
    def __init__(self, exports: AsyncExportsResource) -> None:
        self._exports = exports

        self.create = async_to_streamed_response_wrapper(
            exports.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            exports.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            exports.list,
        )
