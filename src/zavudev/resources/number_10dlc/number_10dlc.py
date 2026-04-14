# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .brands import (
    BrandsResource,
    AsyncBrandsResource,
    BrandsResourceWithRawResponse,
    AsyncBrandsResourceWithRawResponse,
    BrandsResourceWithStreamingResponse,
    AsyncBrandsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .campaigns.campaigns import (
    CampaignsResource,
    AsyncCampaignsResource,
    CampaignsResourceWithRawResponse,
    AsyncCampaignsResourceWithRawResponse,
    CampaignsResourceWithStreamingResponse,
    AsyncCampaignsResourceWithStreamingResponse,
)

__all__ = ["Number10dlcResource", "AsyncNumber10dlcResource"]


class Number10dlcResource(SyncAPIResource):
    @cached_property
    def brands(self) -> BrandsResource:
        return BrandsResource(self._client)

    @cached_property
    def campaigns(self) -> CampaignsResource:
        return CampaignsResource(self._client)

    @cached_property
    def with_raw_response(self) -> Number10dlcResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return Number10dlcResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> Number10dlcResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return Number10dlcResourceWithStreamingResponse(self)


class AsyncNumber10dlcResource(AsyncAPIResource):
    @cached_property
    def brands(self) -> AsyncBrandsResource:
        return AsyncBrandsResource(self._client)

    @cached_property
    def campaigns(self) -> AsyncCampaignsResource:
        return AsyncCampaignsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNumber10dlcResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNumber10dlcResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNumber10dlcResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return AsyncNumber10dlcResourceWithStreamingResponse(self)


class Number10dlcResourceWithRawResponse:
    def __init__(self, number_10dlc: Number10dlcResource) -> None:
        self._number_10dlc = number_10dlc

    @cached_property
    def brands(self) -> BrandsResourceWithRawResponse:
        return BrandsResourceWithRawResponse(self._number_10dlc.brands)

    @cached_property
    def campaigns(self) -> CampaignsResourceWithRawResponse:
        return CampaignsResourceWithRawResponse(self._number_10dlc.campaigns)


class AsyncNumber10dlcResourceWithRawResponse:
    def __init__(self, number_10dlc: AsyncNumber10dlcResource) -> None:
        self._number_10dlc = number_10dlc

    @cached_property
    def brands(self) -> AsyncBrandsResourceWithRawResponse:
        return AsyncBrandsResourceWithRawResponse(self._number_10dlc.brands)

    @cached_property
    def campaigns(self) -> AsyncCampaignsResourceWithRawResponse:
        return AsyncCampaignsResourceWithRawResponse(self._number_10dlc.campaigns)


class Number10dlcResourceWithStreamingResponse:
    def __init__(self, number_10dlc: Number10dlcResource) -> None:
        self._number_10dlc = number_10dlc

    @cached_property
    def brands(self) -> BrandsResourceWithStreamingResponse:
        return BrandsResourceWithStreamingResponse(self._number_10dlc.brands)

    @cached_property
    def campaigns(self) -> CampaignsResourceWithStreamingResponse:
        return CampaignsResourceWithStreamingResponse(self._number_10dlc.campaigns)


class AsyncNumber10dlcResourceWithStreamingResponse:
    def __init__(self, number_10dlc: AsyncNumber10dlcResource) -> None:
        self._number_10dlc = number_10dlc

    @cached_property
    def brands(self) -> AsyncBrandsResourceWithStreamingResponse:
        return AsyncBrandsResourceWithStreamingResponse(self._number_10dlc.brands)

    @cached_property
    def campaigns(self) -> AsyncCampaignsResourceWithStreamingResponse:
        return AsyncCampaignsResourceWithStreamingResponse(self._number_10dlc.campaigns)
