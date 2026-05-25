# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal

import httpx

from ...types import function_create_params, function_deploy_params, function_update_params, function_tail_logs_params
from .secrets import (
    SecretsResource,
    AsyncSecretsResource,
    SecretsResourceWithRawResponse,
    AsyncSecretsResourceWithRawResponse,
    SecretsResourceWithStreamingResponse,
    AsyncSecretsResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...types.function_create_response import FunctionCreateResponse
from ...types.function_delete_response import FunctionDeleteResponse
from ...types.function_deploy_response import FunctionDeployResponse
from ...types.function_update_response import FunctionUpdateResponse
from ...types.function_retrieve_response import FunctionRetrieveResponse
from ...types.function_tail_logs_response import FunctionTailLogsResponse
from ...types.function_get_deployment_response import FunctionGetDeploymentResponse

__all__ = ["FunctionsResource", "AsyncFunctionsResource"]


class FunctionsResource(SyncAPIResource):
    @cached_property
    def secrets(self) -> SecretsResource:
        return SecretsResource(self._client)

    @cached_property
    def with_raw_response(self) -> FunctionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return FunctionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FunctionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return FunctionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        slug: str,
        dependencies: Dict[str, str] | Omit = omit,
        description: str | Omit = omit,
        http_enabled: bool | Omit = omit,
        memory_mb: Literal[128, 256, 512, 1024] | Omit = omit,
        runtime: Literal["nodejs24"] | Omit = omit,
        source_code: str | Omit = omit,
        timeout_sec: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionCreateResponse:
        """Create a new Zavu Function.

        The function starts in `draft` status. A dedicated
        API key is auto-provisioned and injected as the `ZAVU_API_KEY` secret so the
        function can call back into the Zavu API without manual setup.

        Provide `sourceCode` to seed the draft. Call
        `POST /v1/functions/{functionId}/deploy` afterwards to publish.

        Args:
          slug: URL-safe identifier (lowercase, digits, hyphens). Must be unique per project.

          dependencies: npm dependencies. Keys are package names, values are semver ranges.

          http_enabled: Whether to expose a public HTTPS URL for this function.

          runtime: Runtime the function is deployed on.

          source_code: TypeScript source code for the function entry point (max ~900KB).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/functions",
            body=maybe_transform(
                {
                    "name": name,
                    "slug": slug,
                    "dependencies": dependencies,
                    "description": description,
                    "http_enabled": http_enabled,
                    "memory_mb": memory_mb,
                    "runtime": runtime,
                    "source_code": source_code,
                    "timeout_sec": timeout_sec,
                },
                function_create_params.FunctionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FunctionCreateResponse,
        )

    def retrieve(
        self,
        function_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionRetrieveResponse:
        """
        Get function

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return self._get(
            path_template("/v1/functions/{function_id}", function_id=function_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FunctionRetrieveResponse,
        )

    def update(
        self,
        function_id: str,
        *,
        dependencies: Dict[str, str] | Omit = omit,
        source_code: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionUpdateResponse:
        """
        Update the draft source code and/or dependency map without triggering a build.
        Visible in the dashboard immediately, but the live (deployed) function does not
        change until `POST /v1/functions/{functionId}/deploy` runs.

        Args:
          dependencies: New dependency map (replaces existing dependencies).

          source_code: New source code to publish (replaces the draft).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return self._patch(
            path_template("/v1/functions/{function_id}", function_id=function_id),
            body=maybe_transform(
                {
                    "dependencies": dependencies,
                    "source_code": source_code,
                },
                function_update_params.FunctionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FunctionUpdateResponse,
        )

    def delete(
        self,
        function_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionDeleteResponse:
        """
        Permanently delete a function and cascade: triggers, secrets, deployment
        history, managed agents+tools, and revoke the auto-provisioned API key. The AWS
        Lambda + log group are torn down asynchronously.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return self._delete(
            path_template("/v1/functions/{function_id}", function_id=function_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FunctionDeleteResponse,
        )

    def deploy(
        self,
        function_id: str,
        *,
        dependencies: Dict[str, str] | Omit = omit,
        source_code: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionDeployResponse:
        """Publish the function.

        If `sourceCode` or `dependencies` are provided in the
        body, they replace the current draft before deployment. Returns immediately with
        a deployment ID — poll `GET /v1/functions/deployments/{deploymentId}` until
        status is `active` or `failed`.

        Args:
          dependencies: New dependency map (replaces existing dependencies).

          source_code: New source code to publish (replaces the draft).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return self._post(
            path_template("/v1/functions/{function_id}/deploy", function_id=function_id),
            body=maybe_transform(
                {
                    "dependencies": dependencies,
                    "source_code": source_code,
                },
                function_deploy_params.FunctionDeployParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FunctionDeployResponse,
        )

    def get_deployment(
        self,
        deployment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionGetDeploymentResponse:
        """
        Fetch a deployment to poll its status during a deploy.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return self._get(
            path_template("/v1/functions/deployments/{deployment_id}", deployment_id=deployment_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FunctionGetDeploymentResponse,
        )

    def tail_logs(
        self,
        function_id: str,
        *,
        end_time: int | Omit = omit,
        filter_pattern: str | Omit = omit,
        limit: int | Omit = omit,
        next_token: str | Omit = omit,
        start_time: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionTailLogsResponse:
        """Fetch invocation logs for a function.

        Logs are paginated via `nextToken`. Pass
        `startTime` / `endTime` (Unix epoch milliseconds) to bound the window, or
        `filterPattern` to filter messages.

        Args:
          end_time: End of the log window in Unix epoch milliseconds.

          start_time: Start of the log window in Unix epoch milliseconds.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return self._get(
            path_template("/v1/functions/{function_id}/logs", function_id=function_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_time": end_time,
                        "filter_pattern": filter_pattern,
                        "limit": limit,
                        "next_token": next_token,
                        "start_time": start_time,
                    },
                    function_tail_logs_params.FunctionTailLogsParams,
                ),
            ),
            cast_to=FunctionTailLogsResponse,
        )


class AsyncFunctionsResource(AsyncAPIResource):
    @cached_property
    def secrets(self) -> AsyncSecretsResource:
        return AsyncSecretsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFunctionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFunctionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFunctionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return AsyncFunctionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        slug: str,
        dependencies: Dict[str, str] | Omit = omit,
        description: str | Omit = omit,
        http_enabled: bool | Omit = omit,
        memory_mb: Literal[128, 256, 512, 1024] | Omit = omit,
        runtime: Literal["nodejs24"] | Omit = omit,
        source_code: str | Omit = omit,
        timeout_sec: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionCreateResponse:
        """Create a new Zavu Function.

        The function starts in `draft` status. A dedicated
        API key is auto-provisioned and injected as the `ZAVU_API_KEY` secret so the
        function can call back into the Zavu API without manual setup.

        Provide `sourceCode` to seed the draft. Call
        `POST /v1/functions/{functionId}/deploy` afterwards to publish.

        Args:
          slug: URL-safe identifier (lowercase, digits, hyphens). Must be unique per project.

          dependencies: npm dependencies. Keys are package names, values are semver ranges.

          http_enabled: Whether to expose a public HTTPS URL for this function.

          runtime: Runtime the function is deployed on.

          source_code: TypeScript source code for the function entry point (max ~900KB).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/functions",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "slug": slug,
                    "dependencies": dependencies,
                    "description": description,
                    "http_enabled": http_enabled,
                    "memory_mb": memory_mb,
                    "runtime": runtime,
                    "source_code": source_code,
                    "timeout_sec": timeout_sec,
                },
                function_create_params.FunctionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FunctionCreateResponse,
        )

    async def retrieve(
        self,
        function_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionRetrieveResponse:
        """
        Get function

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return await self._get(
            path_template("/v1/functions/{function_id}", function_id=function_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FunctionRetrieveResponse,
        )

    async def update(
        self,
        function_id: str,
        *,
        dependencies: Dict[str, str] | Omit = omit,
        source_code: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionUpdateResponse:
        """
        Update the draft source code and/or dependency map without triggering a build.
        Visible in the dashboard immediately, but the live (deployed) function does not
        change until `POST /v1/functions/{functionId}/deploy` runs.

        Args:
          dependencies: New dependency map (replaces existing dependencies).

          source_code: New source code to publish (replaces the draft).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return await self._patch(
            path_template("/v1/functions/{function_id}", function_id=function_id),
            body=await async_maybe_transform(
                {
                    "dependencies": dependencies,
                    "source_code": source_code,
                },
                function_update_params.FunctionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FunctionUpdateResponse,
        )

    async def delete(
        self,
        function_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionDeleteResponse:
        """
        Permanently delete a function and cascade: triggers, secrets, deployment
        history, managed agents+tools, and revoke the auto-provisioned API key. The AWS
        Lambda + log group are torn down asynchronously.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return await self._delete(
            path_template("/v1/functions/{function_id}", function_id=function_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FunctionDeleteResponse,
        )

    async def deploy(
        self,
        function_id: str,
        *,
        dependencies: Dict[str, str] | Omit = omit,
        source_code: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionDeployResponse:
        """Publish the function.

        If `sourceCode` or `dependencies` are provided in the
        body, they replace the current draft before deployment. Returns immediately with
        a deployment ID — poll `GET /v1/functions/deployments/{deploymentId}` until
        status is `active` or `failed`.

        Args:
          dependencies: New dependency map (replaces existing dependencies).

          source_code: New source code to publish (replaces the draft).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return await self._post(
            path_template("/v1/functions/{function_id}/deploy", function_id=function_id),
            body=await async_maybe_transform(
                {
                    "dependencies": dependencies,
                    "source_code": source_code,
                },
                function_deploy_params.FunctionDeployParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FunctionDeployResponse,
        )

    async def get_deployment(
        self,
        deployment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionGetDeploymentResponse:
        """
        Fetch a deployment to poll its status during a deploy.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return await self._get(
            path_template("/v1/functions/deployments/{deployment_id}", deployment_id=deployment_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FunctionGetDeploymentResponse,
        )

    async def tail_logs(
        self,
        function_id: str,
        *,
        end_time: int | Omit = omit,
        filter_pattern: str | Omit = omit,
        limit: int | Omit = omit,
        next_token: str | Omit = omit,
        start_time: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionTailLogsResponse:
        """Fetch invocation logs for a function.

        Logs are paginated via `nextToken`. Pass
        `startTime` / `endTime` (Unix epoch milliseconds) to bound the window, or
        `filterPattern` to filter messages.

        Args:
          end_time: End of the log window in Unix epoch milliseconds.

          start_time: Start of the log window in Unix epoch milliseconds.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return await self._get(
            path_template("/v1/functions/{function_id}/logs", function_id=function_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_time": end_time,
                        "filter_pattern": filter_pattern,
                        "limit": limit,
                        "next_token": next_token,
                        "start_time": start_time,
                    },
                    function_tail_logs_params.FunctionTailLogsParams,
                ),
            ),
            cast_to=FunctionTailLogsResponse,
        )


class FunctionsResourceWithRawResponse:
    def __init__(self, functions: FunctionsResource) -> None:
        self._functions = functions

        self.create = to_raw_response_wrapper(
            functions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            functions.retrieve,
        )
        self.update = to_raw_response_wrapper(
            functions.update,
        )
        self.delete = to_raw_response_wrapper(
            functions.delete,
        )
        self.deploy = to_raw_response_wrapper(
            functions.deploy,
        )
        self.get_deployment = to_raw_response_wrapper(
            functions.get_deployment,
        )
        self.tail_logs = to_raw_response_wrapper(
            functions.tail_logs,
        )

    @cached_property
    def secrets(self) -> SecretsResourceWithRawResponse:
        return SecretsResourceWithRawResponse(self._functions.secrets)


class AsyncFunctionsResourceWithRawResponse:
    def __init__(self, functions: AsyncFunctionsResource) -> None:
        self._functions = functions

        self.create = async_to_raw_response_wrapper(
            functions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            functions.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            functions.update,
        )
        self.delete = async_to_raw_response_wrapper(
            functions.delete,
        )
        self.deploy = async_to_raw_response_wrapper(
            functions.deploy,
        )
        self.get_deployment = async_to_raw_response_wrapper(
            functions.get_deployment,
        )
        self.tail_logs = async_to_raw_response_wrapper(
            functions.tail_logs,
        )

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithRawResponse:
        return AsyncSecretsResourceWithRawResponse(self._functions.secrets)


class FunctionsResourceWithStreamingResponse:
    def __init__(self, functions: FunctionsResource) -> None:
        self._functions = functions

        self.create = to_streamed_response_wrapper(
            functions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            functions.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            functions.update,
        )
        self.delete = to_streamed_response_wrapper(
            functions.delete,
        )
        self.deploy = to_streamed_response_wrapper(
            functions.deploy,
        )
        self.get_deployment = to_streamed_response_wrapper(
            functions.get_deployment,
        )
        self.tail_logs = to_streamed_response_wrapper(
            functions.tail_logs,
        )

    @cached_property
    def secrets(self) -> SecretsResourceWithStreamingResponse:
        return SecretsResourceWithStreamingResponse(self._functions.secrets)


class AsyncFunctionsResourceWithStreamingResponse:
    def __init__(self, functions: AsyncFunctionsResource) -> None:
        self._functions = functions

        self.create = async_to_streamed_response_wrapper(
            functions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            functions.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            functions.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            functions.delete,
        )
        self.deploy = async_to_streamed_response_wrapper(
            functions.deploy,
        )
        self.get_deployment = async_to_streamed_response_wrapper(
            functions.get_deployment,
        )
        self.tail_logs = async_to_streamed_response_wrapper(
            functions.tail_logs,
        )

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithStreamingResponse:
        return AsyncSecretsResourceWithStreamingResponse(self._functions.secrets)
