# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncCursor, AsyncCursor
from ...._base_client import AsyncPaginator, make_request_options
from ....types.senders.agent import flow_list_params, flow_create_params, flow_update_params, flow_duplicate_params
from ....types.senders.agent.agent_flow import AgentFlow
from ....types.senders.agent.flow_create_response import FlowCreateResponse
from ....types.senders.agent.flow_update_response import FlowUpdateResponse
from ....types.senders.agent.flow_retrieve_response import FlowRetrieveResponse
from ....types.senders.agent.flow_duplicate_response import FlowDuplicateResponse

__all__ = ["FlowsResource", "AsyncFlowsResource"]


class FlowsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FlowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return FlowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FlowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return FlowsResourceWithStreamingResponse(self)

    def create(
        self,
        sender_id: str,
        *,
        name: str,
        steps: Iterable[flow_create_params.Step],
        trigger: flow_create_params.Trigger,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        priority: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlowCreateResponse:
        """
        Create a new flow for an agent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return self._post(
            f"/v1/senders/{sender_id}/agent/flows",
            body=maybe_transform(
                {
                    "name": name,
                    "steps": steps,
                    "trigger": trigger,
                    "description": description,
                    "enabled": enabled,
                    "priority": priority,
                },
                flow_create_params.FlowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FlowCreateResponse,
        )

    def retrieve(
        self,
        flow_id: str,
        *,
        sender_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlowRetrieveResponse:
        """
        Get a specific flow.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return self._get(
            f"/v1/senders/{sender_id}/agent/flows/{flow_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FlowRetrieveResponse,
        )

    def update(
        self,
        flow_id: str,
        *,
        sender_id: str,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        name: str | Omit = omit,
        priority: int | Omit = omit,
        steps: Iterable[flow_update_params.Step] | Omit = omit,
        trigger: flow_update_params.Trigger | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlowUpdateResponse:
        """
        Update a flow.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return self._patch(
            f"/v1/senders/{sender_id}/agent/flows/{flow_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "enabled": enabled,
                    "name": name,
                    "priority": priority,
                    "steps": steps,
                    "trigger": trigger,
                },
                flow_update_params.FlowUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FlowUpdateResponse,
        )

    def list(
        self,
        sender_id: str,
        *,
        cursor: str | Omit = omit,
        enabled: bool | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursor[AgentFlow]:
        """
        List flows for an agent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return self._get_api_list(
            f"/v1/senders/{sender_id}/agent/flows",
            page=SyncCursor[AgentFlow],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "enabled": enabled,
                        "limit": limit,
                    },
                    flow_list_params.FlowListParams,
                ),
            ),
            model=AgentFlow,
        )

    def delete(
        self,
        flow_id: str,
        *,
        sender_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a flow.

        Cannot delete flows with active sessions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/senders/{sender_id}/agent/flows/{flow_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def duplicate(
        self,
        flow_id: str,
        *,
        sender_id: str,
        new_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlowDuplicateResponse:
        """
        Create a copy of an existing flow with a new name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return self._post(
            f"/v1/senders/{sender_id}/agent/flows/{flow_id}/duplicate",
            body=maybe_transform({"new_name": new_name}, flow_duplicate_params.FlowDuplicateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FlowDuplicateResponse,
        )


class AsyncFlowsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFlowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFlowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFlowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return AsyncFlowsResourceWithStreamingResponse(self)

    async def create(
        self,
        sender_id: str,
        *,
        name: str,
        steps: Iterable[flow_create_params.Step],
        trigger: flow_create_params.Trigger,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        priority: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlowCreateResponse:
        """
        Create a new flow for an agent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return await self._post(
            f"/v1/senders/{sender_id}/agent/flows",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "steps": steps,
                    "trigger": trigger,
                    "description": description,
                    "enabled": enabled,
                    "priority": priority,
                },
                flow_create_params.FlowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FlowCreateResponse,
        )

    async def retrieve(
        self,
        flow_id: str,
        *,
        sender_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlowRetrieveResponse:
        """
        Get a specific flow.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return await self._get(
            f"/v1/senders/{sender_id}/agent/flows/{flow_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FlowRetrieveResponse,
        )

    async def update(
        self,
        flow_id: str,
        *,
        sender_id: str,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        name: str | Omit = omit,
        priority: int | Omit = omit,
        steps: Iterable[flow_update_params.Step] | Omit = omit,
        trigger: flow_update_params.Trigger | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlowUpdateResponse:
        """
        Update a flow.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return await self._patch(
            f"/v1/senders/{sender_id}/agent/flows/{flow_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "enabled": enabled,
                    "name": name,
                    "priority": priority,
                    "steps": steps,
                    "trigger": trigger,
                },
                flow_update_params.FlowUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FlowUpdateResponse,
        )

    def list(
        self,
        sender_id: str,
        *,
        cursor: str | Omit = omit,
        enabled: bool | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AgentFlow, AsyncCursor[AgentFlow]]:
        """
        List flows for an agent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return self._get_api_list(
            f"/v1/senders/{sender_id}/agent/flows",
            page=AsyncCursor[AgentFlow],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "enabled": enabled,
                        "limit": limit,
                    },
                    flow_list_params.FlowListParams,
                ),
            ),
            model=AgentFlow,
        )

    async def delete(
        self,
        flow_id: str,
        *,
        sender_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a flow.

        Cannot delete flows with active sessions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/senders/{sender_id}/agent/flows/{flow_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def duplicate(
        self,
        flow_id: str,
        *,
        sender_id: str,
        new_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlowDuplicateResponse:
        """
        Create a copy of an existing flow with a new name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return await self._post(
            f"/v1/senders/{sender_id}/agent/flows/{flow_id}/duplicate",
            body=await async_maybe_transform({"new_name": new_name}, flow_duplicate_params.FlowDuplicateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FlowDuplicateResponse,
        )


class FlowsResourceWithRawResponse:
    def __init__(self, flows: FlowsResource) -> None:
        self._flows = flows

        self.create = to_raw_response_wrapper(
            flows.create,
        )
        self.retrieve = to_raw_response_wrapper(
            flows.retrieve,
        )
        self.update = to_raw_response_wrapper(
            flows.update,
        )
        self.list = to_raw_response_wrapper(
            flows.list,
        )
        self.delete = to_raw_response_wrapper(
            flows.delete,
        )
        self.duplicate = to_raw_response_wrapper(
            flows.duplicate,
        )


class AsyncFlowsResourceWithRawResponse:
    def __init__(self, flows: AsyncFlowsResource) -> None:
        self._flows = flows

        self.create = async_to_raw_response_wrapper(
            flows.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            flows.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            flows.update,
        )
        self.list = async_to_raw_response_wrapper(
            flows.list,
        )
        self.delete = async_to_raw_response_wrapper(
            flows.delete,
        )
        self.duplicate = async_to_raw_response_wrapper(
            flows.duplicate,
        )


class FlowsResourceWithStreamingResponse:
    def __init__(self, flows: FlowsResource) -> None:
        self._flows = flows

        self.create = to_streamed_response_wrapper(
            flows.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            flows.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            flows.update,
        )
        self.list = to_streamed_response_wrapper(
            flows.list,
        )
        self.delete = to_streamed_response_wrapper(
            flows.delete,
        )
        self.duplicate = to_streamed_response_wrapper(
            flows.duplicate,
        )


class AsyncFlowsResourceWithStreamingResponse:
    def __init__(self, flows: AsyncFlowsResource) -> None:
        self._flows = flows

        self.create = async_to_streamed_response_wrapper(
            flows.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            flows.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            flows.update,
        )
        self.list = async_to_streamed_response_wrapper(
            flows.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            flows.delete,
        )
        self.duplicate = async_to_streamed_response_wrapper(
            flows.duplicate,
        )
