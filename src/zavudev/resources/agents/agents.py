# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ...types import (
    agent_list_params,
    agent_test_params,
    agent_create_params,
    agent_update_params,
    agent_list_voices_params,
)
from .senders import (
    SendersResource,
    AsyncSendersResource,
    SendersResourceWithRawResponse,
    AsyncSendersResourceWithRawResponse,
    SendersResourceWithStreamingResponse,
    AsyncSendersResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.senders import AgentProvider
from ...types.agent_test_response import AgentTestResponse
from ...types.senders.agent.agent import Agent
from ...types.agent_create_response import AgentCreateResponse
from ...types.agent_update_response import AgentUpdateResponse
from ...types.senders.agent_provider import AgentProvider
from ...types.agent_retrieve_response import AgentRetrieveResponse
from ...types.agent_list_voices_response import AgentListVoicesResponse

__all__ = ["AgentsResource", "AsyncAgentsResource"]


class AgentsResource(SyncAPIResource):
    @cached_property
    def senders(self) -> SendersResource:
        return SendersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return AgentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        model: str,
        name: str,
        provider: AgentProvider,
        system_prompt: str,
        context_window_messages: int | Omit = omit,
        include_contact_metadata: bool | Omit = omit,
        max_tokens: int | Omit = omit,
        temperature: float | Omit = omit,
        trigger_on_channels: SequenceNotStr[str] | Omit = omit,
        trigger_on_message_types: SequenceNotStr[str] | Omit = omit,
        voice: agent_create_params.Voice | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentCreateResponse:
        """Create an agent without a sender.

        It is created disabled; connect a sender and
        enable it when you are ready for it to answer.

        **Sub-resources.** An agent's tools, flows and knowledge bases are reachable at
        `/v1/agents/{agentId}/tools`, `/v1/agents/{agentId}/flows` and
        `/v1/agents/{agentId}/knowledge-bases`, mirroring the sender-scoped routes
        documented under `/v1/senders/{senderId}/agent/...` exactly. Use the
        agent-scoped form while the agent has no sender: the sender-scoped one cannot
        address it.

        Args:
          provider: LLM provider for the AI agent.

          voice: Voice Agent configuration on a sender's AI agent. Controls how the agent behaves
              on inbound and outbound phone calls through Zavu's managed voice pipeline
              (speech recognition, the agent's LLM, and speech synthesis, with real-time
              interruption handling). Requires the Voice Agents feature to be enabled for your
              team.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/agents",
            body=maybe_transform(
                {
                    "model": model,
                    "name": name,
                    "provider": provider,
                    "system_prompt": system_prompt,
                    "context_window_messages": context_window_messages,
                    "include_contact_metadata": include_contact_metadata,
                    "max_tokens": max_tokens,
                    "temperature": temperature,
                    "trigger_on_channels": trigger_on_channels,
                    "trigger_on_message_types": trigger_on_message_types,
                    "voice": voice,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentCreateResponse,
        )

    def retrieve(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRetrieveResponse:
        """
        Get an agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            path_template("/v1/agents/{agent_id}", agent_id=agent_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRetrieveResponse,
        )

    def update(
        self,
        agent_id: str,
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
        voice: agent_update_params.Voice | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentUpdateResponse:
        """
        Update an agent

        Args:
          provider: LLM provider for the AI agent.

          voice: Voice Agent configuration. Patch this object to enable voice, change the
              greeting, or adjust call limits. Requires the Voice Agents feature to be enabled
              for your team.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._patch(
            path_template("/v1/agents/{agent_id}", agent_id=agent_id),
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
                    "voice": voice,
                },
                agent_update_params.AgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentUpdateResponse,
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
    ) -> SyncCursor[Agent]:
        """
        Every agent in the project, newest first — including agents that are not
        connected to any sender yet, which the sender-scoped routes cannot reach. Each
        item carries `senderIds`, the senders the agent answers on.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/agents",
            page=SyncCursor[Agent],
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
                    agent_list_params.AgentListParams,
                ),
            ),
            model=Agent,
        )

    def delete(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/agents/{agent_id}", agent_id=agent_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_voices(
        self,
        *,
        language: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentListVoicesResponse:
        """The voices an agent can speak with, for `voice.ttsVoiceId`.

        Filter by `language`
        to get the ones that speak it; a voice can still be used with `language: auto`,
        where the agent follows the caller and keeps the chosen voice.

        Args:
          language: BCP-47 tag (`en`, `es`, `pt-BR`). Omit, or pass `auto`, for every voice.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/agents/voices",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"language": language}, agent_list_voices_params.AgentListVoicesParams),
            ),
            cast_to=AgentListVoicesResponse,
        )

    def test(
        self,
        agent_id: str,
        *,
        message: str,
        execute_tools: bool | Omit = omit,
        history: Iterable[agent_test_params.History] | Omit = omit,
        use_knowledge_base: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentTestResponse:
        """
        Run the agent's prompt, model and knowledge base against a message and return
        the reply instead of delivering it. Writes nothing and charges nothing, so it is
        safe to call repeatedly while iterating on a prompt.

        Note that a dry run never **executes** tools — running them would cause real
        side effects. Live conversations on every channel do call them. When the agent
        has enabled tools, that gap is reported in `warnings` rather than silently
        producing an answer that looks like a tool call happened.

        Args:
          message: What to say to the agent.

          execute_tools: Run the tools the agent calls instead of reporting the choice and stopping.

              Off by default because a tool handler talks to the outside world: a rehearsal
              that charges a card is not a rehearsal. Turn it on to exercise the loop that
              actually matters — the model picks a tool, the handler answers, the model
              replies with the result — without sending a message to anyone. What ran comes
              back in `executedToolCalls`.

          history: Prior turns, oldest first, to exercise multi-turn behaviour without persisting a
              thread. Trimmed to the agent's context window.

          use_knowledge_base: Set false to skip retrieval and isolate prompt behaviour from the knowledge
              base.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._post(
            path_template("/v1/agents/{agent_id}/test", agent_id=agent_id),
            body=maybe_transform(
                {
                    "message": message,
                    "execute_tools": execute_tools,
                    "history": history,
                    "use_knowledge_base": use_knowledge_base,
                },
                agent_test_params.AgentTestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentTestResponse,
        )


class AsyncAgentsResource(AsyncAPIResource):
    @cached_property
    def senders(self) -> AsyncSendersResource:
        return AsyncSendersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return AsyncAgentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        model: str,
        name: str,
        provider: AgentProvider,
        system_prompt: str,
        context_window_messages: int | Omit = omit,
        include_contact_metadata: bool | Omit = omit,
        max_tokens: int | Omit = omit,
        temperature: float | Omit = omit,
        trigger_on_channels: SequenceNotStr[str] | Omit = omit,
        trigger_on_message_types: SequenceNotStr[str] | Omit = omit,
        voice: agent_create_params.Voice | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentCreateResponse:
        """Create an agent without a sender.

        It is created disabled; connect a sender and
        enable it when you are ready for it to answer.

        **Sub-resources.** An agent's tools, flows and knowledge bases are reachable at
        `/v1/agents/{agentId}/tools`, `/v1/agents/{agentId}/flows` and
        `/v1/agents/{agentId}/knowledge-bases`, mirroring the sender-scoped routes
        documented under `/v1/senders/{senderId}/agent/...` exactly. Use the
        agent-scoped form while the agent has no sender: the sender-scoped one cannot
        address it.

        Args:
          provider: LLM provider for the AI agent.

          voice: Voice Agent configuration on a sender's AI agent. Controls how the agent behaves
              on inbound and outbound phone calls through Zavu's managed voice pipeline
              (speech recognition, the agent's LLM, and speech synthesis, with real-time
              interruption handling). Requires the Voice Agents feature to be enabled for your
              team.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/agents",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "name": name,
                    "provider": provider,
                    "system_prompt": system_prompt,
                    "context_window_messages": context_window_messages,
                    "include_contact_metadata": include_contact_metadata,
                    "max_tokens": max_tokens,
                    "temperature": temperature,
                    "trigger_on_channels": trigger_on_channels,
                    "trigger_on_message_types": trigger_on_message_types,
                    "voice": voice,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentCreateResponse,
        )

    async def retrieve(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRetrieveResponse:
        """
        Get an agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            path_template("/v1/agents/{agent_id}", agent_id=agent_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRetrieveResponse,
        )

    async def update(
        self,
        agent_id: str,
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
        voice: agent_update_params.Voice | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentUpdateResponse:
        """
        Update an agent

        Args:
          provider: LLM provider for the AI agent.

          voice: Voice Agent configuration. Patch this object to enable voice, change the
              greeting, or adjust call limits. Requires the Voice Agents feature to be enabled
              for your team.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._patch(
            path_template("/v1/agents/{agent_id}", agent_id=agent_id),
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
                    "voice": voice,
                },
                agent_update_params.AgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentUpdateResponse,
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
    ) -> AsyncPaginator[Agent, AsyncCursor[Agent]]:
        """
        Every agent in the project, newest first — including agents that are not
        connected to any sender yet, which the sender-scoped routes cannot reach. Each
        item carries `senderIds`, the senders the agent answers on.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/agents",
            page=AsyncCursor[Agent],
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
                    agent_list_params.AgentListParams,
                ),
            ),
            model=Agent,
        )

    async def delete(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/agents/{agent_id}", agent_id=agent_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list_voices(
        self,
        *,
        language: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentListVoicesResponse:
        """The voices an agent can speak with, for `voice.ttsVoiceId`.

        Filter by `language`
        to get the ones that speak it; a voice can still be used with `language: auto`,
        where the agent follows the caller and keeps the chosen voice.

        Args:
          language: BCP-47 tag (`en`, `es`, `pt-BR`). Omit, or pass `auto`, for every voice.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/agents/voices",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"language": language}, agent_list_voices_params.AgentListVoicesParams
                ),
            ),
            cast_to=AgentListVoicesResponse,
        )

    async def test(
        self,
        agent_id: str,
        *,
        message: str,
        execute_tools: bool | Omit = omit,
        history: Iterable[agent_test_params.History] | Omit = omit,
        use_knowledge_base: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentTestResponse:
        """
        Run the agent's prompt, model and knowledge base against a message and return
        the reply instead of delivering it. Writes nothing and charges nothing, so it is
        safe to call repeatedly while iterating on a prompt.

        Note that a dry run never **executes** tools — running them would cause real
        side effects. Live conversations on every channel do call them. When the agent
        has enabled tools, that gap is reported in `warnings` rather than silently
        producing an answer that looks like a tool call happened.

        Args:
          message: What to say to the agent.

          execute_tools: Run the tools the agent calls instead of reporting the choice and stopping.

              Off by default because a tool handler talks to the outside world: a rehearsal
              that charges a card is not a rehearsal. Turn it on to exercise the loop that
              actually matters — the model picks a tool, the handler answers, the model
              replies with the result — without sending a message to anyone. What ran comes
              back in `executedToolCalls`.

          history: Prior turns, oldest first, to exercise multi-turn behaviour without persisting a
              thread. Trimmed to the agent's context window.

          use_knowledge_base: Set false to skip retrieval and isolate prompt behaviour from the knowledge
              base.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._post(
            path_template("/v1/agents/{agent_id}/test", agent_id=agent_id),
            body=await async_maybe_transform(
                {
                    "message": message,
                    "execute_tools": execute_tools,
                    "history": history,
                    "use_knowledge_base": use_knowledge_base,
                },
                agent_test_params.AgentTestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentTestResponse,
        )


class AgentsResourceWithRawResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.create = to_raw_response_wrapper(
            agents.create,
        )
        self.retrieve = to_raw_response_wrapper(
            agents.retrieve,
        )
        self.update = to_raw_response_wrapper(
            agents.update,
        )
        self.list = to_raw_response_wrapper(
            agents.list,
        )
        self.delete = to_raw_response_wrapper(
            agents.delete,
        )
        self.list_voices = to_raw_response_wrapper(
            agents.list_voices,
        )
        self.test = to_raw_response_wrapper(
            agents.test,
        )

    @cached_property
    def senders(self) -> SendersResourceWithRawResponse:
        return SendersResourceWithRawResponse(self._agents.senders)


class AsyncAgentsResourceWithRawResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create = async_to_raw_response_wrapper(
            agents.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            agents.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            agents.update,
        )
        self.list = async_to_raw_response_wrapper(
            agents.list,
        )
        self.delete = async_to_raw_response_wrapper(
            agents.delete,
        )
        self.list_voices = async_to_raw_response_wrapper(
            agents.list_voices,
        )
        self.test = async_to_raw_response_wrapper(
            agents.test,
        )

    @cached_property
    def senders(self) -> AsyncSendersResourceWithRawResponse:
        return AsyncSendersResourceWithRawResponse(self._agents.senders)


class AgentsResourceWithStreamingResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.create = to_streamed_response_wrapper(
            agents.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            agents.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            agents.update,
        )
        self.list = to_streamed_response_wrapper(
            agents.list,
        )
        self.delete = to_streamed_response_wrapper(
            agents.delete,
        )
        self.list_voices = to_streamed_response_wrapper(
            agents.list_voices,
        )
        self.test = to_streamed_response_wrapper(
            agents.test,
        )

    @cached_property
    def senders(self) -> SendersResourceWithStreamingResponse:
        return SendersResourceWithStreamingResponse(self._agents.senders)


class AsyncAgentsResourceWithStreamingResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create = async_to_streamed_response_wrapper(
            agents.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            agents.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            agents.update,
        )
        self.list = async_to_streamed_response_wrapper(
            agents.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            agents.delete,
        )
        self.list_voices = async_to_streamed_response_wrapper(
            agents.list_voices,
        )
        self.test = async_to_streamed_response_wrapper(
            agents.test,
        )

    @cached_property
    def senders(self) -> AsyncSendersResourceWithStreamingResponse:
        return AsyncSendersResourceWithStreamingResponse(self._agents.senders)
