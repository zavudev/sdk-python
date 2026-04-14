# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncCursor, AsyncCursor
from .phone_numbers import (
    PhoneNumbersResource,
    AsyncPhoneNumbersResource,
    PhoneNumbersResourceWithRawResponse,
    AsyncPhoneNumbersResourceWithRawResponse,
    PhoneNumbersResourceWithStreamingResponse,
    AsyncPhoneNumbersResourceWithStreamingResponse,
)
from ...._base_client import AsyncPaginator, make_request_options
from ....types.number_10dlc import campaign_list_params, campaign_create_params, campaign_update_params
from ....types.number_10dlc.ten_dlc_campaign import TenDlcCampaign
from ....types.number_10dlc.campaign_create_response import CampaignCreateResponse
from ....types.number_10dlc.campaign_submit_response import CampaignSubmitResponse
from ....types.number_10dlc.campaign_update_response import CampaignUpdateResponse
from ....types.number_10dlc.campaign_retrieve_response import CampaignRetrieveResponse
from ....types.number_10dlc.campaign_sync_status_response import CampaignSyncStatusResponse

__all__ = ["CampaignsResource", "AsyncCampaignsResource"]


class CampaignsResource(SyncAPIResource):
    @cached_property
    def phone_numbers(self) -> PhoneNumbersResource:
        return PhoneNumbersResource(self._client)

    @cached_property
    def with_raw_response(self) -> CampaignsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return CampaignsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CampaignsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return CampaignsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        affiliate_marketing: bool,
        age_gated: bool,
        brand_id: str,
        description: str,
        direct_lending: bool,
        embedded_link: bool,
        embedded_phone: bool,
        name: str,
        number_pooling: bool,
        sample_messages: SequenceNotStr[str],
        subscriber_help: bool,
        subscriber_opt_in: bool,
        subscriber_opt_out: bool,
        use_case: str,
        help_message: str | Omit = omit,
        message_flow: str | Omit = omit,
        opt_in_keywords: SequenceNotStr[str] | Omit = omit,
        opt_out_keywords: SequenceNotStr[str] | Omit = omit,
        sub_use_cases: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CampaignCreateResponse:
        """Create a 10DLC campaign under an existing brand.

        The campaign starts in draft
        status. Submit it for carrier review using the submit endpoint.

        Args:
          brand_id: ID of the brand to create this campaign under.

          use_case: Campaign use case (e.g., ACCOUNT_NOTIFICATION, MARKETING, 2FA).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/10dlc/campaigns",
            body=maybe_transform(
                {
                    "affiliate_marketing": affiliate_marketing,
                    "age_gated": age_gated,
                    "brand_id": brand_id,
                    "description": description,
                    "direct_lending": direct_lending,
                    "embedded_link": embedded_link,
                    "embedded_phone": embedded_phone,
                    "name": name,
                    "number_pooling": number_pooling,
                    "sample_messages": sample_messages,
                    "subscriber_help": subscriber_help,
                    "subscriber_opt_in": subscriber_opt_in,
                    "subscriber_opt_out": subscriber_opt_out,
                    "use_case": use_case,
                    "help_message": help_message,
                    "message_flow": message_flow,
                    "opt_in_keywords": opt_in_keywords,
                    "opt_out_keywords": opt_out_keywords,
                    "sub_use_cases": sub_use_cases,
                },
                campaign_create_params.CampaignCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignCreateResponse,
        )

    def retrieve(
        self,
        campaign_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CampaignRetrieveResponse:
        """
        Get 10DLC campaign

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_id:
            raise ValueError(f"Expected a non-empty value for `campaign_id` but received {campaign_id!r}")
        return self._get(
            path_template("/v1/10dlc/campaigns/{campaign_id}", campaign_id=campaign_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignRetrieveResponse,
        )

    def update(
        self,
        campaign_id: str,
        *,
        description: str | Omit = omit,
        help_message: str | Omit = omit,
        message_flow: str | Omit = omit,
        name: str | Omit = omit,
        opt_in_keywords: SequenceNotStr[str] | Omit = omit,
        opt_out_keywords: SequenceNotStr[str] | Omit = omit,
        sample_messages: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CampaignUpdateResponse:
        """Update a 10DLC campaign in draft status.

        Cannot update after submission.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_id:
            raise ValueError(f"Expected a non-empty value for `campaign_id` but received {campaign_id!r}")
        return self._patch(
            path_template("/v1/10dlc/campaigns/{campaign_id}", campaign_id=campaign_id),
            body=maybe_transform(
                {
                    "description": description,
                    "help_message": help_message,
                    "message_flow": message_flow,
                    "name": name,
                    "opt_in_keywords": opt_in_keywords,
                    "opt_out_keywords": opt_out_keywords,
                    "sample_messages": sample_messages,
                },
                campaign_update_params.CampaignUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignUpdateResponse,
        )

    def list(
        self,
        *,
        brand_id: str | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursor[TenDlcCampaign]:
        """
        List 10DLC campaign registrations for this project.

        Args:
          brand_id: Filter campaigns by brand ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/10dlc/campaigns",
            page=SyncCursor[TenDlcCampaign],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "brand_id": brand_id,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    campaign_list_params.CampaignListParams,
                ),
            ),
            model=TenDlcCampaign,
        )

    def delete(
        self,
        campaign_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete 10DLC campaign

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_id:
            raise ValueError(f"Expected a non-empty value for `campaign_id` but received {campaign_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/10dlc/campaigns/{campaign_id}", campaign_id=campaign_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def submit(
        self,
        campaign_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CampaignSubmitResponse:
        """Submit a draft campaign for carrier review.

        The campaign must be in draft status
        and its brand must be verified.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_id:
            raise ValueError(f"Expected a non-empty value for `campaign_id` but received {campaign_id!r}")
        return self._post(
            path_template("/v1/10dlc/campaigns/{campaign_id}/submit", campaign_id=campaign_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignSubmitResponse,
        )

    def sync_status(
        self,
        campaign_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CampaignSyncStatusResponse:
        """Sync the campaign status with the registration provider.

        Use this to check for
        approval updates after submission.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_id:
            raise ValueError(f"Expected a non-empty value for `campaign_id` but received {campaign_id!r}")
        return self._post(
            path_template("/v1/10dlc/campaigns/{campaign_id}/sync", campaign_id=campaign_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignSyncStatusResponse,
        )


class AsyncCampaignsResource(AsyncAPIResource):
    @cached_property
    def phone_numbers(self) -> AsyncPhoneNumbersResource:
        return AsyncPhoneNumbersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCampaignsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCampaignsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCampaignsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return AsyncCampaignsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        affiliate_marketing: bool,
        age_gated: bool,
        brand_id: str,
        description: str,
        direct_lending: bool,
        embedded_link: bool,
        embedded_phone: bool,
        name: str,
        number_pooling: bool,
        sample_messages: SequenceNotStr[str],
        subscriber_help: bool,
        subscriber_opt_in: bool,
        subscriber_opt_out: bool,
        use_case: str,
        help_message: str | Omit = omit,
        message_flow: str | Omit = omit,
        opt_in_keywords: SequenceNotStr[str] | Omit = omit,
        opt_out_keywords: SequenceNotStr[str] | Omit = omit,
        sub_use_cases: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CampaignCreateResponse:
        """Create a 10DLC campaign under an existing brand.

        The campaign starts in draft
        status. Submit it for carrier review using the submit endpoint.

        Args:
          brand_id: ID of the brand to create this campaign under.

          use_case: Campaign use case (e.g., ACCOUNT_NOTIFICATION, MARKETING, 2FA).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/10dlc/campaigns",
            body=await async_maybe_transform(
                {
                    "affiliate_marketing": affiliate_marketing,
                    "age_gated": age_gated,
                    "brand_id": brand_id,
                    "description": description,
                    "direct_lending": direct_lending,
                    "embedded_link": embedded_link,
                    "embedded_phone": embedded_phone,
                    "name": name,
                    "number_pooling": number_pooling,
                    "sample_messages": sample_messages,
                    "subscriber_help": subscriber_help,
                    "subscriber_opt_in": subscriber_opt_in,
                    "subscriber_opt_out": subscriber_opt_out,
                    "use_case": use_case,
                    "help_message": help_message,
                    "message_flow": message_flow,
                    "opt_in_keywords": opt_in_keywords,
                    "opt_out_keywords": opt_out_keywords,
                    "sub_use_cases": sub_use_cases,
                },
                campaign_create_params.CampaignCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignCreateResponse,
        )

    async def retrieve(
        self,
        campaign_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CampaignRetrieveResponse:
        """
        Get 10DLC campaign

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_id:
            raise ValueError(f"Expected a non-empty value for `campaign_id` but received {campaign_id!r}")
        return await self._get(
            path_template("/v1/10dlc/campaigns/{campaign_id}", campaign_id=campaign_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignRetrieveResponse,
        )

    async def update(
        self,
        campaign_id: str,
        *,
        description: str | Omit = omit,
        help_message: str | Omit = omit,
        message_flow: str | Omit = omit,
        name: str | Omit = omit,
        opt_in_keywords: SequenceNotStr[str] | Omit = omit,
        opt_out_keywords: SequenceNotStr[str] | Omit = omit,
        sample_messages: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CampaignUpdateResponse:
        """Update a 10DLC campaign in draft status.

        Cannot update after submission.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_id:
            raise ValueError(f"Expected a non-empty value for `campaign_id` but received {campaign_id!r}")
        return await self._patch(
            path_template("/v1/10dlc/campaigns/{campaign_id}", campaign_id=campaign_id),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "help_message": help_message,
                    "message_flow": message_flow,
                    "name": name,
                    "opt_in_keywords": opt_in_keywords,
                    "opt_out_keywords": opt_out_keywords,
                    "sample_messages": sample_messages,
                },
                campaign_update_params.CampaignUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignUpdateResponse,
        )

    def list(
        self,
        *,
        brand_id: str | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[TenDlcCampaign, AsyncCursor[TenDlcCampaign]]:
        """
        List 10DLC campaign registrations for this project.

        Args:
          brand_id: Filter campaigns by brand ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/10dlc/campaigns",
            page=AsyncCursor[TenDlcCampaign],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "brand_id": brand_id,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    campaign_list_params.CampaignListParams,
                ),
            ),
            model=TenDlcCampaign,
        )

    async def delete(
        self,
        campaign_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete 10DLC campaign

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_id:
            raise ValueError(f"Expected a non-empty value for `campaign_id` but received {campaign_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/10dlc/campaigns/{campaign_id}", campaign_id=campaign_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def submit(
        self,
        campaign_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CampaignSubmitResponse:
        """Submit a draft campaign for carrier review.

        The campaign must be in draft status
        and its brand must be verified.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_id:
            raise ValueError(f"Expected a non-empty value for `campaign_id` but received {campaign_id!r}")
        return await self._post(
            path_template("/v1/10dlc/campaigns/{campaign_id}/submit", campaign_id=campaign_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignSubmitResponse,
        )

    async def sync_status(
        self,
        campaign_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CampaignSyncStatusResponse:
        """Sync the campaign status with the registration provider.

        Use this to check for
        approval updates after submission.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_id:
            raise ValueError(f"Expected a non-empty value for `campaign_id` but received {campaign_id!r}")
        return await self._post(
            path_template("/v1/10dlc/campaigns/{campaign_id}/sync", campaign_id=campaign_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignSyncStatusResponse,
        )


class CampaignsResourceWithRawResponse:
    def __init__(self, campaigns: CampaignsResource) -> None:
        self._campaigns = campaigns

        self.create = to_raw_response_wrapper(
            campaigns.create,
        )
        self.retrieve = to_raw_response_wrapper(
            campaigns.retrieve,
        )
        self.update = to_raw_response_wrapper(
            campaigns.update,
        )
        self.list = to_raw_response_wrapper(
            campaigns.list,
        )
        self.delete = to_raw_response_wrapper(
            campaigns.delete,
        )
        self.submit = to_raw_response_wrapper(
            campaigns.submit,
        )
        self.sync_status = to_raw_response_wrapper(
            campaigns.sync_status,
        )

    @cached_property
    def phone_numbers(self) -> PhoneNumbersResourceWithRawResponse:
        return PhoneNumbersResourceWithRawResponse(self._campaigns.phone_numbers)


class AsyncCampaignsResourceWithRawResponse:
    def __init__(self, campaigns: AsyncCampaignsResource) -> None:
        self._campaigns = campaigns

        self.create = async_to_raw_response_wrapper(
            campaigns.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            campaigns.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            campaigns.update,
        )
        self.list = async_to_raw_response_wrapper(
            campaigns.list,
        )
        self.delete = async_to_raw_response_wrapper(
            campaigns.delete,
        )
        self.submit = async_to_raw_response_wrapper(
            campaigns.submit,
        )
        self.sync_status = async_to_raw_response_wrapper(
            campaigns.sync_status,
        )

    @cached_property
    def phone_numbers(self) -> AsyncPhoneNumbersResourceWithRawResponse:
        return AsyncPhoneNumbersResourceWithRawResponse(self._campaigns.phone_numbers)


class CampaignsResourceWithStreamingResponse:
    def __init__(self, campaigns: CampaignsResource) -> None:
        self._campaigns = campaigns

        self.create = to_streamed_response_wrapper(
            campaigns.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            campaigns.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            campaigns.update,
        )
        self.list = to_streamed_response_wrapper(
            campaigns.list,
        )
        self.delete = to_streamed_response_wrapper(
            campaigns.delete,
        )
        self.submit = to_streamed_response_wrapper(
            campaigns.submit,
        )
        self.sync_status = to_streamed_response_wrapper(
            campaigns.sync_status,
        )

    @cached_property
    def phone_numbers(self) -> PhoneNumbersResourceWithStreamingResponse:
        return PhoneNumbersResourceWithStreamingResponse(self._campaigns.phone_numbers)


class AsyncCampaignsResourceWithStreamingResponse:
    def __init__(self, campaigns: AsyncCampaignsResource) -> None:
        self._campaigns = campaigns

        self.create = async_to_streamed_response_wrapper(
            campaigns.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            campaigns.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            campaigns.update,
        )
        self.list = async_to_streamed_response_wrapper(
            campaigns.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            campaigns.delete,
        )
        self.submit = async_to_streamed_response_wrapper(
            campaigns.submit,
        )
        self.sync_status = async_to_streamed_response_wrapper(
            campaigns.sync_status,
        )

    @cached_property
    def phone_numbers(self) -> AsyncPhoneNumbersResourceWithStreamingResponse:
        return AsyncPhoneNumbersResourceWithStreamingResponse(self._campaigns.phone_numbers)
