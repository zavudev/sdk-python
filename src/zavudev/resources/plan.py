# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.plan_retrieve_response import PlanRetrieveResponse

__all__ = ["PlanResource", "AsyncPlanResource"]


class PlanResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PlanResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return PlanResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PlanResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return PlanResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlanRetrieveResponse:
        """
        Get the current subscription plan for the API key's team, including tier,
        billing interval, and period dates.
        """
        return self._get(
            "/v1/plan",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanRetrieveResponse,
        )


class AsyncPlanResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPlanResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPlanResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPlanResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return AsyncPlanResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlanRetrieveResponse:
        """
        Get the current subscription plan for the API key's team, including tier,
        billing interval, and period dates.
        """
        return await self._get(
            "/v1/plan",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanRetrieveResponse,
        )


class PlanResourceWithRawResponse:
    def __init__(self, plan: PlanResource) -> None:
        self._plan = plan

        self.retrieve = to_raw_response_wrapper(
            plan.retrieve,
        )


class AsyncPlanResourceWithRawResponse:
    def __init__(self, plan: AsyncPlanResource) -> None:
        self._plan = plan

        self.retrieve = async_to_raw_response_wrapper(
            plan.retrieve,
        )


class PlanResourceWithStreamingResponse:
    def __init__(self, plan: PlanResource) -> None:
        self._plan = plan

        self.retrieve = to_streamed_response_wrapper(
            plan.retrieve,
        )


class AsyncPlanResourceWithStreamingResponse:
    def __init__(self, plan: AsyncPlanResource) -> None:
        self._plan = plan

        self.retrieve = async_to_streamed_response_wrapper(
            plan.retrieve,
        )
