# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import url_list_verified_params, url_submit_for_verification_params
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
from ..types.verified_url import VerifiedURL
from ..types.url_retrieve_details_response import URLRetrieveDetailsResponse
from ..types.url_submit_for_verification_response import URLSubmitForVerificationResponse

__all__ = ["URLsResource", "AsyncURLsResource"]


class URLsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> URLsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return URLsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> URLsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return URLsResourceWithStreamingResponse(self)

    def list_verified(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["pending", "approved", "rejected", "malicious"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursor[VerifiedURL]:
        """
        List URLs that have been verified for this project.

        Args:
          status: Filter by verification status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/urls",
            page=SyncCursor[VerifiedURL],
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
                    url_list_verified_params.URLListVerifiedParams,
                ),
            ),
            model=VerifiedURL,
        )

    def retrieve_details(
        self,
        url_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> URLRetrieveDetailsResponse:
        """
        Get details of a specific verified URL.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not url_id:
            raise ValueError(f"Expected a non-empty value for `url_id` but received {url_id!r}")
        return self._get(
            path_template("/v1/urls/{url_id}", url_id=url_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLRetrieveDetailsResponse,
        )

    def submit_for_verification(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> URLSubmitForVerificationResponse:
        """Submit a URL for verification.

        URLs are automatically checked against Google Web
        Risk API. Safe URLs are auto-approved, malicious URLs are blocked. URL
        shorteners (bit.ly, t.co, etc.) are always blocked.

        **Important:** All SMS and Email messages containing URLs require those URLs to
        be verified before the message can be sent. This endpoint allows
        pre-verification of URLs.

        Args:
          url: The URL to submit for verification.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/urls",
            body=maybe_transform({"url": url}, url_submit_for_verification_params.URLSubmitForVerificationParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLSubmitForVerificationResponse,
        )


class AsyncURLsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncURLsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncURLsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncURLsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return AsyncURLsResourceWithStreamingResponse(self)

    def list_verified(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["pending", "approved", "rejected", "malicious"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[VerifiedURL, AsyncCursor[VerifiedURL]]:
        """
        List URLs that have been verified for this project.

        Args:
          status: Filter by verification status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/urls",
            page=AsyncCursor[VerifiedURL],
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
                    url_list_verified_params.URLListVerifiedParams,
                ),
            ),
            model=VerifiedURL,
        )

    async def retrieve_details(
        self,
        url_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> URLRetrieveDetailsResponse:
        """
        Get details of a specific verified URL.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not url_id:
            raise ValueError(f"Expected a non-empty value for `url_id` but received {url_id!r}")
        return await self._get(
            path_template("/v1/urls/{url_id}", url_id=url_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLRetrieveDetailsResponse,
        )

    async def submit_for_verification(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> URLSubmitForVerificationResponse:
        """Submit a URL for verification.

        URLs are automatically checked against Google Web
        Risk API. Safe URLs are auto-approved, malicious URLs are blocked. URL
        shorteners (bit.ly, t.co, etc.) are always blocked.

        **Important:** All SMS and Email messages containing URLs require those URLs to
        be verified before the message can be sent. This endpoint allows
        pre-verification of URLs.

        Args:
          url: The URL to submit for verification.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/urls",
            body=await async_maybe_transform(
                {"url": url}, url_submit_for_verification_params.URLSubmitForVerificationParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLSubmitForVerificationResponse,
        )


class URLsResourceWithRawResponse:
    def __init__(self, urls: URLsResource) -> None:
        self._urls = urls

        self.list_verified = to_raw_response_wrapper(
            urls.list_verified,
        )
        self.retrieve_details = to_raw_response_wrapper(
            urls.retrieve_details,
        )
        self.submit_for_verification = to_raw_response_wrapper(
            urls.submit_for_verification,
        )


class AsyncURLsResourceWithRawResponse:
    def __init__(self, urls: AsyncURLsResource) -> None:
        self._urls = urls

        self.list_verified = async_to_raw_response_wrapper(
            urls.list_verified,
        )
        self.retrieve_details = async_to_raw_response_wrapper(
            urls.retrieve_details,
        )
        self.submit_for_verification = async_to_raw_response_wrapper(
            urls.submit_for_verification,
        )


class URLsResourceWithStreamingResponse:
    def __init__(self, urls: URLsResource) -> None:
        self._urls = urls

        self.list_verified = to_streamed_response_wrapper(
            urls.list_verified,
        )
        self.retrieve_details = to_streamed_response_wrapper(
            urls.retrieve_details,
        )
        self.submit_for_verification = to_streamed_response_wrapper(
            urls.submit_for_verification,
        )


class AsyncURLsResourceWithStreamingResponse:
    def __init__(self, urls: AsyncURLsResource) -> None:
        self._urls = urls

        self.list_verified = async_to_streamed_response_wrapper(
            urls.list_verified,
        )
        self.retrieve_details = async_to_streamed_response_wrapper(
            urls.retrieve_details,
        )
        self.submit_for_verification = async_to_streamed_response_wrapper(
            urls.submit_for_verification,
        )
