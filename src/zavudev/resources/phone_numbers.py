# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..types import (
    PhoneNumberType,
    PhoneNumberStatus,
    phone_number_list_params,
    phone_number_update_params,
    phone_number_purchase_params,
    phone_number_requirements_params,
    phone_number_search_available_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ..types.phone_number_type import PhoneNumberType
from ..types.owned_phone_number import OwnedPhoneNumber
from ..types.phone_number_status import PhoneNumberStatus
from ..types.phone_number_update_response import PhoneNumberUpdateResponse
from ..types.phone_number_purchase_response import PhoneNumberPurchaseResponse
from ..types.phone_number_retrieve_response import PhoneNumberRetrieveResponse
from ..types.phone_number_requirements_response import PhoneNumberRequirementsResponse
from ..types.phone_number_search_available_response import PhoneNumberSearchAvailableResponse

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

    def retrieve(
        self,
        phone_number_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberRetrieveResponse:
        """
        Get details of a specific phone number.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number_id:
            raise ValueError(f"Expected a non-empty value for `phone_number_id` but received {phone_number_id!r}")
        return self._get(
            path_template("/v1/phone-numbers/{phone_number_id}", phone_number_id=phone_number_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberRetrieveResponse,
        )

    def update(
        self,
        phone_number_id: str,
        *,
        name: Optional[str] | Omit = omit,
        sender_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberUpdateResponse:
        """
        Update a phone number's name or sender assignment.

        Args:
          name: Custom name for the phone number. Set to null to clear.

          sender_id: Sender ID to assign the phone number to. Set to null to unassign. A number under
              regulatory review is recorded now and connected to the sender when approved; a
              rejected number is refused.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number_id:
            raise ValueError(f"Expected a non-empty value for `phone_number_id` but received {phone_number_id!r}")
        return self._patch(
            path_template("/v1/phone-numbers/{phone_number_id}", phone_number_id=phone_number_id),
            body=maybe_transform(
                {
                    "name": name,
                    "sender_id": sender_id,
                },
                phone_number_update_params.PhoneNumberUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberUpdateResponse,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        status: PhoneNumberStatus | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursor[OwnedPhoneNumber]:
        """
        List all phone numbers owned by this project.

        Args:
          cursor: Pagination cursor.

          status: Filter by phone number status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/phone-numbers",
            page=SyncCursor[OwnedPhoneNumber],
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
                    phone_number_list_params.PhoneNumberListParams,
                ),
            ),
            model=OwnedPhoneNumber,
        )

    def purchase(
        self,
        *,
        phone_number: str,
        name: str | Omit = omit,
        regulatory_requirements: Iterable[phone_number_purchase_params.RegulatoryRequirement] | Omit = omit,
        type: PhoneNumberType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberPurchaseResponse:
        """Purchase an available phone number.

        Requires a paid plan: the Free plan cannot
        purchase phone numbers and receives `402` with code `paid_plan_required`.

        **The included number.** A paid plan includes one number at no charge, once per
        account: it must be a US or Canadian number (a +1 number) costing $20 a month or
        less. `isFreeEligible` in `GET /v1/phone-numbers/available` marks the numbers
        that qualify. Claiming it spends the benefit for good, across every team the
        account owner owns, so releasing that number does not make another one free.

        **Numbers with regulatory requirements.** Which numbers need regulatory
        information is decided per number, not by a fixed country list. The purchase
        looks the requirements up for the exact number before charging anything:

        1. `GET /v1/phone-numbers/requirements?phoneNumber=...`. If `items` is empty,
           buy normally.
        2. Create what it asks for: addresses with `POST /v1/addresses`, documents with
           `POST /v1/documents`.
        3. Purchase with `type` and `regulatoryRequirements`. The number is bought and
           billed at once with `regulatoryStatus: pending_review`.
        4. Poll `GET /v1/phone-numbers/{phoneNumberId}` until `regulatoryStatus` is
           `approved`. Assign it to a sender before or after approval; it starts
           carrying messages once approved.

        **Reuse.** Information you submitted is kept for your project, per country and
        `type`, and a later purchase there may omit `regulatoryRequirements`. Reuse only
        happens when what is kept still covers every requirement of the new number and
        every address and document in it belongs to the project. Otherwise, or when
        nothing is kept, the purchase returns `400 regulatory_compliance_required` with
        the missing requirements in `details`.

        Invalid values (a missing, unknown or repeated requirement id, an address or
        document from another project, or one rejected in review) return
        `400 invalid_request`. If an address or document cannot be registered for
        review, the purchase returns `400 invalid_request` naming the requirement. If
        the requirements cannot be looked up, the purchase returns
        `502 requirements_unavailable`, except for US and Canadian numbers, which are
        sold as numbers without requirements. None of these errors charge anything.

        Args:
          phone_number: Phone number in E.164 format.

          name: Optional custom name for the phone number.

          regulatory_requirements: Regulatory information, for numbers whose requirements list is not empty. Get
              the list with `GET /v1/phone-numbers/requirements?phoneNumber=...` and send one
              entry per requirement id, except `action` requirements, which take no value.
              Every required id must be present, once, and no unknown id may be sent;
              otherwise the purchase is refused with `400 invalid_request` before anything is
              charged.

              The information is kept for your project under the number's country and `type`.
              A later purchase there may omit this field if what is kept still covers that
              number's requirements. Omit it for numbers without requirements.

          type: Type of phone number. `mobile` is stocked in countries where no geographic
              (`local`) or non-geographic (`national`) inventory exists, and in several
              markets it is the only type that can receive SMS.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/phone-numbers",
            body=maybe_transform(
                {
                    "phone_number": phone_number,
                    "name": name,
                    "regulatory_requirements": regulatory_requirements,
                    "type": type,
                },
                phone_number_purchase_params.PhoneNumberPurchaseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberPurchaseResponse,
        )

    def release(
        self,
        phone_number_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Release a phone number.

        The phone number must not be assigned to a sender.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number_id:
            raise ValueError(f"Expected a non-empty value for `phone_number_id` but received {phone_number_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/phone-numbers/{phone_number_id}", phone_number_id=phone_number_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def requirements(
        self,
        *,
        country_code: str | Omit = omit,
        phone_number: str | Omit = omit,
        type: PhoneNumberType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberRequirementsResponse:
        """
        Get the regulatory information needed to buy a phone number, for one specific
        number or for a country and number type. Prefer `phoneNumber`: the response is
        then exactly the list the purchase of that number validates against. Pass each
        `requirementTypes[].id` back as `requirementType` in `regulatoryRequirements` on
        `POST /v1/phone-numbers`.

        For `phoneNumber`, the requirements of that exact number are returned. When they
        cannot be resolved for the number itself, the list for its country and `type` is
        returned instead, and the purchase uses the same list. An empty `items` array
        means the number needs no regulatory information. If the requirements cannot be
        retrieved at all, the response is `502 requirements_unavailable`, never an empty
        list.

        URL-encode the `+` of `phoneNumber` as `%2B`. An unencoded `+` is also accepted.

        Args:
          country_code: Two-letter ISO country code. Required unless `phoneNumber` is given.

          phone_number: E.164 number from `GET /v1/phone-numbers/available`, with `+` encoded as `%2B`.
              Returns the requirements the purchase of that number checks. Takes precedence
              over `countryCode`.

          type: Type of phone number (local, national, mobile, tollFree). Defaults to `local`.
              With `phoneNumber`, used only when the number's own requirements cannot be
              resolved and the country list is returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/phone-numbers/requirements",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "country_code": country_code,
                        "phone_number": phone_number,
                        "type": type,
                    },
                    phone_number_requirements_params.PhoneNumberRequirementsParams,
                ),
            ),
            cast_to=PhoneNumberRequirementsResponse,
        )

    def search_available(
        self,
        *,
        country_code: str,
        capabilities: str | Omit = omit,
        contains: str | Omit = omit,
        limit: int | Omit = omit,
        type: PhoneNumberType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberSearchAvailableResponse:
        """
        Search for available phone numbers to purchase by country and type.

        Args:
          country_code: Two-letter ISO country code.

          capabilities: Comma-separated capabilities the number must have: `sms`, `voice`, `mms`.
              Numbers missing any of them are dropped.

          contains: Search for numbers containing this string.

          limit: Maximum number of results to return.

          type: Type of phone number to search for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/phone-numbers/available",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "country_code": country_code,
                        "capabilities": capabilities,
                        "contains": contains,
                        "limit": limit,
                        "type": type,
                    },
                    phone_number_search_available_params.PhoneNumberSearchAvailableParams,
                ),
            ),
            cast_to=PhoneNumberSearchAvailableResponse,
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

    async def retrieve(
        self,
        phone_number_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberRetrieveResponse:
        """
        Get details of a specific phone number.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number_id:
            raise ValueError(f"Expected a non-empty value for `phone_number_id` but received {phone_number_id!r}")
        return await self._get(
            path_template("/v1/phone-numbers/{phone_number_id}", phone_number_id=phone_number_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberRetrieveResponse,
        )

    async def update(
        self,
        phone_number_id: str,
        *,
        name: Optional[str] | Omit = omit,
        sender_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberUpdateResponse:
        """
        Update a phone number's name or sender assignment.

        Args:
          name: Custom name for the phone number. Set to null to clear.

          sender_id: Sender ID to assign the phone number to. Set to null to unassign. A number under
              regulatory review is recorded now and connected to the sender when approved; a
              rejected number is refused.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number_id:
            raise ValueError(f"Expected a non-empty value for `phone_number_id` but received {phone_number_id!r}")
        return await self._patch(
            path_template("/v1/phone-numbers/{phone_number_id}", phone_number_id=phone_number_id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "sender_id": sender_id,
                },
                phone_number_update_params.PhoneNumberUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberUpdateResponse,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        status: PhoneNumberStatus | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[OwnedPhoneNumber, AsyncCursor[OwnedPhoneNumber]]:
        """
        List all phone numbers owned by this project.

        Args:
          cursor: Pagination cursor.

          status: Filter by phone number status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/phone-numbers",
            page=AsyncCursor[OwnedPhoneNumber],
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
                    phone_number_list_params.PhoneNumberListParams,
                ),
            ),
            model=OwnedPhoneNumber,
        )

    async def purchase(
        self,
        *,
        phone_number: str,
        name: str | Omit = omit,
        regulatory_requirements: Iterable[phone_number_purchase_params.RegulatoryRequirement] | Omit = omit,
        type: PhoneNumberType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberPurchaseResponse:
        """Purchase an available phone number.

        Requires a paid plan: the Free plan cannot
        purchase phone numbers and receives `402` with code `paid_plan_required`.

        **The included number.** A paid plan includes one number at no charge, once per
        account: it must be a US or Canadian number (a +1 number) costing $20 a month or
        less. `isFreeEligible` in `GET /v1/phone-numbers/available` marks the numbers
        that qualify. Claiming it spends the benefit for good, across every team the
        account owner owns, so releasing that number does not make another one free.

        **Numbers with regulatory requirements.** Which numbers need regulatory
        information is decided per number, not by a fixed country list. The purchase
        looks the requirements up for the exact number before charging anything:

        1. `GET /v1/phone-numbers/requirements?phoneNumber=...`. If `items` is empty,
           buy normally.
        2. Create what it asks for: addresses with `POST /v1/addresses`, documents with
           `POST /v1/documents`.
        3. Purchase with `type` and `regulatoryRequirements`. The number is bought and
           billed at once with `regulatoryStatus: pending_review`.
        4. Poll `GET /v1/phone-numbers/{phoneNumberId}` until `regulatoryStatus` is
           `approved`. Assign it to a sender before or after approval; it starts
           carrying messages once approved.

        **Reuse.** Information you submitted is kept for your project, per country and
        `type`, and a later purchase there may omit `regulatoryRequirements`. Reuse only
        happens when what is kept still covers every requirement of the new number and
        every address and document in it belongs to the project. Otherwise, or when
        nothing is kept, the purchase returns `400 regulatory_compliance_required` with
        the missing requirements in `details`.

        Invalid values (a missing, unknown or repeated requirement id, an address or
        document from another project, or one rejected in review) return
        `400 invalid_request`. If an address or document cannot be registered for
        review, the purchase returns `400 invalid_request` naming the requirement. If
        the requirements cannot be looked up, the purchase returns
        `502 requirements_unavailable`, except for US and Canadian numbers, which are
        sold as numbers without requirements. None of these errors charge anything.

        Args:
          phone_number: Phone number in E.164 format.

          name: Optional custom name for the phone number.

          regulatory_requirements: Regulatory information, for numbers whose requirements list is not empty. Get
              the list with `GET /v1/phone-numbers/requirements?phoneNumber=...` and send one
              entry per requirement id, except `action` requirements, which take no value.
              Every required id must be present, once, and no unknown id may be sent;
              otherwise the purchase is refused with `400 invalid_request` before anything is
              charged.

              The information is kept for your project under the number's country and `type`.
              A later purchase there may omit this field if what is kept still covers that
              number's requirements. Omit it for numbers without requirements.

          type: Type of phone number. `mobile` is stocked in countries where no geographic
              (`local`) or non-geographic (`national`) inventory exists, and in several
              markets it is the only type that can receive SMS.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/phone-numbers",
            body=await async_maybe_transform(
                {
                    "phone_number": phone_number,
                    "name": name,
                    "regulatory_requirements": regulatory_requirements,
                    "type": type,
                },
                phone_number_purchase_params.PhoneNumberPurchaseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberPurchaseResponse,
        )

    async def release(
        self,
        phone_number_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Release a phone number.

        The phone number must not be assigned to a sender.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number_id:
            raise ValueError(f"Expected a non-empty value for `phone_number_id` but received {phone_number_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/phone-numbers/{phone_number_id}", phone_number_id=phone_number_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def requirements(
        self,
        *,
        country_code: str | Omit = omit,
        phone_number: str | Omit = omit,
        type: PhoneNumberType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberRequirementsResponse:
        """
        Get the regulatory information needed to buy a phone number, for one specific
        number or for a country and number type. Prefer `phoneNumber`: the response is
        then exactly the list the purchase of that number validates against. Pass each
        `requirementTypes[].id` back as `requirementType` in `regulatoryRequirements` on
        `POST /v1/phone-numbers`.

        For `phoneNumber`, the requirements of that exact number are returned. When they
        cannot be resolved for the number itself, the list for its country and `type` is
        returned instead, and the purchase uses the same list. An empty `items` array
        means the number needs no regulatory information. If the requirements cannot be
        retrieved at all, the response is `502 requirements_unavailable`, never an empty
        list.

        URL-encode the `+` of `phoneNumber` as `%2B`. An unencoded `+` is also accepted.

        Args:
          country_code: Two-letter ISO country code. Required unless `phoneNumber` is given.

          phone_number: E.164 number from `GET /v1/phone-numbers/available`, with `+` encoded as `%2B`.
              Returns the requirements the purchase of that number checks. Takes precedence
              over `countryCode`.

          type: Type of phone number (local, national, mobile, tollFree). Defaults to `local`.
              With `phoneNumber`, used only when the number's own requirements cannot be
              resolved and the country list is returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/phone-numbers/requirements",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "country_code": country_code,
                        "phone_number": phone_number,
                        "type": type,
                    },
                    phone_number_requirements_params.PhoneNumberRequirementsParams,
                ),
            ),
            cast_to=PhoneNumberRequirementsResponse,
        )

    async def search_available(
        self,
        *,
        country_code: str,
        capabilities: str | Omit = omit,
        contains: str | Omit = omit,
        limit: int | Omit = omit,
        type: PhoneNumberType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberSearchAvailableResponse:
        """
        Search for available phone numbers to purchase by country and type.

        Args:
          country_code: Two-letter ISO country code.

          capabilities: Comma-separated capabilities the number must have: `sms`, `voice`, `mms`.
              Numbers missing any of them are dropped.

          contains: Search for numbers containing this string.

          limit: Maximum number of results to return.

          type: Type of phone number to search for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/phone-numbers/available",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "country_code": country_code,
                        "capabilities": capabilities,
                        "contains": contains,
                        "limit": limit,
                        "type": type,
                    },
                    phone_number_search_available_params.PhoneNumberSearchAvailableParams,
                ),
            ),
            cast_to=PhoneNumberSearchAvailableResponse,
        )


class PhoneNumbersResourceWithRawResponse:
    def __init__(self, phone_numbers: PhoneNumbersResource) -> None:
        self._phone_numbers = phone_numbers

        self.retrieve = to_raw_response_wrapper(
            phone_numbers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            phone_numbers.update,
        )
        self.list = to_raw_response_wrapper(
            phone_numbers.list,
        )
        self.purchase = to_raw_response_wrapper(
            phone_numbers.purchase,
        )
        self.release = to_raw_response_wrapper(
            phone_numbers.release,
        )
        self.requirements = to_raw_response_wrapper(
            phone_numbers.requirements,
        )
        self.search_available = to_raw_response_wrapper(
            phone_numbers.search_available,
        )


class AsyncPhoneNumbersResourceWithRawResponse:
    def __init__(self, phone_numbers: AsyncPhoneNumbersResource) -> None:
        self._phone_numbers = phone_numbers

        self.retrieve = async_to_raw_response_wrapper(
            phone_numbers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            phone_numbers.update,
        )
        self.list = async_to_raw_response_wrapper(
            phone_numbers.list,
        )
        self.purchase = async_to_raw_response_wrapper(
            phone_numbers.purchase,
        )
        self.release = async_to_raw_response_wrapper(
            phone_numbers.release,
        )
        self.requirements = async_to_raw_response_wrapper(
            phone_numbers.requirements,
        )
        self.search_available = async_to_raw_response_wrapper(
            phone_numbers.search_available,
        )


class PhoneNumbersResourceWithStreamingResponse:
    def __init__(self, phone_numbers: PhoneNumbersResource) -> None:
        self._phone_numbers = phone_numbers

        self.retrieve = to_streamed_response_wrapper(
            phone_numbers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            phone_numbers.update,
        )
        self.list = to_streamed_response_wrapper(
            phone_numbers.list,
        )
        self.purchase = to_streamed_response_wrapper(
            phone_numbers.purchase,
        )
        self.release = to_streamed_response_wrapper(
            phone_numbers.release,
        )
        self.requirements = to_streamed_response_wrapper(
            phone_numbers.requirements,
        )
        self.search_available = to_streamed_response_wrapper(
            phone_numbers.search_available,
        )


class AsyncPhoneNumbersResourceWithStreamingResponse:
    def __init__(self, phone_numbers: AsyncPhoneNumbersResource) -> None:
        self._phone_numbers = phone_numbers

        self.retrieve = async_to_streamed_response_wrapper(
            phone_numbers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            phone_numbers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            phone_numbers.list,
        )
        self.purchase = async_to_streamed_response_wrapper(
            phone_numbers.purchase,
        )
        self.release = async_to_streamed_response_wrapper(
            phone_numbers.release,
        )
        self.requirements = async_to_streamed_response_wrapper(
            phone_numbers.requirements,
        )
        self.search_available = async_to_streamed_response_wrapper(
            phone_numbers.search_available,
        )
