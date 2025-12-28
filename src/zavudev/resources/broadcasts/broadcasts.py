# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime

import httpx

from ...types import (
    BroadcastStatus,
    BroadcastChannel,
    BroadcastMessageType,
    broadcast_list_params,
    broadcast_send_params,
    broadcast_create_params,
    broadcast_update_params,
    broadcast_reschedule_params,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from .contacts import (
    ContactsResource,
    AsyncContactsResource,
    ContactsResourceWithRawResponse,
    AsyncContactsResourceWithRawResponse,
    ContactsResourceWithStreamingResponse,
    AsyncContactsResourceWithStreamingResponse,
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
from ...types.broadcast import Broadcast
from ...types.broadcast_status import BroadcastStatus
from ...types.broadcast_channel import BroadcastChannel
from ...types.broadcast_progress import BroadcastProgress
from ...types.broadcast_message_type import BroadcastMessageType
from ...types.broadcast_content_param import BroadcastContentParam
from ...types.broadcast_send_response import BroadcastSendResponse
from ...types.broadcast_cancel_response import BroadcastCancelResponse
from ...types.broadcast_create_response import BroadcastCreateResponse
from ...types.broadcast_update_response import BroadcastUpdateResponse
from ...types.broadcast_retrieve_response import BroadcastRetrieveResponse
from ...types.broadcast_reschedule_response import BroadcastRescheduleResponse

__all__ = ["BroadcastsResource", "AsyncBroadcastsResource"]


class BroadcastsResource(SyncAPIResource):
    @cached_property
    def contacts(self) -> ContactsResource:
        return ContactsResource(self._client)

    @cached_property
    def with_raw_response(self) -> BroadcastsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return BroadcastsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BroadcastsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return BroadcastsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        channel: BroadcastChannel,
        name: str,
        content: BroadcastContentParam | Omit = omit,
        email_html_body: str | Omit = omit,
        email_subject: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        message_type: BroadcastMessageType | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        scheduled_at: Union[str, datetime] | Omit = omit,
        sender_id: str | Omit = omit,
        text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BroadcastCreateResponse:
        """Create a new broadcast campaign.

        Add contacts after creation, then send.

        Args:
          channel: Broadcast delivery channel. Use 'smart' for per-contact intelligent routing.

          name: Name of the broadcast campaign.

          content: Content for non-text broadcast message types.

          email_html_body: HTML body for email broadcasts.

          email_subject: Email subject line. Required for email broadcasts.

          idempotency_key: Idempotency key to prevent duplicate broadcasts.

          message_type: Type of message for broadcast.

          scheduled_at: Schedule the broadcast for future delivery.

          sender_id: Sender profile ID. Uses default sender if omitted.

          text: Text content or caption. Supports template variables: {{name}}, {{1}}, etc.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/broadcasts",
            body=maybe_transform(
                {
                    "channel": channel,
                    "name": name,
                    "content": content,
                    "email_html_body": email_html_body,
                    "email_subject": email_subject,
                    "idempotency_key": idempotency_key,
                    "message_type": message_type,
                    "metadata": metadata,
                    "scheduled_at": scheduled_at,
                    "sender_id": sender_id,
                    "text": text,
                },
                broadcast_create_params.BroadcastCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BroadcastCreateResponse,
        )

    def retrieve(
        self,
        broadcast_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BroadcastRetrieveResponse:
        """
        Get broadcast

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        return self._get(
            f"/v1/broadcasts/{broadcast_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BroadcastRetrieveResponse,
        )

    def update(
        self,
        broadcast_id: str,
        *,
        content: BroadcastContentParam | Omit = omit,
        email_html_body: str | Omit = omit,
        email_subject: str | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        name: str | Omit = omit,
        text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BroadcastUpdateResponse:
        """
        Update a broadcast in draft status.

        Args:
          content: Content for non-text broadcast message types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        return self._patch(
            f"/v1/broadcasts/{broadcast_id}",
            body=maybe_transform(
                {
                    "content": content,
                    "email_html_body": email_html_body,
                    "email_subject": email_subject,
                    "metadata": metadata,
                    "name": name,
                    "text": text,
                },
                broadcast_update_params.BroadcastUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BroadcastUpdateResponse,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        status: BroadcastStatus | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursor[Broadcast]:
        """
        List broadcasts for this project.

        Args:
          status: Current status of the broadcast.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/broadcasts",
            page=SyncCursor[Broadcast],
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
                    broadcast_list_params.BroadcastListParams,
                ),
            ),
            model=Broadcast,
        )

    def delete(
        self,
        broadcast_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a broadcast in draft status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/broadcasts/{broadcast_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def cancel(
        self,
        broadcast_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BroadcastCancelResponse:
        """Cancel a broadcast.

        Pending contacts will be skipped, but already queued
        messages may still be delivered.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        return self._post(
            f"/v1/broadcasts/{broadcast_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BroadcastCancelResponse,
        )

    def progress(
        self,
        broadcast_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BroadcastProgress:
        """
        Get real-time progress of a broadcast including delivery counts and estimated
        completion time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        return self._get(
            f"/v1/broadcasts/{broadcast_id}/progress",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BroadcastProgress,
        )

    def reschedule(
        self,
        broadcast_id: str,
        *,
        scheduled_at: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BroadcastRescheduleResponse:
        """Update the scheduled time for a broadcast.

        The broadcast must be in scheduled
        status.

        Args:
          scheduled_at: New scheduled time for the broadcast.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        return self._patch(
            f"/v1/broadcasts/{broadcast_id}/schedule",
            body=maybe_transform({"scheduled_at": scheduled_at}, broadcast_reschedule_params.BroadcastRescheduleParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BroadcastRescheduleResponse,
        )

    def send(
        self,
        broadcast_id: str,
        *,
        scheduled_at: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BroadcastSendResponse:
        """Start sending the broadcast immediately or schedule for later.

        Reserves the
        estimated cost from your balance.

        Args:
          scheduled_at: Schedule for future delivery. Omit to send immediately.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        return self._post(
            f"/v1/broadcasts/{broadcast_id}/send",
            body=maybe_transform({"scheduled_at": scheduled_at}, broadcast_send_params.BroadcastSendParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BroadcastSendResponse,
        )


class AsyncBroadcastsResource(AsyncAPIResource):
    @cached_property
    def contacts(self) -> AsyncContactsResource:
        return AsyncContactsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBroadcastsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBroadcastsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBroadcastsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return AsyncBroadcastsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        channel: BroadcastChannel,
        name: str,
        content: BroadcastContentParam | Omit = omit,
        email_html_body: str | Omit = omit,
        email_subject: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        message_type: BroadcastMessageType | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        scheduled_at: Union[str, datetime] | Omit = omit,
        sender_id: str | Omit = omit,
        text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BroadcastCreateResponse:
        """Create a new broadcast campaign.

        Add contacts after creation, then send.

        Args:
          channel: Broadcast delivery channel. Use 'smart' for per-contact intelligent routing.

          name: Name of the broadcast campaign.

          content: Content for non-text broadcast message types.

          email_html_body: HTML body for email broadcasts.

          email_subject: Email subject line. Required for email broadcasts.

          idempotency_key: Idempotency key to prevent duplicate broadcasts.

          message_type: Type of message for broadcast.

          scheduled_at: Schedule the broadcast for future delivery.

          sender_id: Sender profile ID. Uses default sender if omitted.

          text: Text content or caption. Supports template variables: {{name}}, {{1}}, etc.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/broadcasts",
            body=await async_maybe_transform(
                {
                    "channel": channel,
                    "name": name,
                    "content": content,
                    "email_html_body": email_html_body,
                    "email_subject": email_subject,
                    "idempotency_key": idempotency_key,
                    "message_type": message_type,
                    "metadata": metadata,
                    "scheduled_at": scheduled_at,
                    "sender_id": sender_id,
                    "text": text,
                },
                broadcast_create_params.BroadcastCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BroadcastCreateResponse,
        )

    async def retrieve(
        self,
        broadcast_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BroadcastRetrieveResponse:
        """
        Get broadcast

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        return await self._get(
            f"/v1/broadcasts/{broadcast_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BroadcastRetrieveResponse,
        )

    async def update(
        self,
        broadcast_id: str,
        *,
        content: BroadcastContentParam | Omit = omit,
        email_html_body: str | Omit = omit,
        email_subject: str | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        name: str | Omit = omit,
        text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BroadcastUpdateResponse:
        """
        Update a broadcast in draft status.

        Args:
          content: Content for non-text broadcast message types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        return await self._patch(
            f"/v1/broadcasts/{broadcast_id}",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "email_html_body": email_html_body,
                    "email_subject": email_subject,
                    "metadata": metadata,
                    "name": name,
                    "text": text,
                },
                broadcast_update_params.BroadcastUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BroadcastUpdateResponse,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        status: BroadcastStatus | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Broadcast, AsyncCursor[Broadcast]]:
        """
        List broadcasts for this project.

        Args:
          status: Current status of the broadcast.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/broadcasts",
            page=AsyncCursor[Broadcast],
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
                    broadcast_list_params.BroadcastListParams,
                ),
            ),
            model=Broadcast,
        )

    async def delete(
        self,
        broadcast_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a broadcast in draft status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/broadcasts/{broadcast_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def cancel(
        self,
        broadcast_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BroadcastCancelResponse:
        """Cancel a broadcast.

        Pending contacts will be skipped, but already queued
        messages may still be delivered.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        return await self._post(
            f"/v1/broadcasts/{broadcast_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BroadcastCancelResponse,
        )

    async def progress(
        self,
        broadcast_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BroadcastProgress:
        """
        Get real-time progress of a broadcast including delivery counts and estimated
        completion time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        return await self._get(
            f"/v1/broadcasts/{broadcast_id}/progress",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BroadcastProgress,
        )

    async def reschedule(
        self,
        broadcast_id: str,
        *,
        scheduled_at: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BroadcastRescheduleResponse:
        """Update the scheduled time for a broadcast.

        The broadcast must be in scheduled
        status.

        Args:
          scheduled_at: New scheduled time for the broadcast.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        return await self._patch(
            f"/v1/broadcasts/{broadcast_id}/schedule",
            body=await async_maybe_transform(
                {"scheduled_at": scheduled_at}, broadcast_reschedule_params.BroadcastRescheduleParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BroadcastRescheduleResponse,
        )

    async def send(
        self,
        broadcast_id: str,
        *,
        scheduled_at: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BroadcastSendResponse:
        """Start sending the broadcast immediately or schedule for later.

        Reserves the
        estimated cost from your balance.

        Args:
          scheduled_at: Schedule for future delivery. Omit to send immediately.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        return await self._post(
            f"/v1/broadcasts/{broadcast_id}/send",
            body=await async_maybe_transform({"scheduled_at": scheduled_at}, broadcast_send_params.BroadcastSendParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BroadcastSendResponse,
        )


class BroadcastsResourceWithRawResponse:
    def __init__(self, broadcasts: BroadcastsResource) -> None:
        self._broadcasts = broadcasts

        self.create = to_raw_response_wrapper(
            broadcasts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            broadcasts.retrieve,
        )
        self.update = to_raw_response_wrapper(
            broadcasts.update,
        )
        self.list = to_raw_response_wrapper(
            broadcasts.list,
        )
        self.delete = to_raw_response_wrapper(
            broadcasts.delete,
        )
        self.cancel = to_raw_response_wrapper(
            broadcasts.cancel,
        )
        self.progress = to_raw_response_wrapper(
            broadcasts.progress,
        )
        self.reschedule = to_raw_response_wrapper(
            broadcasts.reschedule,
        )
        self.send = to_raw_response_wrapper(
            broadcasts.send,
        )

    @cached_property
    def contacts(self) -> ContactsResourceWithRawResponse:
        return ContactsResourceWithRawResponse(self._broadcasts.contacts)


class AsyncBroadcastsResourceWithRawResponse:
    def __init__(self, broadcasts: AsyncBroadcastsResource) -> None:
        self._broadcasts = broadcasts

        self.create = async_to_raw_response_wrapper(
            broadcasts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            broadcasts.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            broadcasts.update,
        )
        self.list = async_to_raw_response_wrapper(
            broadcasts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            broadcasts.delete,
        )
        self.cancel = async_to_raw_response_wrapper(
            broadcasts.cancel,
        )
        self.progress = async_to_raw_response_wrapper(
            broadcasts.progress,
        )
        self.reschedule = async_to_raw_response_wrapper(
            broadcasts.reschedule,
        )
        self.send = async_to_raw_response_wrapper(
            broadcasts.send,
        )

    @cached_property
    def contacts(self) -> AsyncContactsResourceWithRawResponse:
        return AsyncContactsResourceWithRawResponse(self._broadcasts.contacts)


class BroadcastsResourceWithStreamingResponse:
    def __init__(self, broadcasts: BroadcastsResource) -> None:
        self._broadcasts = broadcasts

        self.create = to_streamed_response_wrapper(
            broadcasts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            broadcasts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            broadcasts.update,
        )
        self.list = to_streamed_response_wrapper(
            broadcasts.list,
        )
        self.delete = to_streamed_response_wrapper(
            broadcasts.delete,
        )
        self.cancel = to_streamed_response_wrapper(
            broadcasts.cancel,
        )
        self.progress = to_streamed_response_wrapper(
            broadcasts.progress,
        )
        self.reschedule = to_streamed_response_wrapper(
            broadcasts.reschedule,
        )
        self.send = to_streamed_response_wrapper(
            broadcasts.send,
        )

    @cached_property
    def contacts(self) -> ContactsResourceWithStreamingResponse:
        return ContactsResourceWithStreamingResponse(self._broadcasts.contacts)


class AsyncBroadcastsResourceWithStreamingResponse:
    def __init__(self, broadcasts: AsyncBroadcastsResource) -> None:
        self._broadcasts = broadcasts

        self.create = async_to_streamed_response_wrapper(
            broadcasts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            broadcasts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            broadcasts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            broadcasts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            broadcasts.delete,
        )
        self.cancel = async_to_streamed_response_wrapper(
            broadcasts.cancel,
        )
        self.progress = async_to_streamed_response_wrapper(
            broadcasts.progress,
        )
        self.reschedule = async_to_streamed_response_wrapper(
            broadcasts.reschedule,
        )
        self.send = async_to_streamed_response_wrapper(
            broadcasts.send,
        )

    @cached_property
    def contacts(self) -> AsyncContactsResourceWithStreamingResponse:
        return AsyncContactsResourceWithStreamingResponse(self._broadcasts.contacts)
