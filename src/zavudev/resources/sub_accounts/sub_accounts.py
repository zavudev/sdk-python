# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from ...types import sub_account_list_params, sub_account_create_params, sub_account_update_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from .api_keys import (
    APIKeysResource,
    AsyncAPIKeysResource,
    APIKeysResourceWithRawResponse,
    AsyncAPIKeysResourceWithRawResponse,
    APIKeysResourceWithStreamingResponse,
    AsyncAPIKeysResourceWithStreamingResponse,
)
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
from ...types.sub_account import SubAccount
from ...types.sub_account_create_response import SubAccountCreateResponse
from ...types.sub_account_update_response import SubAccountUpdateResponse
from ...types.sub_account_retrieve_response import SubAccountRetrieveResponse
from ...types.sub_account_deactivate_response import SubAccountDeactivateResponse
from ...types.sub_account_get_balance_response import SubAccountGetBalanceResponse

__all__ = ["SubAccountsResource", "AsyncSubAccountsResource"]


class SubAccountsResource(SyncAPIResource):
    @cached_property
    def api_keys(self) -> APIKeysResource:
        return APIKeysResource(self._client)

    @cached_property
    def with_raw_response(self) -> SubAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return SubAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return SubAccountsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        credit_limit: int | Omit = omit,
        external_id: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubAccountCreateResponse:
        """Create a new sub-account (project) with its own API key.

        All charges are billed
        to the parent team's balance. Use creditLimit to set a spending cap. The
        sub-account's API key is returned only in the creation response.

        Args:
          name: Name of the sub-account.

          credit_limit: Spending cap in cents. When reached, messages from this sub-account will be
              blocked. Omit or set to 0 for no limit.

          external_id: External reference ID for your own tracking.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/sub-accounts",
            body=maybe_transform(
                {
                    "name": name,
                    "credit_limit": credit_limit,
                    "external_id": external_id,
                    "metadata": metadata,
                },
                sub_account_create_params.SubAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubAccountCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubAccountRetrieveResponse:
        """
        Get sub-account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/sub-accounts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubAccountRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        credit_limit: Optional[int] | Omit = omit,
        external_id: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        name: str | Omit = omit,
        status: Literal["active", "inactive"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubAccountUpdateResponse:
        """
        Update sub-account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/v1/sub-accounts/{id}", id=id),
            body=maybe_transform(
                {
                    "credit_limit": credit_limit,
                    "external_id": external_id,
                    "metadata": metadata,
                    "name": name,
                    "status": status,
                },
                sub_account_update_params.SubAccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubAccountUpdateResponse,
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
    ) -> SyncCursor[SubAccount]:
        """
        List sub-accounts for this team.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/sub-accounts",
            page=SyncCursor[SubAccount],
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
                    sub_account_list_params.SubAccountListParams,
                ),
            ),
            model=SubAccount,
        )

    def deactivate(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubAccountDeactivateResponse:
        """Deactivate a sub-account.

        Remaining balance is returned to the parent team and
        all API keys are revoked.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/v1/sub-accounts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubAccountDeactivateResponse,
        )

    def get_balance(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubAccountGetBalanceResponse:
        """Get spending information for a sub-account.

        Returns the parent team's balance,
        the sub-account's total spending, and its credit limit (spending cap).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/sub-accounts/{id}/balance", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubAccountGetBalanceResponse,
        )


class AsyncSubAccountsResource(AsyncAPIResource):
    @cached_property
    def api_keys(self) -> AsyncAPIKeysResource:
        return AsyncAPIKeysResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSubAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return AsyncSubAccountsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        credit_limit: int | Omit = omit,
        external_id: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubAccountCreateResponse:
        """Create a new sub-account (project) with its own API key.

        All charges are billed
        to the parent team's balance. Use creditLimit to set a spending cap. The
        sub-account's API key is returned only in the creation response.

        Args:
          name: Name of the sub-account.

          credit_limit: Spending cap in cents. When reached, messages from this sub-account will be
              blocked. Omit or set to 0 for no limit.

          external_id: External reference ID for your own tracking.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/sub-accounts",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "credit_limit": credit_limit,
                    "external_id": external_id,
                    "metadata": metadata,
                },
                sub_account_create_params.SubAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubAccountCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubAccountRetrieveResponse:
        """
        Get sub-account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/sub-accounts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubAccountRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        credit_limit: Optional[int] | Omit = omit,
        external_id: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        name: str | Omit = omit,
        status: Literal["active", "inactive"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubAccountUpdateResponse:
        """
        Update sub-account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/v1/sub-accounts/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "credit_limit": credit_limit,
                    "external_id": external_id,
                    "metadata": metadata,
                    "name": name,
                    "status": status,
                },
                sub_account_update_params.SubAccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubAccountUpdateResponse,
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
    ) -> AsyncPaginator[SubAccount, AsyncCursor[SubAccount]]:
        """
        List sub-accounts for this team.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/sub-accounts",
            page=AsyncCursor[SubAccount],
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
                    sub_account_list_params.SubAccountListParams,
                ),
            ),
            model=SubAccount,
        )

    async def deactivate(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubAccountDeactivateResponse:
        """Deactivate a sub-account.

        Remaining balance is returned to the parent team and
        all API keys are revoked.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/v1/sub-accounts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubAccountDeactivateResponse,
        )

    async def get_balance(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubAccountGetBalanceResponse:
        """Get spending information for a sub-account.

        Returns the parent team's balance,
        the sub-account's total spending, and its credit limit (spending cap).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/sub-accounts/{id}/balance", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubAccountGetBalanceResponse,
        )


class SubAccountsResourceWithRawResponse:
    def __init__(self, sub_accounts: SubAccountsResource) -> None:
        self._sub_accounts = sub_accounts

        self.create = to_raw_response_wrapper(
            sub_accounts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            sub_accounts.retrieve,
        )
        self.update = to_raw_response_wrapper(
            sub_accounts.update,
        )
        self.list = to_raw_response_wrapper(
            sub_accounts.list,
        )
        self.deactivate = to_raw_response_wrapper(
            sub_accounts.deactivate,
        )
        self.get_balance = to_raw_response_wrapper(
            sub_accounts.get_balance,
        )

    @cached_property
    def api_keys(self) -> APIKeysResourceWithRawResponse:
        return APIKeysResourceWithRawResponse(self._sub_accounts.api_keys)


class AsyncSubAccountsResourceWithRawResponse:
    def __init__(self, sub_accounts: AsyncSubAccountsResource) -> None:
        self._sub_accounts = sub_accounts

        self.create = async_to_raw_response_wrapper(
            sub_accounts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            sub_accounts.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            sub_accounts.update,
        )
        self.list = async_to_raw_response_wrapper(
            sub_accounts.list,
        )
        self.deactivate = async_to_raw_response_wrapper(
            sub_accounts.deactivate,
        )
        self.get_balance = async_to_raw_response_wrapper(
            sub_accounts.get_balance,
        )

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResourceWithRawResponse:
        return AsyncAPIKeysResourceWithRawResponse(self._sub_accounts.api_keys)


class SubAccountsResourceWithStreamingResponse:
    def __init__(self, sub_accounts: SubAccountsResource) -> None:
        self._sub_accounts = sub_accounts

        self.create = to_streamed_response_wrapper(
            sub_accounts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            sub_accounts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            sub_accounts.update,
        )
        self.list = to_streamed_response_wrapper(
            sub_accounts.list,
        )
        self.deactivate = to_streamed_response_wrapper(
            sub_accounts.deactivate,
        )
        self.get_balance = to_streamed_response_wrapper(
            sub_accounts.get_balance,
        )

    @cached_property
    def api_keys(self) -> APIKeysResourceWithStreamingResponse:
        return APIKeysResourceWithStreamingResponse(self._sub_accounts.api_keys)


class AsyncSubAccountsResourceWithStreamingResponse:
    def __init__(self, sub_accounts: AsyncSubAccountsResource) -> None:
        self._sub_accounts = sub_accounts

        self.create = async_to_streamed_response_wrapper(
            sub_accounts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            sub_accounts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            sub_accounts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            sub_accounts.list,
        )
        self.deactivate = async_to_streamed_response_wrapper(
            sub_accounts.deactivate,
        )
        self.get_balance = async_to_streamed_response_wrapper(
            sub_accounts.get_balance,
        )

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResourceWithStreamingResponse:
        return AsyncAPIKeysResourceWithStreamingResponse(self._sub_accounts.api_keys)
