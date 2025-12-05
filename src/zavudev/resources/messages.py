# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..types import (
    Channel,
    MessageType,
    MessageStatus,
    message_list_params,
    message_send_params,
    message_react_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, strip_not_given, async_maybe_transform
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
from ..types.channel import Channel
from ..types.message import Message
from ..types.message_type import MessageType
from ..types.message_status import MessageStatus
from ..types.message_response import MessageResponse
from ..types.message_content_param import MessageContentParam

__all__ = ["MessagesResource", "AsyncMessagesResource"]


class MessagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return MessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return MessagesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageResponse:
        """
        Get message by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._get(
            f"/v1/messages/{message_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageResponse,
        )

    def list(
        self,
        *,
        channel: Channel | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        status: MessageStatus | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursor[Message]:
        """
        List messages previously sent by this project.

        Args:
          channel: Delivery channel. Use 'auto' for intelligent routing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/messages",
            page=SyncCursor[Message],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "channel": channel,
                        "cursor": cursor,
                        "limit": limit,
                        "status": status,
                        "to": to,
                    },
                    message_list_params.MessageListParams,
                ),
            ),
            model=Message,
        )

    def react(
        self,
        message_id: str,
        *,
        emoji: str,
        zavu_sender: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageResponse:
        """Send an emoji reaction to an existing WhatsApp message.

        Reactions are only
        supported for WhatsApp messages.

        Args:
          emoji: Single emoji character to react with.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        extra_headers = {**strip_not_given({"Zavu-Sender": zavu_sender}), **(extra_headers or {})}
        return self._post(
            f"/v1/messages/{message_id}/reactions",
            body=maybe_transform({"emoji": emoji}, message_react_params.MessageReactParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageResponse,
        )

    def send(
        self,
        *,
        to: str,
        channel: Channel | Omit = omit,
        content: MessageContentParam | Omit = omit,
        html_body: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        message_type: MessageType | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        reply_to: str | Omit = omit,
        subject: str | Omit = omit,
        text: str | Omit = omit,
        zavu_sender: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageResponse:
        """
        Send a message to a recipient via SMS or WhatsApp.

        **Channel selection:**

        - If `channel` is omitted and `messageType` is `text`, defaults to SMS
        - If `messageType` is anything other than `text`, WhatsApp is used automatically

        **WhatsApp 24-hour window:**

        - Free-form messages (non-template) require an open 24h window
        - Window opens when the user messages you first
        - Use template messages to initiate conversations outside the window

        Args:
          to: Recipient phone number in E.164 format or email address.

          channel: Delivery channel. Use 'auto' for intelligent routing. If omitted with non-text
              messageType, WhatsApp is used. For email recipients, defaults to 'email'.

          content: Additional content for non-text message types.

          html_body: HTML body for email messages. If provided, email will be sent as multipart with
              both text and HTML.

          idempotency_key: Optional idempotency key to avoid duplicate sends.

          message_type: Type of message. Defaults to 'text'.

          metadata: Arbitrary metadata to associate with the message.

          reply_to: Reply-To email address for email messages.

          subject: Email subject line. Required when channel is 'email' or recipient is an email
              address.

          text: Text body for text messages or caption for media messages.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Zavu-Sender": zavu_sender}), **(extra_headers or {})}
        return self._post(
            "/v1/messages",
            body=maybe_transform(
                {
                    "to": to,
                    "channel": channel,
                    "content": content,
                    "html_body": html_body,
                    "idempotency_key": idempotency_key,
                    "message_type": message_type,
                    "metadata": metadata,
                    "reply_to": reply_to,
                    "subject": subject,
                    "text": text,
                },
                message_send_params.MessageSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageResponse,
        )


class AsyncMessagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return AsyncMessagesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageResponse:
        """
        Get message by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._get(
            f"/v1/messages/{message_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageResponse,
        )

    def list(
        self,
        *,
        channel: Channel | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        status: MessageStatus | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Message, AsyncCursor[Message]]:
        """
        List messages previously sent by this project.

        Args:
          channel: Delivery channel. Use 'auto' for intelligent routing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/messages",
            page=AsyncCursor[Message],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "channel": channel,
                        "cursor": cursor,
                        "limit": limit,
                        "status": status,
                        "to": to,
                    },
                    message_list_params.MessageListParams,
                ),
            ),
            model=Message,
        )

    async def react(
        self,
        message_id: str,
        *,
        emoji: str,
        zavu_sender: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageResponse:
        """Send an emoji reaction to an existing WhatsApp message.

        Reactions are only
        supported for WhatsApp messages.

        Args:
          emoji: Single emoji character to react with.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        extra_headers = {**strip_not_given({"Zavu-Sender": zavu_sender}), **(extra_headers or {})}
        return await self._post(
            f"/v1/messages/{message_id}/reactions",
            body=await async_maybe_transform({"emoji": emoji}, message_react_params.MessageReactParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageResponse,
        )

    async def send(
        self,
        *,
        to: str,
        channel: Channel | Omit = omit,
        content: MessageContentParam | Omit = omit,
        html_body: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        message_type: MessageType | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        reply_to: str | Omit = omit,
        subject: str | Omit = omit,
        text: str | Omit = omit,
        zavu_sender: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageResponse:
        """
        Send a message to a recipient via SMS or WhatsApp.

        **Channel selection:**

        - If `channel` is omitted and `messageType` is `text`, defaults to SMS
        - If `messageType` is anything other than `text`, WhatsApp is used automatically

        **WhatsApp 24-hour window:**

        - Free-form messages (non-template) require an open 24h window
        - Window opens when the user messages you first
        - Use template messages to initiate conversations outside the window

        Args:
          to: Recipient phone number in E.164 format or email address.

          channel: Delivery channel. Use 'auto' for intelligent routing. If omitted with non-text
              messageType, WhatsApp is used. For email recipients, defaults to 'email'.

          content: Additional content for non-text message types.

          html_body: HTML body for email messages. If provided, email will be sent as multipart with
              both text and HTML.

          idempotency_key: Optional idempotency key to avoid duplicate sends.

          message_type: Type of message. Defaults to 'text'.

          metadata: Arbitrary metadata to associate with the message.

          reply_to: Reply-To email address for email messages.

          subject: Email subject line. Required when channel is 'email' or recipient is an email
              address.

          text: Text body for text messages or caption for media messages.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Zavu-Sender": zavu_sender}), **(extra_headers or {})}
        return await self._post(
            "/v1/messages",
            body=await async_maybe_transform(
                {
                    "to": to,
                    "channel": channel,
                    "content": content,
                    "html_body": html_body,
                    "idempotency_key": idempotency_key,
                    "message_type": message_type,
                    "metadata": metadata,
                    "reply_to": reply_to,
                    "subject": subject,
                    "text": text,
                },
                message_send_params.MessageSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageResponse,
        )


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.retrieve = to_raw_response_wrapper(
            messages.retrieve,
        )
        self.list = to_raw_response_wrapper(
            messages.list,
        )
        self.react = to_raw_response_wrapper(
            messages.react,
        )
        self.send = to_raw_response_wrapper(
            messages.send,
        )


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.retrieve = async_to_raw_response_wrapper(
            messages.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            messages.list,
        )
        self.react = async_to_raw_response_wrapper(
            messages.react,
        )
        self.send = async_to_raw_response_wrapper(
            messages.send,
        )


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.retrieve = to_streamed_response_wrapper(
            messages.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            messages.list,
        )
        self.react = to_streamed_response_wrapper(
            messages.react,
        )
        self.send = to_streamed_response_wrapper(
            messages.send,
        )


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.retrieve = async_to_streamed_response_wrapper(
            messages.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            messages.list,
        )
        self.react = async_to_streamed_response_wrapper(
            messages.react,
        )
        self.send = async_to_streamed_response_wrapper(
            messages.send,
        )
