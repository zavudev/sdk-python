# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ...types import BroadcastContactStatus
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
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
from ...types.broadcasts import contact_add_params, contact_list_params
from ...types.broadcast_contact import BroadcastContact
from ...types.broadcast_contact_status import BroadcastContactStatus
from ...types.broadcasts.contact_add_response import ContactAddResponse

__all__ = ["ContactsResource", "AsyncContactsResource"]


class ContactsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContactsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return ContactsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContactsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return ContactsResourceWithStreamingResponse(self)

    def list(
        self,
        broadcast_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        status: BroadcastContactStatus | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursor[BroadcastContact]:
        """
        List contacts in a broadcast with optional status filter.

        Args:
          status: Status of a contact within a broadcast.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        return self._get_api_list(
            f"/v1/broadcasts/{broadcast_id}/contacts",
            page=SyncCursor[BroadcastContact],
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
                    contact_list_params.ContactListParams,
                ),
            ),
            model=BroadcastContact,
        )

    def add(
        self,
        broadcast_id: str,
        *,
        contacts: Iterable[contact_add_params.Contact],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactAddResponse:
        """Add contacts to a broadcast in batch.

        Maximum 1000 contacts per request.

        Args:
          contacts: List of contacts to add (max 1000 per request).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        return self._post(
            f"/v1/broadcasts/{broadcast_id}/contacts",
            body=maybe_transform({"contacts": contacts}, contact_add_params.ContactAddParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactAddResponse,
        )

    def remove(
        self,
        contact_id: str,
        *,
        broadcast_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a contact from a broadcast in draft status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/broadcasts/{broadcast_id}/contacts/{contact_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncContactsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContactsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContactsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContactsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return AsyncContactsResourceWithStreamingResponse(self)

    def list(
        self,
        broadcast_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        status: BroadcastContactStatus | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[BroadcastContact, AsyncCursor[BroadcastContact]]:
        """
        List contacts in a broadcast with optional status filter.

        Args:
          status: Status of a contact within a broadcast.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        return self._get_api_list(
            f"/v1/broadcasts/{broadcast_id}/contacts",
            page=AsyncCursor[BroadcastContact],
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
                    contact_list_params.ContactListParams,
                ),
            ),
            model=BroadcastContact,
        )

    async def add(
        self,
        broadcast_id: str,
        *,
        contacts: Iterable[contact_add_params.Contact],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactAddResponse:
        """Add contacts to a broadcast in batch.

        Maximum 1000 contacts per request.

        Args:
          contacts: List of contacts to add (max 1000 per request).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        return await self._post(
            f"/v1/broadcasts/{broadcast_id}/contacts",
            body=await async_maybe_transform({"contacts": contacts}, contact_add_params.ContactAddParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactAddResponse,
        )

    async def remove(
        self,
        contact_id: str,
        *,
        broadcast_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a contact from a broadcast in draft status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/broadcasts/{broadcast_id}/contacts/{contact_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ContactsResourceWithRawResponse:
    def __init__(self, contacts: ContactsResource) -> None:
        self._contacts = contacts

        self.list = to_raw_response_wrapper(
            contacts.list,
        )
        self.add = to_raw_response_wrapper(
            contacts.add,
        )
        self.remove = to_raw_response_wrapper(
            contacts.remove,
        )


class AsyncContactsResourceWithRawResponse:
    def __init__(self, contacts: AsyncContactsResource) -> None:
        self._contacts = contacts

        self.list = async_to_raw_response_wrapper(
            contacts.list,
        )
        self.add = async_to_raw_response_wrapper(
            contacts.add,
        )
        self.remove = async_to_raw_response_wrapper(
            contacts.remove,
        )


class ContactsResourceWithStreamingResponse:
    def __init__(self, contacts: ContactsResource) -> None:
        self._contacts = contacts

        self.list = to_streamed_response_wrapper(
            contacts.list,
        )
        self.add = to_streamed_response_wrapper(
            contacts.add,
        )
        self.remove = to_streamed_response_wrapper(
            contacts.remove,
        )


class AsyncContactsResourceWithStreamingResponse:
    def __init__(self, contacts: AsyncContactsResource) -> None:
        self._contacts = contacts

        self.list = async_to_streamed_response_wrapper(
            contacts.list,
        )
        self.add = async_to_streamed_response_wrapper(
            contacts.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            contacts.remove,
        )
