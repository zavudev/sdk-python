# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.agents import sender_connect_params
from ...types.agents.sender_connect_response import SenderConnectResponse

__all__ = ["SendersResource", "AsyncSendersResource"]


class SendersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SendersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return SendersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SendersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return SendersResourceWithStreamingResponse(self)

    def connect(
        self,
        agent_id: str,
        *,
        sender_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SenderConnectResponse:
        """Make the agent answer on this sender.

        An agent can serve several senders; a
        sender answers with at most one agent, so connecting one that is already in use
        returns `400` naming the agent that holds it.

        Args:
          sender_id: Sender to connect.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._post(
            path_template("/v1/agents/{agent_id}/senders", agent_id=agent_id),
            body=maybe_transform({"sender_id": sender_id}, sender_connect_params.SenderConnectParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SenderConnectResponse,
        )

    def disconnect(
        self,
        sender_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Stop the agent answering on this sender.

        The agent's primary sender is part of
        the agent itself and cannot be disconnected here.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/agents/{agent_id}/senders/{sender_id}", agent_id=agent_id, sender_id=sender_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSendersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSendersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSendersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSendersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return AsyncSendersResourceWithStreamingResponse(self)

    async def connect(
        self,
        agent_id: str,
        *,
        sender_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SenderConnectResponse:
        """Make the agent answer on this sender.

        An agent can serve several senders; a
        sender answers with at most one agent, so connecting one that is already in use
        returns `400` naming the agent that holds it.

        Args:
          sender_id: Sender to connect.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._post(
            path_template("/v1/agents/{agent_id}/senders", agent_id=agent_id),
            body=await async_maybe_transform({"sender_id": sender_id}, sender_connect_params.SenderConnectParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SenderConnectResponse,
        )

    async def disconnect(
        self,
        sender_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Stop the agent answering on this sender.

        The agent's primary sender is part of
        the agent itself and cannot be disconnected here.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/agents/{agent_id}/senders/{sender_id}", agent_id=agent_id, sender_id=sender_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SendersResourceWithRawResponse:
    def __init__(self, senders: SendersResource) -> None:
        self._senders = senders

        self.connect = to_raw_response_wrapper(
            senders.connect,
        )
        self.disconnect = to_raw_response_wrapper(
            senders.disconnect,
        )


class AsyncSendersResourceWithRawResponse:
    def __init__(self, senders: AsyncSendersResource) -> None:
        self._senders = senders

        self.connect = async_to_raw_response_wrapper(
            senders.connect,
        )
        self.disconnect = async_to_raw_response_wrapper(
            senders.disconnect,
        )


class SendersResourceWithStreamingResponse:
    def __init__(self, senders: SendersResource) -> None:
        self._senders = senders

        self.connect = to_streamed_response_wrapper(
            senders.connect,
        )
        self.disconnect = to_streamed_response_wrapper(
            senders.disconnect,
        )


class AsyncSendersResourceWithStreamingResponse:
    def __init__(self, senders: AsyncSendersResource) -> None:
        self._senders = senders

        self.connect = async_to_streamed_response_wrapper(
            senders.connect,
        )
        self.disconnect = async_to_streamed_response_wrapper(
            senders.disconnect,
        )
