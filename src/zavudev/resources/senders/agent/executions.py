# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform
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
from ....types.senders import AgentExecutionStatus
from ....types.senders.agent import execution_list_params
from ....types.senders.agent_execution import AgentExecution
from ....types.senders.agent_execution_status import AgentExecutionStatus

__all__ = ["ExecutionsResource", "AsyncExecutionsResource"]


class ExecutionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExecutionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return ExecutionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExecutionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return ExecutionsResourceWithStreamingResponse(self)

    def list(
        self,
        sender_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        status: AgentExecutionStatus | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursor[AgentExecution]:
        """
        List recent agent executions with pagination.

        Args:
          status: Status of an agent execution.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return self._get_api_list(
            f"/v1/senders/{sender_id}/agent/executions",
            page=SyncCursor[AgentExecution],
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
                    execution_list_params.ExecutionListParams,
                ),
            ),
            model=AgentExecution,
        )


class AsyncExecutionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExecutionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExecutionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExecutionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return AsyncExecutionsResourceWithStreamingResponse(self)

    def list(
        self,
        sender_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        status: AgentExecutionStatus | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AgentExecution, AsyncCursor[AgentExecution]]:
        """
        List recent agent executions with pagination.

        Args:
          status: Status of an agent execution.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return self._get_api_list(
            f"/v1/senders/{sender_id}/agent/executions",
            page=AsyncCursor[AgentExecution],
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
                    execution_list_params.ExecutionListParams,
                ),
            ),
            model=AgentExecution,
        )


class ExecutionsResourceWithRawResponse:
    def __init__(self, executions: ExecutionsResource) -> None:
        self._executions = executions

        self.list = to_raw_response_wrapper(
            executions.list,
        )


class AsyncExecutionsResourceWithRawResponse:
    def __init__(self, executions: AsyncExecutionsResource) -> None:
        self._executions = executions

        self.list = async_to_raw_response_wrapper(
            executions.list,
        )


class ExecutionsResourceWithStreamingResponse:
    def __init__(self, executions: ExecutionsResource) -> None:
        self._executions = executions

        self.list = to_streamed_response_wrapper(
            executions.list,
        )


class AsyncExecutionsResourceWithStreamingResponse:
    def __init__(self, executions: AsyncExecutionsResource) -> None:
        self._executions = executions

        self.list = async_to_streamed_response_wrapper(
            executions.list,
        )
