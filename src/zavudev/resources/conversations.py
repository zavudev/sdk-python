# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import conversation_list_params, conversation_list_messages_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform
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
from ..types.message import Message
from ..types.conversation_list_response import ConversationListResponse
from ..types.conversation_retrieve_response import ConversationRetrieveResponse
from ..types.conversation_mark_as_read_response import ConversationMarkAsReadResponse

__all__ = ["ConversationsResource", "AsyncConversationsResource"]


class ConversationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConversationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return ConversationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConversationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return ConversationsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        conversation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationRetrieveResponse:
        """
        Get conversation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return self._get(
            path_template("/v1/conversations/{conversation_id}", conversation_id=conversation_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationRetrieveResponse,
        )

    def list(
        self,
        *,
        channel: Literal["sms", "sms_oneway", "whatsapp", "email", "telegram", "instagram", "messenger", "voice"]
        | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        search: str | Omit = omit,
        sender_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursor[ConversationListResponse]:
        """List inbox threads, most recently active first.

        A conversation groups every
        message with one contact across channels, which is what you need to build an
        inbox: `GET /v1/messages` returns a flat log with no thread to hang it on.

        Use `senderId` to scope the list to a single number, and `channel` to keep only
        threads that have carried that channel.

        Args:
          channel: Keep only threads that have carried this channel.

          cursor: Opaque cursor from a previous response's `nextCursor`. Do not construct it.

          search: Search threads by identity: phone number (any format — `+1 (555) 123-4567` and
              `15551234567` both match), email address (full or local part), WhatsApp group
              subject, WhatsApp username, or BSUID. Matching is by whole word, with prefix
              matching on the last term, so `mar` finds `maria@example.com` and `+1555` finds
              `+15551234567`; a fragment from the middle or end of a number (`4567`) does not
              match.

              It does **not** search message bodies — only who the thread is with.

              Results come back ranked by relevance rather than by recency, so the usual "most
              recently active first" ordering does not apply while `q` is set. `senderId` and
              `channel` still narrow the results, and `cursor` paginates them as usual. An
              empty or whitespace-only `q` returns no items rather than the full list.

          sender_id: Keep only threads last handled by this sender.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/conversations",
            page=SyncCursor[ConversationListResponse],
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
                        "search": search,
                        "sender_id": sender_id,
                    },
                    conversation_list_params.ConversationListParams,
                ),
            ),
            model=ConversationListResponse,
        )

    def list_messages(
        self,
        conversation_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursor[Message]:
        """
        Messages in this thread, newest first, across every channel it has carried.
        Reply with `POST /v1/messages`, passing the conversation's `senderId` as the
        `Zavu-Sender` header so the answer leaves from the number the contact already
        knows.

        Args:
          cursor: Opaque cursor from a previous response's `nextCursor`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return self._get_api_list(
            path_template("/v1/conversations/{conversation_id}/messages", conversation_id=conversation_id),
            page=SyncCursor[Message],
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
                    conversation_list_messages_params.ConversationListMessagesParams,
                ),
            ),
            model=Message,
        )

    def mark_as_read(
        self,
        conversation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationMarkAsReadResponse:
        """Reset the thread's `unreadCount` to zero.

        Marks the thread read in your own
        inbox only: it does not send a read receipt to the contact.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return self._post(
            path_template("/v1/conversations/{conversation_id}/read", conversation_id=conversation_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationMarkAsReadResponse,
        )


class AsyncConversationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConversationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConversationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConversationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return AsyncConversationsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        conversation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationRetrieveResponse:
        """
        Get conversation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return await self._get(
            path_template("/v1/conversations/{conversation_id}", conversation_id=conversation_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationRetrieveResponse,
        )

    def list(
        self,
        *,
        channel: Literal["sms", "sms_oneway", "whatsapp", "email", "telegram", "instagram", "messenger", "voice"]
        | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        search: str | Omit = omit,
        sender_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ConversationListResponse, AsyncCursor[ConversationListResponse]]:
        """List inbox threads, most recently active first.

        A conversation groups every
        message with one contact across channels, which is what you need to build an
        inbox: `GET /v1/messages` returns a flat log with no thread to hang it on.

        Use `senderId` to scope the list to a single number, and `channel` to keep only
        threads that have carried that channel.

        Args:
          channel: Keep only threads that have carried this channel.

          cursor: Opaque cursor from a previous response's `nextCursor`. Do not construct it.

          search: Search threads by identity: phone number (any format — `+1 (555) 123-4567` and
              `15551234567` both match), email address (full or local part), WhatsApp group
              subject, WhatsApp username, or BSUID. Matching is by whole word, with prefix
              matching on the last term, so `mar` finds `maria@example.com` and `+1555` finds
              `+15551234567`; a fragment from the middle or end of a number (`4567`) does not
              match.

              It does **not** search message bodies — only who the thread is with.

              Results come back ranked by relevance rather than by recency, so the usual "most
              recently active first" ordering does not apply while `q` is set. `senderId` and
              `channel` still narrow the results, and `cursor` paginates them as usual. An
              empty or whitespace-only `q` returns no items rather than the full list.

          sender_id: Keep only threads last handled by this sender.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/conversations",
            page=AsyncCursor[ConversationListResponse],
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
                        "search": search,
                        "sender_id": sender_id,
                    },
                    conversation_list_params.ConversationListParams,
                ),
            ),
            model=ConversationListResponse,
        )

    def list_messages(
        self,
        conversation_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Message, AsyncCursor[Message]]:
        """
        Messages in this thread, newest first, across every channel it has carried.
        Reply with `POST /v1/messages`, passing the conversation's `senderId` as the
        `Zavu-Sender` header so the answer leaves from the number the contact already
        knows.

        Args:
          cursor: Opaque cursor from a previous response's `nextCursor`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return self._get_api_list(
            path_template("/v1/conversations/{conversation_id}/messages", conversation_id=conversation_id),
            page=AsyncCursor[Message],
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
                    conversation_list_messages_params.ConversationListMessagesParams,
                ),
            ),
            model=Message,
        )

    async def mark_as_read(
        self,
        conversation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationMarkAsReadResponse:
        """Reset the thread's `unreadCount` to zero.

        Marks the thread read in your own
        inbox only: it does not send a read receipt to the contact.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return await self._post(
            path_template("/v1/conversations/{conversation_id}/read", conversation_id=conversation_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationMarkAsReadResponse,
        )


class ConversationsResourceWithRawResponse:
    def __init__(self, conversations: ConversationsResource) -> None:
        self._conversations = conversations

        self.retrieve = to_raw_response_wrapper(
            conversations.retrieve,
        )
        self.list = to_raw_response_wrapper(
            conversations.list,
        )
        self.list_messages = to_raw_response_wrapper(
            conversations.list_messages,
        )
        self.mark_as_read = to_raw_response_wrapper(
            conversations.mark_as_read,
        )


class AsyncConversationsResourceWithRawResponse:
    def __init__(self, conversations: AsyncConversationsResource) -> None:
        self._conversations = conversations

        self.retrieve = async_to_raw_response_wrapper(
            conversations.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            conversations.list,
        )
        self.list_messages = async_to_raw_response_wrapper(
            conversations.list_messages,
        )
        self.mark_as_read = async_to_raw_response_wrapper(
            conversations.mark_as_read,
        )


class ConversationsResourceWithStreamingResponse:
    def __init__(self, conversations: ConversationsResource) -> None:
        self._conversations = conversations

        self.retrieve = to_streamed_response_wrapper(
            conversations.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            conversations.list,
        )
        self.list_messages = to_streamed_response_wrapper(
            conversations.list_messages,
        )
        self.mark_as_read = to_streamed_response_wrapper(
            conversations.mark_as_read,
        )


class AsyncConversationsResourceWithStreamingResponse:
    def __init__(self, conversations: AsyncConversationsResource) -> None:
        self._conversations = conversations

        self.retrieve = async_to_streamed_response_wrapper(
            conversations.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            conversations.list,
        )
        self.list_messages = async_to_streamed_response_wrapper(
            conversations.list_messages,
        )
        self.mark_as_read = async_to_streamed_response_wrapper(
            conversations.mark_as_read,
        )
