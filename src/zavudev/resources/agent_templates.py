# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._utils import path_template
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.agent_template_list_response import AgentTemplateListResponse
from ..types.agent_template_retrieve_response import AgentTemplateRetrieveResponse

__all__ = ["AgentTemplatesResource", "AsyncAgentTemplatesResource"]


class AgentTemplatesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AgentTemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AgentTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentTemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return AgentTemplatesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        template_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentTemplateRetrieveResponse:
        """
        Fetch a single factory agent fully rendered: the function files to scaffold (an
        `index.ts` that declares the agent with `defineAgent` and its skills with
        `defineTool`) plus the secrets it needs. This is what
        `npx zavudev agents pull <id>` writes to disk before `npx zavudev deploy`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        return self._get(
            path_template("/v1/agent-templates/{template_id}", template_id=template_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentTemplateRetrieveResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentTemplateListResponse:
        """
        List the factory agents available to scaffold with `npx zavudev agents pull`.
        Each entry is a ready-made voice or text agent (system prompt, skills, and — for
        voice agents — a co-located voice config).
        """
        return self._get(
            "/v1/agent-templates",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentTemplateListResponse,
        )


class AsyncAgentTemplatesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAgentTemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentTemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return AsyncAgentTemplatesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        template_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentTemplateRetrieveResponse:
        """
        Fetch a single factory agent fully rendered: the function files to scaffold (an
        `index.ts` that declares the agent with `defineAgent` and its skills with
        `defineTool`) plus the secrets it needs. This is what
        `npx zavudev agents pull <id>` writes to disk before `npx zavudev deploy`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        return await self._get(
            path_template("/v1/agent-templates/{template_id}", template_id=template_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentTemplateRetrieveResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentTemplateListResponse:
        """
        List the factory agents available to scaffold with `npx zavudev agents pull`.
        Each entry is a ready-made voice or text agent (system prompt, skills, and — for
        voice agents — a co-located voice config).
        """
        return await self._get(
            "/v1/agent-templates",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentTemplateListResponse,
        )


class AgentTemplatesResourceWithRawResponse:
    def __init__(self, agent_templates: AgentTemplatesResource) -> None:
        self._agent_templates = agent_templates

        self.retrieve = to_raw_response_wrapper(
            agent_templates.retrieve,
        )
        self.list = to_raw_response_wrapper(
            agent_templates.list,
        )


class AsyncAgentTemplatesResourceWithRawResponse:
    def __init__(self, agent_templates: AsyncAgentTemplatesResource) -> None:
        self._agent_templates = agent_templates

        self.retrieve = async_to_raw_response_wrapper(
            agent_templates.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            agent_templates.list,
        )


class AgentTemplatesResourceWithStreamingResponse:
    def __init__(self, agent_templates: AgentTemplatesResource) -> None:
        self._agent_templates = agent_templates

        self.retrieve = to_streamed_response_wrapper(
            agent_templates.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            agent_templates.list,
        )


class AsyncAgentTemplatesResourceWithStreamingResponse:
    def __init__(self, agent_templates: AsyncAgentTemplatesResource) -> None:
        self._agent_templates = agent_templates

        self.retrieve = async_to_streamed_response_wrapper(
            agent_templates.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            agent_templates.list,
        )
