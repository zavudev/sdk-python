# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .flows import (
    FlowsResource,
    AsyncFlowsResource,
    FlowsResourceWithRawResponse,
    AsyncFlowsResourceWithRawResponse,
    FlowsResourceWithStreamingResponse,
    AsyncFlowsResourceWithStreamingResponse,
)
from .tools import (
    ToolsResource,
    AsyncToolsResource,
    ToolsResourceWithRawResponse,
    AsyncToolsResourceWithRawResponse,
    ToolsResourceWithStreamingResponse,
    AsyncToolsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from .executions import (
    ExecutionsResource,
    AsyncExecutionsResource,
    ExecutionsResourceWithRawResponse,
    AsyncExecutionsResourceWithRawResponse,
    ExecutionsResourceWithStreamingResponse,
    AsyncExecutionsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.senders import AgentProvider, agent_create_params, agent_update_params
from ....types.senders.agent_stats import AgentStats
from ....types.senders.agent_provider import AgentProvider
from ....types.senders.agent_response import AgentResponse
from .knowledge_bases.knowledge_bases import (
    KnowledgeBasesResource,
    AsyncKnowledgeBasesResource,
    KnowledgeBasesResourceWithRawResponse,
    AsyncKnowledgeBasesResourceWithRawResponse,
    KnowledgeBasesResourceWithStreamingResponse,
    AsyncKnowledgeBasesResourceWithStreamingResponse,
)

__all__ = ["AgentResource", "AsyncAgentResource"]


class AgentResource(SyncAPIResource):
    @cached_property
    def executions(self) -> ExecutionsResource:
        return ExecutionsResource(self._client)

    @cached_property
    def flows(self) -> FlowsResource:
        return FlowsResource(self._client)

    @cached_property
    def tools(self) -> ToolsResource:
        return ToolsResource(self._client)

    @cached_property
    def knowledge_bases(self) -> KnowledgeBasesResource:
        return KnowledgeBasesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AgentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AgentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return AgentResourceWithStreamingResponse(self)

    def create(
        self,
        sender_id: str,
        *,
        model: str,
        name: str,
        provider: AgentProvider,
        system_prompt: str,
        api_key: str | Omit = omit,
        context_window_messages: int | Omit = omit,
        include_contact_metadata: bool | Omit = omit,
        max_tokens: int | Omit = omit,
        temperature: float | Omit = omit,
        trigger_on_channels: SequenceNotStr[str] | Omit = omit,
        trigger_on_message_types: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentResponse:
        """Create an AI agent for a sender.

        Each sender can have at most one agent.

        Args:
          provider: LLM provider for the AI agent.

          api_key: API key for the LLM provider. Required unless provider is 'zavu'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return self._post(
            f"/v1/senders/{sender_id}/agent",
            body=maybe_transform(
                {
                    "model": model,
                    "name": name,
                    "provider": provider,
                    "system_prompt": system_prompt,
                    "api_key": api_key,
                    "context_window_messages": context_window_messages,
                    "include_contact_metadata": include_contact_metadata,
                    "max_tokens": max_tokens,
                    "temperature": temperature,
                    "trigger_on_channels": trigger_on_channels,
                    "trigger_on_message_types": trigger_on_message_types,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentResponse,
        )

    def retrieve(
        self,
        sender_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentResponse:
        """
        Get the AI agent configuration for a sender.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return self._get(
            f"/v1/senders/{sender_id}/agent",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentResponse,
        )

    def update(
        self,
        sender_id: str,
        *,
        api_key: str | Omit = omit,
        context_window_messages: int | Omit = omit,
        enabled: bool | Omit = omit,
        include_contact_metadata: bool | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        model: str | Omit = omit,
        name: str | Omit = omit,
        provider: AgentProvider | Omit = omit,
        system_prompt: str | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        trigger_on_channels: SequenceNotStr[str] | Omit = omit,
        trigger_on_message_types: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentResponse:
        """
        Update an AI agent's configuration.

        Args:
          provider: LLM provider for the AI agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return self._patch(
            f"/v1/senders/{sender_id}/agent",
            body=maybe_transform(
                {
                    "api_key": api_key,
                    "context_window_messages": context_window_messages,
                    "enabled": enabled,
                    "include_contact_metadata": include_contact_metadata,
                    "max_tokens": max_tokens,
                    "model": model,
                    "name": name,
                    "provider": provider,
                    "system_prompt": system_prompt,
                    "temperature": temperature,
                    "trigger_on_channels": trigger_on_channels,
                    "trigger_on_message_types": trigger_on_message_types,
                },
                agent_update_params.AgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentResponse,
        )

    def delete(
        self,
        sender_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an AI agent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/senders/{sender_id}/agent",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def stats(
        self,
        sender_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentStats:
        """
        Get statistics for an AI agent including invocations, tokens, and costs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return self._get(
            f"/v1/senders/{sender_id}/agent/stats",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentStats,
        )


class AsyncAgentResource(AsyncAPIResource):
    @cached_property
    def executions(self) -> AsyncExecutionsResource:
        return AsyncExecutionsResource(self._client)

    @cached_property
    def flows(self) -> AsyncFlowsResource:
        return AsyncFlowsResource(self._client)

    @cached_property
    def tools(self) -> AsyncToolsResource:
        return AsyncToolsResource(self._client)

    @cached_property
    def knowledge_bases(self) -> AsyncKnowledgeBasesResource:
        return AsyncKnowledgeBasesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAgentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return AsyncAgentResourceWithStreamingResponse(self)

    async def create(
        self,
        sender_id: str,
        *,
        model: str,
        name: str,
        provider: AgentProvider,
        system_prompt: str,
        api_key: str | Omit = omit,
        context_window_messages: int | Omit = omit,
        include_contact_metadata: bool | Omit = omit,
        max_tokens: int | Omit = omit,
        temperature: float | Omit = omit,
        trigger_on_channels: SequenceNotStr[str] | Omit = omit,
        trigger_on_message_types: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentResponse:
        """Create an AI agent for a sender.

        Each sender can have at most one agent.

        Args:
          provider: LLM provider for the AI agent.

          api_key: API key for the LLM provider. Required unless provider is 'zavu'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return await self._post(
            f"/v1/senders/{sender_id}/agent",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "name": name,
                    "provider": provider,
                    "system_prompt": system_prompt,
                    "api_key": api_key,
                    "context_window_messages": context_window_messages,
                    "include_contact_metadata": include_contact_metadata,
                    "max_tokens": max_tokens,
                    "temperature": temperature,
                    "trigger_on_channels": trigger_on_channels,
                    "trigger_on_message_types": trigger_on_message_types,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentResponse,
        )

    async def retrieve(
        self,
        sender_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentResponse:
        """
        Get the AI agent configuration for a sender.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return await self._get(
            f"/v1/senders/{sender_id}/agent",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentResponse,
        )

    async def update(
        self,
        sender_id: str,
        *,
        api_key: str | Omit = omit,
        context_window_messages: int | Omit = omit,
        enabled: bool | Omit = omit,
        include_contact_metadata: bool | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        model: str | Omit = omit,
        name: str | Omit = omit,
        provider: AgentProvider | Omit = omit,
        system_prompt: str | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        trigger_on_channels: SequenceNotStr[str] | Omit = omit,
        trigger_on_message_types: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentResponse:
        """
        Update an AI agent's configuration.

        Args:
          provider: LLM provider for the AI agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return await self._patch(
            f"/v1/senders/{sender_id}/agent",
            body=await async_maybe_transform(
                {
                    "api_key": api_key,
                    "context_window_messages": context_window_messages,
                    "enabled": enabled,
                    "include_contact_metadata": include_contact_metadata,
                    "max_tokens": max_tokens,
                    "model": model,
                    "name": name,
                    "provider": provider,
                    "system_prompt": system_prompt,
                    "temperature": temperature,
                    "trigger_on_channels": trigger_on_channels,
                    "trigger_on_message_types": trigger_on_message_types,
                },
                agent_update_params.AgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentResponse,
        )

    async def delete(
        self,
        sender_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an AI agent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/senders/{sender_id}/agent",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def stats(
        self,
        sender_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentStats:
        """
        Get statistics for an AI agent including invocations, tokens, and costs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return await self._get(
            f"/v1/senders/{sender_id}/agent/stats",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentStats,
        )


class AgentResourceWithRawResponse:
    def __init__(self, agent: AgentResource) -> None:
        self._agent = agent

        self.create = to_raw_response_wrapper(
            agent.create,
        )
        self.retrieve = to_raw_response_wrapper(
            agent.retrieve,
        )
        self.update = to_raw_response_wrapper(
            agent.update,
        )
        self.delete = to_raw_response_wrapper(
            agent.delete,
        )
        self.stats = to_raw_response_wrapper(
            agent.stats,
        )

    @cached_property
    def executions(self) -> ExecutionsResourceWithRawResponse:
        return ExecutionsResourceWithRawResponse(self._agent.executions)

    @cached_property
    def flows(self) -> FlowsResourceWithRawResponse:
        return FlowsResourceWithRawResponse(self._agent.flows)

    @cached_property
    def tools(self) -> ToolsResourceWithRawResponse:
        return ToolsResourceWithRawResponse(self._agent.tools)

    @cached_property
    def knowledge_bases(self) -> KnowledgeBasesResourceWithRawResponse:
        return KnowledgeBasesResourceWithRawResponse(self._agent.knowledge_bases)


class AsyncAgentResourceWithRawResponse:
    def __init__(self, agent: AsyncAgentResource) -> None:
        self._agent = agent

        self.create = async_to_raw_response_wrapper(
            agent.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            agent.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            agent.update,
        )
        self.delete = async_to_raw_response_wrapper(
            agent.delete,
        )
        self.stats = async_to_raw_response_wrapper(
            agent.stats,
        )

    @cached_property
    def executions(self) -> AsyncExecutionsResourceWithRawResponse:
        return AsyncExecutionsResourceWithRawResponse(self._agent.executions)

    @cached_property
    def flows(self) -> AsyncFlowsResourceWithRawResponse:
        return AsyncFlowsResourceWithRawResponse(self._agent.flows)

    @cached_property
    def tools(self) -> AsyncToolsResourceWithRawResponse:
        return AsyncToolsResourceWithRawResponse(self._agent.tools)

    @cached_property
    def knowledge_bases(self) -> AsyncKnowledgeBasesResourceWithRawResponse:
        return AsyncKnowledgeBasesResourceWithRawResponse(self._agent.knowledge_bases)


class AgentResourceWithStreamingResponse:
    def __init__(self, agent: AgentResource) -> None:
        self._agent = agent

        self.create = to_streamed_response_wrapper(
            agent.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            agent.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            agent.update,
        )
        self.delete = to_streamed_response_wrapper(
            agent.delete,
        )
        self.stats = to_streamed_response_wrapper(
            agent.stats,
        )

    @cached_property
    def executions(self) -> ExecutionsResourceWithStreamingResponse:
        return ExecutionsResourceWithStreamingResponse(self._agent.executions)

    @cached_property
    def flows(self) -> FlowsResourceWithStreamingResponse:
        return FlowsResourceWithStreamingResponse(self._agent.flows)

    @cached_property
    def tools(self) -> ToolsResourceWithStreamingResponse:
        return ToolsResourceWithStreamingResponse(self._agent.tools)

    @cached_property
    def knowledge_bases(self) -> KnowledgeBasesResourceWithStreamingResponse:
        return KnowledgeBasesResourceWithStreamingResponse(self._agent.knowledge_bases)


class AsyncAgentResourceWithStreamingResponse:
    def __init__(self, agent: AsyncAgentResource) -> None:
        self._agent = agent

        self.create = async_to_streamed_response_wrapper(
            agent.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            agent.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            agent.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            agent.delete,
        )
        self.stats = async_to_streamed_response_wrapper(
            agent.stats,
        )

    @cached_property
    def executions(self) -> AsyncExecutionsResourceWithStreamingResponse:
        return AsyncExecutionsResourceWithStreamingResponse(self._agent.executions)

    @cached_property
    def flows(self) -> AsyncFlowsResourceWithStreamingResponse:
        return AsyncFlowsResourceWithStreamingResponse(self._agent.flows)

    @cached_property
    def tools(self) -> AsyncToolsResourceWithStreamingResponse:
        return AsyncToolsResourceWithStreamingResponse(self._agent.tools)

    @cached_property
    def knowledge_bases(self) -> AsyncKnowledgeBasesResourceWithStreamingResponse:
        return AsyncKnowledgeBasesResourceWithStreamingResponse(self._agent.knowledge_bases)
