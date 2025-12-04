# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import introspect_validate_phone_params
from .._types import Body, Query, Headers, NotGiven, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.introspect_validate_phone_response import IntrospectValidatePhoneResponse

__all__ = ["IntrospectResource", "AsyncIntrospectResource"]


class IntrospectResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IntrospectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return IntrospectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IntrospectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return IntrospectResourceWithStreamingResponse(self)

    def validate_phone(
        self,
        *,
        phone_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntrospectValidatePhoneResponse:
        """
        Validate a phone number and check if a WhatsApp conversation window is open.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/introspect/phone",
            body=maybe_transform(
                {"phone_number": phone_number}, introspect_validate_phone_params.IntrospectValidatePhoneParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntrospectValidatePhoneResponse,
        )


class AsyncIntrospectResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIntrospectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIntrospectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIntrospectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return AsyncIntrospectResourceWithStreamingResponse(self)

    async def validate_phone(
        self,
        *,
        phone_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntrospectValidatePhoneResponse:
        """
        Validate a phone number and check if a WhatsApp conversation window is open.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/introspect/phone",
            body=await async_maybe_transform(
                {"phone_number": phone_number}, introspect_validate_phone_params.IntrospectValidatePhoneParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntrospectValidatePhoneResponse,
        )


class IntrospectResourceWithRawResponse:
    def __init__(self, introspect: IntrospectResource) -> None:
        self._introspect = introspect

        self.validate_phone = to_raw_response_wrapper(
            introspect.validate_phone,
        )


class AsyncIntrospectResourceWithRawResponse:
    def __init__(self, introspect: AsyncIntrospectResource) -> None:
        self._introspect = introspect

        self.validate_phone = async_to_raw_response_wrapper(
            introspect.validate_phone,
        )


class IntrospectResourceWithStreamingResponse:
    def __init__(self, introspect: IntrospectResource) -> None:
        self._introspect = introspect

        self.validate_phone = to_streamed_response_wrapper(
            introspect.validate_phone,
        )


class AsyncIntrospectResourceWithStreamingResponse:
    def __init__(self, introspect: AsyncIntrospectResource) -> None:
        self._introspect = introspect

        self.validate_phone = async_to_streamed_response_wrapper(
            introspect.validate_phone,
        )
