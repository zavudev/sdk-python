# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.senders.whatsapp_sync_retrieve_response import WhatsappSyncRetrieveResponse
from ...types.senders.whatsapp_sync_start_history_sync_response import WhatsappSyncStartHistorySyncResponse
from ...types.senders.whatsapp_sync_start_contacts_sync_response import WhatsappSyncStartContactsSyncResponse

__all__ = ["WhatsappSyncResource", "AsyncWhatsappSyncResource"]


class WhatsappSyncResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WhatsappSyncResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return WhatsappSyncResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WhatsappSyncResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return WhatsappSyncResourceWithStreamingResponse(self)

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
    ) -> WhatsappSyncRetrieveResponse:
        """Get the current sync status for a sender's WhatsApp coexistence account.

        Only
        available for senders connected in coexistence mode (WhatsApp Business App +
        Cloud API).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return self._get(
            path_template("/v1/senders/{sender_id}/whatsapp-sync", sender_id=sender_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WhatsappSyncRetrieveResponse,
        )

    def start_contacts_sync(
        self,
        sender_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WhatsappSyncStartContactsSyncResponse:
        """Initiate contact names sync from the WhatsApp Business App.

        This imports contact
        names stored in the app to Zavu. Only available for coexistence accounts with
        active status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return self._post(
            path_template("/v1/senders/{sender_id}/whatsapp-sync/contacts", sender_id=sender_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WhatsappSyncStartContactsSyncResponse,
        )

    def start_history_sync(
        self,
        sender_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WhatsappSyncStartHistorySyncResponse:
        """Initiate message history sync from the WhatsApp Business App.

        This sends a
        request to the account owner to approve sharing their conversation history. Only
        available for coexistence accounts with active status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return self._post(
            path_template("/v1/senders/{sender_id}/whatsapp-sync/history", sender_id=sender_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WhatsappSyncStartHistorySyncResponse,
        )


class AsyncWhatsappSyncResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWhatsappSyncResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWhatsappSyncResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWhatsappSyncResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return AsyncWhatsappSyncResourceWithStreamingResponse(self)

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
    ) -> WhatsappSyncRetrieveResponse:
        """Get the current sync status for a sender's WhatsApp coexistence account.

        Only
        available for senders connected in coexistence mode (WhatsApp Business App +
        Cloud API).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return await self._get(
            path_template("/v1/senders/{sender_id}/whatsapp-sync", sender_id=sender_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WhatsappSyncRetrieveResponse,
        )

    async def start_contacts_sync(
        self,
        sender_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WhatsappSyncStartContactsSyncResponse:
        """Initiate contact names sync from the WhatsApp Business App.

        This imports contact
        names stored in the app to Zavu. Only available for coexistence accounts with
        active status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return await self._post(
            path_template("/v1/senders/{sender_id}/whatsapp-sync/contacts", sender_id=sender_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WhatsappSyncStartContactsSyncResponse,
        )

    async def start_history_sync(
        self,
        sender_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WhatsappSyncStartHistorySyncResponse:
        """Initiate message history sync from the WhatsApp Business App.

        This sends a
        request to the account owner to approve sharing their conversation history. Only
        available for coexistence accounts with active status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return await self._post(
            path_template("/v1/senders/{sender_id}/whatsapp-sync/history", sender_id=sender_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WhatsappSyncStartHistorySyncResponse,
        )


class WhatsappSyncResourceWithRawResponse:
    def __init__(self, whatsapp_sync: WhatsappSyncResource) -> None:
        self._whatsapp_sync = whatsapp_sync

        self.retrieve = to_raw_response_wrapper(
            whatsapp_sync.retrieve,
        )
        self.start_contacts_sync = to_raw_response_wrapper(
            whatsapp_sync.start_contacts_sync,
        )
        self.start_history_sync = to_raw_response_wrapper(
            whatsapp_sync.start_history_sync,
        )


class AsyncWhatsappSyncResourceWithRawResponse:
    def __init__(self, whatsapp_sync: AsyncWhatsappSyncResource) -> None:
        self._whatsapp_sync = whatsapp_sync

        self.retrieve = async_to_raw_response_wrapper(
            whatsapp_sync.retrieve,
        )
        self.start_contacts_sync = async_to_raw_response_wrapper(
            whatsapp_sync.start_contacts_sync,
        )
        self.start_history_sync = async_to_raw_response_wrapper(
            whatsapp_sync.start_history_sync,
        )


class WhatsappSyncResourceWithStreamingResponse:
    def __init__(self, whatsapp_sync: WhatsappSyncResource) -> None:
        self._whatsapp_sync = whatsapp_sync

        self.retrieve = to_streamed_response_wrapper(
            whatsapp_sync.retrieve,
        )
        self.start_contacts_sync = to_streamed_response_wrapper(
            whatsapp_sync.start_contacts_sync,
        )
        self.start_history_sync = to_streamed_response_wrapper(
            whatsapp_sync.start_history_sync,
        )


class AsyncWhatsappSyncResourceWithStreamingResponse:
    def __init__(self, whatsapp_sync: AsyncWhatsappSyncResource) -> None:
        self._whatsapp_sync = whatsapp_sync

        self.retrieve = async_to_streamed_response_wrapper(
            whatsapp_sync.retrieve,
        )
        self.start_contacts_sync = async_to_streamed_response_wrapper(
            whatsapp_sync.start_contacts_sync,
        )
        self.start_history_sync = async_to_streamed_response_wrapper(
            whatsapp_sync.start_history_sync,
        )
