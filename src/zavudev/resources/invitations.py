# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import invitation_list_params, invitation_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncCursor, AsyncCursor
from .._base_client import AsyncPaginator, make_request_options
from ..types.invitation import Invitation
from ..types.invitation_cancel_response import InvitationCancelResponse
from ..types.invitation_create_response import InvitationCreateResponse
from ..types.invitation_retrieve_response import InvitationRetrieveResponse

__all__ = ["InvitationsResource", "AsyncInvitationsResource"]


class InvitationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InvitationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return InvitationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InvitationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return InvitationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        allowed_phone_countries: SequenceNotStr[str] | Omit = omit,
        client_email: str | Omit = omit,
        client_name: str | Omit = omit,
        client_phone: str | Omit = omit,
        expires_in_days: int | Omit = omit,
        phone_number_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvitationCreateResponse:
        """
        Create a partner invitation link for a client to connect their WhatsApp Business
        account. The client will complete Meta's embedded signup flow and the resulting
        sender will be created in your project.

        Args:
          allowed_phone_countries: ISO country codes for allowed phone numbers.

          client_email: Email of the client being invited.

          client_name: Name of the client being invited.

          client_phone: Phone number of the client in E.164 format.

          expires_in_days: Number of days until the invitation expires.

          phone_number_id: ID of a Zavu phone number to pre-assign for WhatsApp registration. If provided,
              the client will use this number instead of their own.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/invitations",
            body=maybe_transform(
                {
                    "allowed_phone_countries": allowed_phone_countries,
                    "client_email": client_email,
                    "client_name": client_name,
                    "client_phone": client_phone,
                    "expires_in_days": expires_in_days,
                    "phone_number_id": phone_number_id,
                },
                invitation_create_params.InvitationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvitationCreateResponse,
        )

    def retrieve(
        self,
        invitation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvitationRetrieveResponse:
        """
        Get invitation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invitation_id:
            raise ValueError(f"Expected a non-empty value for `invitation_id` but received {invitation_id!r}")
        return self._get(
            path_template("/v1/invitations/{invitation_id}", invitation_id=invitation_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvitationRetrieveResponse,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["pending", "in_progress", "completed", "expired", "cancelled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursor[Invitation]:
        """
        List partner invitations for this project.

        Args:
          status: Current status of the partner invitation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/invitations",
            page=SyncCursor[Invitation],
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
                    invitation_list_params.InvitationListParams,
                ),
            ),
            model=Invitation,
        )

    def cancel(
        self,
        invitation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvitationCancelResponse:
        """Cancel an active invitation.

        The client will no longer be able to use the
        invitation link.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invitation_id:
            raise ValueError(f"Expected a non-empty value for `invitation_id` but received {invitation_id!r}")
        return self._post(
            path_template("/v1/invitations/{invitation_id}/cancel", invitation_id=invitation_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvitationCancelResponse,
        )


class AsyncInvitationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInvitationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInvitationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInvitationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return AsyncInvitationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        allowed_phone_countries: SequenceNotStr[str] | Omit = omit,
        client_email: str | Omit = omit,
        client_name: str | Omit = omit,
        client_phone: str | Omit = omit,
        expires_in_days: int | Omit = omit,
        phone_number_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvitationCreateResponse:
        """
        Create a partner invitation link for a client to connect their WhatsApp Business
        account. The client will complete Meta's embedded signup flow and the resulting
        sender will be created in your project.

        Args:
          allowed_phone_countries: ISO country codes for allowed phone numbers.

          client_email: Email of the client being invited.

          client_name: Name of the client being invited.

          client_phone: Phone number of the client in E.164 format.

          expires_in_days: Number of days until the invitation expires.

          phone_number_id: ID of a Zavu phone number to pre-assign for WhatsApp registration. If provided,
              the client will use this number instead of their own.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/invitations",
            body=await async_maybe_transform(
                {
                    "allowed_phone_countries": allowed_phone_countries,
                    "client_email": client_email,
                    "client_name": client_name,
                    "client_phone": client_phone,
                    "expires_in_days": expires_in_days,
                    "phone_number_id": phone_number_id,
                },
                invitation_create_params.InvitationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvitationCreateResponse,
        )

    async def retrieve(
        self,
        invitation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvitationRetrieveResponse:
        """
        Get invitation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invitation_id:
            raise ValueError(f"Expected a non-empty value for `invitation_id` but received {invitation_id!r}")
        return await self._get(
            path_template("/v1/invitations/{invitation_id}", invitation_id=invitation_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvitationRetrieveResponse,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["pending", "in_progress", "completed", "expired", "cancelled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Invitation, AsyncCursor[Invitation]]:
        """
        List partner invitations for this project.

        Args:
          status: Current status of the partner invitation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/invitations",
            page=AsyncCursor[Invitation],
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
                    invitation_list_params.InvitationListParams,
                ),
            ),
            model=Invitation,
        )

    async def cancel(
        self,
        invitation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvitationCancelResponse:
        """Cancel an active invitation.

        The client will no longer be able to use the
        invitation link.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invitation_id:
            raise ValueError(f"Expected a non-empty value for `invitation_id` but received {invitation_id!r}")
        return await self._post(
            path_template("/v1/invitations/{invitation_id}/cancel", invitation_id=invitation_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvitationCancelResponse,
        )


class InvitationsResourceWithRawResponse:
    def __init__(self, invitations: InvitationsResource) -> None:
        self._invitations = invitations

        self.create = to_raw_response_wrapper(
            invitations.create,
        )
        self.retrieve = to_raw_response_wrapper(
            invitations.retrieve,
        )
        self.list = to_raw_response_wrapper(
            invitations.list,
        )
        self.cancel = to_raw_response_wrapper(
            invitations.cancel,
        )


class AsyncInvitationsResourceWithRawResponse:
    def __init__(self, invitations: AsyncInvitationsResource) -> None:
        self._invitations = invitations

        self.create = async_to_raw_response_wrapper(
            invitations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            invitations.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            invitations.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            invitations.cancel,
        )


class InvitationsResourceWithStreamingResponse:
    def __init__(self, invitations: InvitationsResource) -> None:
        self._invitations = invitations

        self.create = to_streamed_response_wrapper(
            invitations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            invitations.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            invitations.list,
        )
        self.cancel = to_streamed_response_wrapper(
            invitations.cancel,
        )


class AsyncInvitationsResourceWithStreamingResponse:
    def __init__(self, invitations: AsyncInvitationsResource) -> None:
        self._invitations = invitations

        self.create = async_to_streamed_response_wrapper(
            invitations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            invitations.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            invitations.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            invitations.cancel,
        )
