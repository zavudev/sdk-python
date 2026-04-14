# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncCursor, AsyncCursor
from ..._base_client import AsyncPaginator, make_request_options
from ...types.number_10dlc import brand_list_params, brand_create_params, brand_update_params
from ...types.number_10dlc.ten_dlc_brand import TenDlcBrand
from ...types.number_10dlc.brand_create_response import BrandCreateResponse
from ...types.number_10dlc.brand_submit_response import BrandSubmitResponse
from ...types.number_10dlc.brand_update_response import BrandUpdateResponse
from ...types.number_10dlc.brand_retrieve_response import BrandRetrieveResponse
from ...types.number_10dlc.brand_sync_status_response import BrandSyncStatusResponse
from ...types.number_10dlc.brand_list_use_cases_response import BrandListUseCasesResponse

__all__ = ["BrandsResource", "AsyncBrandsResource"]


class BrandsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BrandsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return BrandsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrandsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return BrandsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        city: str,
        country: str,
        display_name: str,
        email: str,
        entity_type: Literal["PRIVATE_PROFIT", "PUBLIC_PROFIT", "NON_PROFIT", "GOVERNMENT", "SOLE_PROPRIETOR"],
        phone: str,
        postal_code: str,
        state: str,
        street: str,
        vertical: str,
        company_name: str | Omit = omit,
        ein: str | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        stock_exchange: str | Omit = omit,
        stock_symbol: str | Omit = omit,
        website: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandCreateResponse:
        """Create a 10DLC brand registration.

        The brand starts in draft status. Submit it
        for review using the submit endpoint.

        Args:
          country: Two-letter ISO country code.

          display_name: Display name of the brand.

          entity_type: Business entity type for 10DLC brand registration.

          phone: Contact phone in E.164 format.

          vertical: Industry vertical.

          company_name: Legal company name.

          ein: Employer Identification Number (format: XX-XXXXXXX).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/10dlc/brands",
            body=maybe_transform(
                {
                    "city": city,
                    "country": country,
                    "display_name": display_name,
                    "email": email,
                    "entity_type": entity_type,
                    "phone": phone,
                    "postal_code": postal_code,
                    "state": state,
                    "street": street,
                    "vertical": vertical,
                    "company_name": company_name,
                    "ein": ein,
                    "first_name": first_name,
                    "last_name": last_name,
                    "stock_exchange": stock_exchange,
                    "stock_symbol": stock_symbol,
                    "website": website,
                },
                brand_create_params.BrandCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandCreateResponse,
        )

    def retrieve(
        self,
        brand_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveResponse:
        """
        Get 10DLC brand

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        return self._get(
            path_template("/v1/10dlc/brands/{brand_id}", brand_id=brand_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandRetrieveResponse,
        )

    def update(
        self,
        brand_id: str,
        *,
        city: str | Omit = omit,
        company_name: str | Omit = omit,
        country: str | Omit = omit,
        display_name: str | Omit = omit,
        ein: str | Omit = omit,
        email: str | Omit = omit,
        entity_type: Literal["PRIVATE_PROFIT", "PUBLIC_PROFIT", "NON_PROFIT", "GOVERNMENT", "SOLE_PROPRIETOR"]
        | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        phone: str | Omit = omit,
        postal_code: str | Omit = omit,
        state: str | Omit = omit,
        stock_exchange: str | Omit = omit,
        stock_symbol: str | Omit = omit,
        street: str | Omit = omit,
        vertical: str | Omit = omit,
        website: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandUpdateResponse:
        """Update a 10DLC brand in draft status.

        Cannot update after submission.

        Args:
          entity_type: Business entity type for 10DLC brand registration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        return self._patch(
            path_template("/v1/10dlc/brands/{brand_id}", brand_id=brand_id),
            body=maybe_transform(
                {
                    "city": city,
                    "company_name": company_name,
                    "country": country,
                    "display_name": display_name,
                    "ein": ein,
                    "email": email,
                    "entity_type": entity_type,
                    "first_name": first_name,
                    "last_name": last_name,
                    "phone": phone,
                    "postal_code": postal_code,
                    "state": state,
                    "stock_exchange": stock_exchange,
                    "stock_symbol": stock_symbol,
                    "street": street,
                    "vertical": vertical,
                    "website": website,
                },
                brand_update_params.BrandUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandUpdateResponse,
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
    ) -> SyncCursor[TenDlcBrand]:
        """
        List 10DLC brand registrations for this project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/10dlc/brands",
            page=SyncCursor[TenDlcBrand],
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
                    brand_list_params.BrandListParams,
                ),
            ),
            model=TenDlcBrand,
        )

    def delete(
        self,
        brand_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete 10DLC brand

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/10dlc/brands/{brand_id}", brand_id=brand_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_use_cases(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandListUseCasesResponse:
        """List available use cases for 10DLC campaign registration."""
        return self._get(
            "/v1/10dlc/brands/use-cases",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandListUseCasesResponse,
        )

    def submit(
        self,
        brand_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandSubmitResponse:
        """Submit a draft brand to The Campaign Registry (TCR) for vetting.

        The brand must
        be in draft status. A $35 registration fee is charged from your balance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        return self._post(
            path_template("/v1/10dlc/brands/{brand_id}/submit", brand_id=brand_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandSubmitResponse,
        )

    def sync_status(
        self,
        brand_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandSyncStatusResponse:
        """Sync the brand status with the registration provider.

        Use this to check for
        approval updates after submission.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        return self._post(
            path_template("/v1/10dlc/brands/{brand_id}/sync", brand_id=brand_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandSyncStatusResponse,
        )


class AsyncBrandsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBrandsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBrandsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBrandsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return AsyncBrandsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        city: str,
        country: str,
        display_name: str,
        email: str,
        entity_type: Literal["PRIVATE_PROFIT", "PUBLIC_PROFIT", "NON_PROFIT", "GOVERNMENT", "SOLE_PROPRIETOR"],
        phone: str,
        postal_code: str,
        state: str,
        street: str,
        vertical: str,
        company_name: str | Omit = omit,
        ein: str | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        stock_exchange: str | Omit = omit,
        stock_symbol: str | Omit = omit,
        website: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandCreateResponse:
        """Create a 10DLC brand registration.

        The brand starts in draft status. Submit it
        for review using the submit endpoint.

        Args:
          country: Two-letter ISO country code.

          display_name: Display name of the brand.

          entity_type: Business entity type for 10DLC brand registration.

          phone: Contact phone in E.164 format.

          vertical: Industry vertical.

          company_name: Legal company name.

          ein: Employer Identification Number (format: XX-XXXXXXX).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/10dlc/brands",
            body=await async_maybe_transform(
                {
                    "city": city,
                    "country": country,
                    "display_name": display_name,
                    "email": email,
                    "entity_type": entity_type,
                    "phone": phone,
                    "postal_code": postal_code,
                    "state": state,
                    "street": street,
                    "vertical": vertical,
                    "company_name": company_name,
                    "ein": ein,
                    "first_name": first_name,
                    "last_name": last_name,
                    "stock_exchange": stock_exchange,
                    "stock_symbol": stock_symbol,
                    "website": website,
                },
                brand_create_params.BrandCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandCreateResponse,
        )

    async def retrieve(
        self,
        brand_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveResponse:
        """
        Get 10DLC brand

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        return await self._get(
            path_template("/v1/10dlc/brands/{brand_id}", brand_id=brand_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandRetrieveResponse,
        )

    async def update(
        self,
        brand_id: str,
        *,
        city: str | Omit = omit,
        company_name: str | Omit = omit,
        country: str | Omit = omit,
        display_name: str | Omit = omit,
        ein: str | Omit = omit,
        email: str | Omit = omit,
        entity_type: Literal["PRIVATE_PROFIT", "PUBLIC_PROFIT", "NON_PROFIT", "GOVERNMENT", "SOLE_PROPRIETOR"]
        | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        phone: str | Omit = omit,
        postal_code: str | Omit = omit,
        state: str | Omit = omit,
        stock_exchange: str | Omit = omit,
        stock_symbol: str | Omit = omit,
        street: str | Omit = omit,
        vertical: str | Omit = omit,
        website: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandUpdateResponse:
        """Update a 10DLC brand in draft status.

        Cannot update after submission.

        Args:
          entity_type: Business entity type for 10DLC brand registration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        return await self._patch(
            path_template("/v1/10dlc/brands/{brand_id}", brand_id=brand_id),
            body=await async_maybe_transform(
                {
                    "city": city,
                    "company_name": company_name,
                    "country": country,
                    "display_name": display_name,
                    "ein": ein,
                    "email": email,
                    "entity_type": entity_type,
                    "first_name": first_name,
                    "last_name": last_name,
                    "phone": phone,
                    "postal_code": postal_code,
                    "state": state,
                    "stock_exchange": stock_exchange,
                    "stock_symbol": stock_symbol,
                    "street": street,
                    "vertical": vertical,
                    "website": website,
                },
                brand_update_params.BrandUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandUpdateResponse,
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
    ) -> AsyncPaginator[TenDlcBrand, AsyncCursor[TenDlcBrand]]:
        """
        List 10DLC brand registrations for this project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/10dlc/brands",
            page=AsyncCursor[TenDlcBrand],
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
                    brand_list_params.BrandListParams,
                ),
            ),
            model=TenDlcBrand,
        )

    async def delete(
        self,
        brand_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete 10DLC brand

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/10dlc/brands/{brand_id}", brand_id=brand_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list_use_cases(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandListUseCasesResponse:
        """List available use cases for 10DLC campaign registration."""
        return await self._get(
            "/v1/10dlc/brands/use-cases",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandListUseCasesResponse,
        )

    async def submit(
        self,
        brand_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandSubmitResponse:
        """Submit a draft brand to The Campaign Registry (TCR) for vetting.

        The brand must
        be in draft status. A $35 registration fee is charged from your balance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        return await self._post(
            path_template("/v1/10dlc/brands/{brand_id}/submit", brand_id=brand_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandSubmitResponse,
        )

    async def sync_status(
        self,
        brand_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandSyncStatusResponse:
        """Sync the brand status with the registration provider.

        Use this to check for
        approval updates after submission.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        return await self._post(
            path_template("/v1/10dlc/brands/{brand_id}/sync", brand_id=brand_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandSyncStatusResponse,
        )


class BrandsResourceWithRawResponse:
    def __init__(self, brands: BrandsResource) -> None:
        self._brands = brands

        self.create = to_raw_response_wrapper(
            brands.create,
        )
        self.retrieve = to_raw_response_wrapper(
            brands.retrieve,
        )
        self.update = to_raw_response_wrapper(
            brands.update,
        )
        self.list = to_raw_response_wrapper(
            brands.list,
        )
        self.delete = to_raw_response_wrapper(
            brands.delete,
        )
        self.list_use_cases = to_raw_response_wrapper(
            brands.list_use_cases,
        )
        self.submit = to_raw_response_wrapper(
            brands.submit,
        )
        self.sync_status = to_raw_response_wrapper(
            brands.sync_status,
        )


class AsyncBrandsResourceWithRawResponse:
    def __init__(self, brands: AsyncBrandsResource) -> None:
        self._brands = brands

        self.create = async_to_raw_response_wrapper(
            brands.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            brands.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            brands.update,
        )
        self.list = async_to_raw_response_wrapper(
            brands.list,
        )
        self.delete = async_to_raw_response_wrapper(
            brands.delete,
        )
        self.list_use_cases = async_to_raw_response_wrapper(
            brands.list_use_cases,
        )
        self.submit = async_to_raw_response_wrapper(
            brands.submit,
        )
        self.sync_status = async_to_raw_response_wrapper(
            brands.sync_status,
        )


class BrandsResourceWithStreamingResponse:
    def __init__(self, brands: BrandsResource) -> None:
        self._brands = brands

        self.create = to_streamed_response_wrapper(
            brands.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            brands.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            brands.update,
        )
        self.list = to_streamed_response_wrapper(
            brands.list,
        )
        self.delete = to_streamed_response_wrapper(
            brands.delete,
        )
        self.list_use_cases = to_streamed_response_wrapper(
            brands.list_use_cases,
        )
        self.submit = to_streamed_response_wrapper(
            brands.submit,
        )
        self.sync_status = to_streamed_response_wrapper(
            brands.sync_status,
        )


class AsyncBrandsResourceWithStreamingResponse:
    def __init__(self, brands: AsyncBrandsResource) -> None:
        self._brands = brands

        self.create = async_to_streamed_response_wrapper(
            brands.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            brands.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            brands.update,
        )
        self.list = async_to_streamed_response_wrapper(
            brands.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            brands.delete,
        )
        self.list_use_cases = async_to_streamed_response_wrapper(
            brands.list_use_cases,
        )
        self.submit = async_to_streamed_response_wrapper(
            brands.submit,
        )
        self.sync_status = async_to_streamed_response_wrapper(
            brands.sync_status,
        )
