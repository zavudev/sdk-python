# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

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
from ....types.senders.agent import tool_list_params, tool_test_params, tool_create_params, tool_update_params
from ....types.senders.agent.agent_tool import AgentTool
from ....types.senders.agent.tool_test_response import ToolTestResponse
from ....types.senders.agent.tool_create_response import ToolCreateResponse
from ....types.senders.agent.tool_update_response import ToolUpdateResponse
from ....types.senders.agent.tool_retrieve_response import ToolRetrieveResponse

__all__ = ["ToolsResource", "AsyncToolsResource"]


class ToolsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ToolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return ToolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ToolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return ToolsResourceWithStreamingResponse(self)

    def create(
        self,
        sender_id: str,
        *,
        description: str,
        name: str,
        parameters: tool_create_params.Parameters,
        webhook_url: str,
        enabled: bool | Omit = omit,
        webhook_secret: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolCreateResponse:
        """Create a new tool for an agent.

        Tools allow the agent to call external webhooks.

        Args:
          webhook_url: Must be HTTPS.

          webhook_secret: Optional secret for webhook signature verification.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return self._post(
            f"/v1/senders/{sender_id}/agent/tools",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "parameters": parameters,
                    "webhook_url": webhook_url,
                    "enabled": enabled,
                    "webhook_secret": webhook_secret,
                },
                tool_create_params.ToolCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolCreateResponse,
        )

    def retrieve(
        self,
        tool_id: str,
        *,
        sender_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolRetrieveResponse:
        """
        Get a specific tool.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        return self._get(
            f"/v1/senders/{sender_id}/agent/tools/{tool_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolRetrieveResponse,
        )

    def update(
        self,
        tool_id: str,
        *,
        sender_id: str,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        name: str | Omit = omit,
        parameters: tool_update_params.Parameters | Omit = omit,
        webhook_secret: Optional[str] | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolUpdateResponse:
        """
        Update a tool.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        return self._patch(
            f"/v1/senders/{sender_id}/agent/tools/{tool_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "enabled": enabled,
                    "name": name,
                    "parameters": parameters,
                    "webhook_secret": webhook_secret,
                    "webhook_url": webhook_url,
                },
                tool_update_params.ToolUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolUpdateResponse,
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
    ) -> SyncCursor[AgentTool]:
        """
        List tools for an agent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return self._get_api_list(
            f"/v1/senders/{sender_id}/agent/tools",
            page=SyncCursor[AgentTool],
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
                    tool_list_params.ToolListParams,
                ),
            ),
            model=AgentTool,
        )

    def delete(
        self,
        tool_id: str,
        *,
        sender_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a tool.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/senders/{sender_id}/agent/tools/{tool_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def test(
        self,
        tool_id: str,
        *,
        sender_id: str,
        test_params: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolTestResponse:
        """
        Test a tool by triggering its webhook with test parameters.

        Args:
          test_params: Parameters to pass to the tool for testing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        return self._post(
            f"/v1/senders/{sender_id}/agent/tools/{tool_id}/test",
            body=maybe_transform({"test_params": test_params}, tool_test_params.ToolTestParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolTestResponse,
        )


class AsyncToolsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncToolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncToolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncToolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return AsyncToolsResourceWithStreamingResponse(self)

    async def create(
        self,
        sender_id: str,
        *,
        description: str,
        name: str,
        parameters: tool_create_params.Parameters,
        webhook_url: str,
        enabled: bool | Omit = omit,
        webhook_secret: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolCreateResponse:
        """Create a new tool for an agent.

        Tools allow the agent to call external webhooks.

        Args:
          webhook_url: Must be HTTPS.

          webhook_secret: Optional secret for webhook signature verification.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return await self._post(
            f"/v1/senders/{sender_id}/agent/tools",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "parameters": parameters,
                    "webhook_url": webhook_url,
                    "enabled": enabled,
                    "webhook_secret": webhook_secret,
                },
                tool_create_params.ToolCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolCreateResponse,
        )

    async def retrieve(
        self,
        tool_id: str,
        *,
        sender_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolRetrieveResponse:
        """
        Get a specific tool.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        return await self._get(
            f"/v1/senders/{sender_id}/agent/tools/{tool_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolRetrieveResponse,
        )

    async def update(
        self,
        tool_id: str,
        *,
        sender_id: str,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        name: str | Omit = omit,
        parameters: tool_update_params.Parameters | Omit = omit,
        webhook_secret: Optional[str] | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolUpdateResponse:
        """
        Update a tool.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        return await self._patch(
            f"/v1/senders/{sender_id}/agent/tools/{tool_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "enabled": enabled,
                    "name": name,
                    "parameters": parameters,
                    "webhook_secret": webhook_secret,
                    "webhook_url": webhook_url,
                },
                tool_update_params.ToolUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolUpdateResponse,
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
    ) -> AsyncPaginator[AgentTool, AsyncCursor[AgentTool]]:
        """
        List tools for an agent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return self._get_api_list(
            f"/v1/senders/{sender_id}/agent/tools",
            page=AsyncCursor[AgentTool],
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
                    tool_list_params.ToolListParams,
                ),
            ),
            model=AgentTool,
        )

    async def delete(
        self,
        tool_id: str,
        *,
        sender_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a tool.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/senders/{sender_id}/agent/tools/{tool_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def test(
        self,
        tool_id: str,
        *,
        sender_id: str,
        test_params: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolTestResponse:
        """
        Test a tool by triggering its webhook with test parameters.

        Args:
          test_params: Parameters to pass to the tool for testing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        return await self._post(
            f"/v1/senders/{sender_id}/agent/tools/{tool_id}/test",
            body=await async_maybe_transform({"test_params": test_params}, tool_test_params.ToolTestParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolTestResponse,
        )


class ToolsResourceWithRawResponse:
    def __init__(self, tools: ToolsResource) -> None:
        self._tools = tools

        self.create = to_raw_response_wrapper(
            tools.create,
        )
        self.retrieve = to_raw_response_wrapper(
            tools.retrieve,
        )
        self.update = to_raw_response_wrapper(
            tools.update,
        )
        self.list = to_raw_response_wrapper(
            tools.list,
        )
        self.delete = to_raw_response_wrapper(
            tools.delete,
        )
        self.test = to_raw_response_wrapper(
            tools.test,
        )


class AsyncToolsResourceWithRawResponse:
    def __init__(self, tools: AsyncToolsResource) -> None:
        self._tools = tools

        self.create = async_to_raw_response_wrapper(
            tools.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            tools.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            tools.update,
        )
        self.list = async_to_raw_response_wrapper(
            tools.list,
        )
        self.delete = async_to_raw_response_wrapper(
            tools.delete,
        )
        self.test = async_to_raw_response_wrapper(
            tools.test,
        )


class ToolsResourceWithStreamingResponse:
    def __init__(self, tools: ToolsResource) -> None:
        self._tools = tools

        self.create = to_streamed_response_wrapper(
            tools.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            tools.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            tools.update,
        )
        self.list = to_streamed_response_wrapper(
            tools.list,
        )
        self.delete = to_streamed_response_wrapper(
            tools.delete,
        )
        self.test = to_streamed_response_wrapper(
            tools.test,
        )


class AsyncToolsResourceWithStreamingResponse:
    def __init__(self, tools: AsyncToolsResource) -> None:
        self._tools = tools

        self.create = async_to_streamed_response_wrapper(
            tools.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            tools.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            tools.update,
        )
        self.list = async_to_streamed_response_wrapper(
            tools.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            tools.delete,
        )
        self.test = async_to_streamed_response_wrapper(
            tools.test,
        )
