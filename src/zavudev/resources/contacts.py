# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from ..types import contact_list_params, contact_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
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
from ..types.contact import Contact

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

    def retrieve(
        self,
        contact_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Contact:
        """
        Get contact

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        return self._get(
            f"/v1/contacts/{contact_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Contact,
        )

    def update(
        self,
        contact_id: str,
        *,
        default_channel: Optional[Literal["sms", "whatsapp", "telegram", "email", "instagram"]] | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Contact:
        """Update contact

        Args:
          default_channel: Preferred channel for this contact.

        Set to null to clear.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        return self._patch(
            f"/v1/contacts/{contact_id}",
            body=maybe_transform(
                {
                    "default_channel": default_channel,
                    "metadata": metadata,
                },
                contact_update_params.ContactUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Contact,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        phone_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursor[Contact]:
        """
        List contacts with their communication channels.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/contacts",
            page=SyncCursor[Contact],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "phone_number": phone_number,
                    },
                    contact_list_params.ContactListParams,
                ),
            ),
            model=Contact,
        )

    def retrieve_by_phone(
        self,
        phone_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Contact:
        """
        Get contact by phone number

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return self._get(
            f"/v1/contacts/phone/{phone_number}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Contact,
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

    async def retrieve(
        self,
        contact_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Contact:
        """
        Get contact

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        return await self._get(
            f"/v1/contacts/{contact_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Contact,
        )

    async def update(
        self,
        contact_id: str,
        *,
        default_channel: Optional[Literal["sms", "whatsapp", "telegram", "email", "instagram"]] | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Contact:
        """Update contact

        Args:
          default_channel: Preferred channel for this contact.

        Set to null to clear.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        return await self._patch(
            f"/v1/contacts/{contact_id}",
            body=await async_maybe_transform(
                {
                    "default_channel": default_channel,
                    "metadata": metadata,
                },
                contact_update_params.ContactUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Contact,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        phone_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Contact, AsyncCursor[Contact]]:
        """
        List contacts with their communication channels.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/contacts",
            page=AsyncCursor[Contact],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "phone_number": phone_number,
                    },
                    contact_list_params.ContactListParams,
                ),
            ),
            model=Contact,
        )

    async def retrieve_by_phone(
        self,
        phone_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Contact:
        """
        Get contact by phone number

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return await self._get(
            f"/v1/contacts/phone/{phone_number}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Contact,
        )


class ContactsResourceWithRawResponse:
    def __init__(self, contacts: ContactsResource) -> None:
        self._contacts = contacts

        self.retrieve = to_raw_response_wrapper(
            contacts.retrieve,
        )
        self.update = to_raw_response_wrapper(
            contacts.update,
        )
        self.list = to_raw_response_wrapper(
            contacts.list,
        )
        self.retrieve_by_phone = to_raw_response_wrapper(
            contacts.retrieve_by_phone,
        )


class AsyncContactsResourceWithRawResponse:
    def __init__(self, contacts: AsyncContactsResource) -> None:
        self._contacts = contacts

        self.retrieve = async_to_raw_response_wrapper(
            contacts.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            contacts.update,
        )
        self.list = async_to_raw_response_wrapper(
            contacts.list,
        )
        self.retrieve_by_phone = async_to_raw_response_wrapper(
            contacts.retrieve_by_phone,
        )


class ContactsResourceWithStreamingResponse:
    def __init__(self, contacts: ContactsResource) -> None:
        self._contacts = contacts

        self.retrieve = to_streamed_response_wrapper(
            contacts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            contacts.update,
        )
        self.list = to_streamed_response_wrapper(
            contacts.list,
        )
        self.retrieve_by_phone = to_streamed_response_wrapper(
            contacts.retrieve_by_phone,
        )


class AsyncContactsResourceWithStreamingResponse:
    def __init__(self, contacts: AsyncContactsResource) -> None:
        self._contacts = contacts

        self.retrieve = async_to_streamed_response_wrapper(
            contacts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            contacts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            contacts.list,
        )
        self.retrieve_by_phone = async_to_streamed_response_wrapper(
            contacts.retrieve_by_phone,
        )
