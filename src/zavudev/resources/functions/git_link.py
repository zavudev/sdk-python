# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ...types.functions import git_link_link_params, git_link_update_params
from ...types.functions.git_link_link_response import GitLinkLinkResponse
from ...types.functions.git_link_update_response import GitLinkUpdateResponse
from ...types.functions.git_link_retrieve_response import GitLinkRetrieveResponse
from ...types.functions.git_link_deploy_now_response import GitLinkDeployNowResponse

__all__ = ["GitLinkResource", "AsyncGitLinkResource"]


class GitLinkResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GitLinkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return GitLinkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GitLinkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return GitLinkResourceWithStreamingResponse(self)

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
    ) -> GitLinkRetrieveResponse:
        """The link and its last deploy.

        Never returns the webhook secret.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return self._get(
            path_template("/v1/functions/{function_id}/git-link", function_id=function_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GitLinkRetrieveResponse,
        )

    def update(
        self,
        function_id: str,
        *,
        auto_deploy: bool | Omit = omit,
        branch: str | Omit = omit,
        root_dir: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GitLinkUpdateResponse:
        """Change the branch, the root directory, or whether pushes deploy.

        Pass at least
        one field. `rootDir: null` clears the subdirectory.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return self._patch(
            path_template("/v1/functions/{function_id}/git-link", function_id=function_id),
            body=maybe_transform(
                {
                    "auto_deploy": auto_deploy,
                    "branch": branch,
                    "root_dir": root_dir,
                },
                git_link_update_params.GitLinkUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GitLinkUpdateResponse,
        )

    def deploy_now(
        self,
        function_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GitLinkDeployNowResponse:
        """Fetch the linked branch and deploy it without waiting for a push.

        Returns
        immediately; follow the outcome with `GET /v1/functions/{functionId}/git-link`,
        whose `lastStatus` and `lastError` describe the run.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return self._post(
            path_template("/v1/functions/{function_id}/git-link/deploy", function_id=function_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GitLinkDeployNowResponse,
        )

    def link(
        self,
        function_id: str,
        *,
        owner: str,
        repo: str,
        auto_deploy: bool | Omit = omit,
        branch: str | Omit = omit,
        root_dir: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GitLinkLinkResponse:
        """Bind a repository to this function so every push to `branch` deploys it.

        A
        function holds at most one link; linking again returns 400.

        **The server decides how the link authenticates.** If the project has the Zavu
        GitHub App installed, the link uses that installation: private repositories work
        and there is nothing to configure in the repository. Otherwise it falls back to
        a manual link and the response carries a `webhookSecret` you add to the
        repository yourself. `connection` says which one you got.

        The repository is not checked against GitHub here, because it cannot be: an
        owner/repo that does not exist, or that the installation cannot see, is accepted
        and fails on the first deploy with a fetch error.

        Args:
          root_dir: Subdirectory holding the project, for monorepos.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return self._post(
            path_template("/v1/functions/{function_id}/git-link", function_id=function_id),
            body=maybe_transform(
                {
                    "owner": owner,
                    "repo": repo,
                    "auto_deploy": auto_deploy,
                    "branch": branch,
                    "root_dir": root_dir,
                },
                git_link_link_params.GitLinkLinkParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GitLinkLinkResponse,
        )

    def unlink(
        self,
        function_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Remove the link.

        The function and its deployments stay. A manual webhook left in
        the repository stops being accepted, so remove it there too.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/functions/{function_id}/git-link", function_id=function_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncGitLinkResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGitLinkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGitLinkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGitLinkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return AsyncGitLinkResourceWithStreamingResponse(self)

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
    ) -> GitLinkRetrieveResponse:
        """The link and its last deploy.

        Never returns the webhook secret.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return await self._get(
            path_template("/v1/functions/{function_id}/git-link", function_id=function_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GitLinkRetrieveResponse,
        )

    async def update(
        self,
        function_id: str,
        *,
        auto_deploy: bool | Omit = omit,
        branch: str | Omit = omit,
        root_dir: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GitLinkUpdateResponse:
        """Change the branch, the root directory, or whether pushes deploy.

        Pass at least
        one field. `rootDir: null` clears the subdirectory.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return await self._patch(
            path_template("/v1/functions/{function_id}/git-link", function_id=function_id),
            body=await async_maybe_transform(
                {
                    "auto_deploy": auto_deploy,
                    "branch": branch,
                    "root_dir": root_dir,
                },
                git_link_update_params.GitLinkUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GitLinkUpdateResponse,
        )

    async def deploy_now(
        self,
        function_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GitLinkDeployNowResponse:
        """Fetch the linked branch and deploy it without waiting for a push.

        Returns
        immediately; follow the outcome with `GET /v1/functions/{functionId}/git-link`,
        whose `lastStatus` and `lastError` describe the run.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return await self._post(
            path_template("/v1/functions/{function_id}/git-link/deploy", function_id=function_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GitLinkDeployNowResponse,
        )

    async def link(
        self,
        function_id: str,
        *,
        owner: str,
        repo: str,
        auto_deploy: bool | Omit = omit,
        branch: str | Omit = omit,
        root_dir: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GitLinkLinkResponse:
        """Bind a repository to this function so every push to `branch` deploys it.

        A
        function holds at most one link; linking again returns 400.

        **The server decides how the link authenticates.** If the project has the Zavu
        GitHub App installed, the link uses that installation: private repositories work
        and there is nothing to configure in the repository. Otherwise it falls back to
        a manual link and the response carries a `webhookSecret` you add to the
        repository yourself. `connection` says which one you got.

        The repository is not checked against GitHub here, because it cannot be: an
        owner/repo that does not exist, or that the installation cannot see, is accepted
        and fails on the first deploy with a fetch error.

        Args:
          root_dir: Subdirectory holding the project, for monorepos.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return await self._post(
            path_template("/v1/functions/{function_id}/git-link", function_id=function_id),
            body=await async_maybe_transform(
                {
                    "owner": owner,
                    "repo": repo,
                    "auto_deploy": auto_deploy,
                    "branch": branch,
                    "root_dir": root_dir,
                },
                git_link_link_params.GitLinkLinkParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GitLinkLinkResponse,
        )

    async def unlink(
        self,
        function_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Remove the link.

        The function and its deployments stay. A manual webhook left in
        the repository stops being accepted, so remove it there too.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/functions/{function_id}/git-link", function_id=function_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class GitLinkResourceWithRawResponse:
    def __init__(self, git_link: GitLinkResource) -> None:
        self._git_link = git_link

        self.retrieve = to_raw_response_wrapper(
            git_link.retrieve,
        )
        self.update = to_raw_response_wrapper(
            git_link.update,
        )
        self.deploy_now = to_raw_response_wrapper(
            git_link.deploy_now,
        )
        self.link = to_raw_response_wrapper(
            git_link.link,
        )
        self.unlink = to_raw_response_wrapper(
            git_link.unlink,
        )


class AsyncGitLinkResourceWithRawResponse:
    def __init__(self, git_link: AsyncGitLinkResource) -> None:
        self._git_link = git_link

        self.retrieve = async_to_raw_response_wrapper(
            git_link.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            git_link.update,
        )
        self.deploy_now = async_to_raw_response_wrapper(
            git_link.deploy_now,
        )
        self.link = async_to_raw_response_wrapper(
            git_link.link,
        )
        self.unlink = async_to_raw_response_wrapper(
            git_link.unlink,
        )


class GitLinkResourceWithStreamingResponse:
    def __init__(self, git_link: GitLinkResource) -> None:
        self._git_link = git_link

        self.retrieve = to_streamed_response_wrapper(
            git_link.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            git_link.update,
        )
        self.deploy_now = to_streamed_response_wrapper(
            git_link.deploy_now,
        )
        self.link = to_streamed_response_wrapper(
            git_link.link,
        )
        self.unlink = to_streamed_response_wrapper(
            git_link.unlink,
        )


class AsyncGitLinkResourceWithStreamingResponse:
    def __init__(self, git_link: AsyncGitLinkResource) -> None:
        self._git_link = git_link

        self.retrieve = async_to_streamed_response_wrapper(
            git_link.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            git_link.update,
        )
        self.deploy_now = async_to_streamed_response_wrapper(
            git_link.deploy_now,
        )
        self.link = async_to_streamed_response_wrapper(
            git_link.link,
        )
        self.unlink = async_to_streamed_response_wrapper(
            git_link.unlink,
        )
