# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.number_10dlc.campaigns import phone_number_assign_params
from ....types.number_10dlc.campaigns.phone_number_list_response import PhoneNumberListResponse
from ....types.number_10dlc.campaigns.phone_number_assign_response import PhoneNumberAssignResponse

__all__ = ["PhoneNumbersResource", "AsyncPhoneNumbersResource"]


class PhoneNumbersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PhoneNumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return PhoneNumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PhoneNumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return PhoneNumbersResourceWithStreamingResponse(self)

    def list(
        self,
        campaign_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberListResponse:
        """
        List phone numbers assigned to a 10DLC campaign.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_id:
            raise ValueError(f"Expected a non-empty value for `campaign_id` but received {campaign_id!r}")
        return self._get(
            path_template("/v1/10dlc/campaigns/{campaign_id}/phone-numbers", campaign_id=campaign_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberListResponse,
        )

    def assign(
        self,
        campaign_id: str,
        *,
        phone_number_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberAssignResponse:
        """Assign a US phone number to an approved 10DLC campaign.

        The campaign must be in
        approved status.

        Args:
          phone_number_id: ID of the phone number to assign.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_id:
            raise ValueError(f"Expected a non-empty value for `campaign_id` but received {campaign_id!r}")
        return self._post(
            path_template("/v1/10dlc/campaigns/{campaign_id}/phone-numbers", campaign_id=campaign_id),
            body=maybe_transform(
                {"phone_number_id": phone_number_id}, phone_number_assign_params.PhoneNumberAssignParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberAssignResponse,
        )

    def unassign(
        self,
        assignment_id: str,
        *,
        campaign_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a phone number assignment from a 10DLC campaign.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_id:
            raise ValueError(f"Expected a non-empty value for `campaign_id` but received {campaign_id!r}")
        if not assignment_id:
            raise ValueError(f"Expected a non-empty value for `assignment_id` but received {assignment_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/v1/10dlc/campaigns/{campaign_id}/phone-numbers/{assignment_id}",
                campaign_id=campaign_id,
                assignment_id=assignment_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncPhoneNumbersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPhoneNumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPhoneNumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPhoneNumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return AsyncPhoneNumbersResourceWithStreamingResponse(self)

    async def list(
        self,
        campaign_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberListResponse:
        """
        List phone numbers assigned to a 10DLC campaign.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_id:
            raise ValueError(f"Expected a non-empty value for `campaign_id` but received {campaign_id!r}")
        return await self._get(
            path_template("/v1/10dlc/campaigns/{campaign_id}/phone-numbers", campaign_id=campaign_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberListResponse,
        )

    async def assign(
        self,
        campaign_id: str,
        *,
        phone_number_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberAssignResponse:
        """Assign a US phone number to an approved 10DLC campaign.

        The campaign must be in
        approved status.

        Args:
          phone_number_id: ID of the phone number to assign.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_id:
            raise ValueError(f"Expected a non-empty value for `campaign_id` but received {campaign_id!r}")
        return await self._post(
            path_template("/v1/10dlc/campaigns/{campaign_id}/phone-numbers", campaign_id=campaign_id),
            body=await async_maybe_transform(
                {"phone_number_id": phone_number_id}, phone_number_assign_params.PhoneNumberAssignParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberAssignResponse,
        )

    async def unassign(
        self,
        assignment_id: str,
        *,
        campaign_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a phone number assignment from a 10DLC campaign.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_id:
            raise ValueError(f"Expected a non-empty value for `campaign_id` but received {campaign_id!r}")
        if not assignment_id:
            raise ValueError(f"Expected a non-empty value for `assignment_id` but received {assignment_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/v1/10dlc/campaigns/{campaign_id}/phone-numbers/{assignment_id}",
                campaign_id=campaign_id,
                assignment_id=assignment_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class PhoneNumbersResourceWithRawResponse:
    def __init__(self, phone_numbers: PhoneNumbersResource) -> None:
        self._phone_numbers = phone_numbers

        self.list = to_raw_response_wrapper(
            phone_numbers.list,
        )
        self.assign = to_raw_response_wrapper(
            phone_numbers.assign,
        )
        self.unassign = to_raw_response_wrapper(
            phone_numbers.unassign,
        )


class AsyncPhoneNumbersResourceWithRawResponse:
    def __init__(self, phone_numbers: AsyncPhoneNumbersResource) -> None:
        self._phone_numbers = phone_numbers

        self.list = async_to_raw_response_wrapper(
            phone_numbers.list,
        )
        self.assign = async_to_raw_response_wrapper(
            phone_numbers.assign,
        )
        self.unassign = async_to_raw_response_wrapper(
            phone_numbers.unassign,
        )


class PhoneNumbersResourceWithStreamingResponse:
    def __init__(self, phone_numbers: PhoneNumbersResource) -> None:
        self._phone_numbers = phone_numbers

        self.list = to_streamed_response_wrapper(
            phone_numbers.list,
        )
        self.assign = to_streamed_response_wrapper(
            phone_numbers.assign,
        )
        self.unassign = to_streamed_response_wrapper(
            phone_numbers.unassign,
        )


class AsyncPhoneNumbersResourceWithStreamingResponse:
    def __init__(self, phone_numbers: AsyncPhoneNumbersResource) -> None:
        self._phone_numbers = phone_numbers

        self.list = async_to_streamed_response_wrapper(
            phone_numbers.list,
        )
        self.assign = async_to_streamed_response_wrapper(
            phone_numbers.assign,
        )
        self.unassign = async_to_streamed_response_wrapper(
            phone_numbers.unassign,
        )
