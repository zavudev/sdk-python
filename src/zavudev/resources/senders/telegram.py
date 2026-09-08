# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NoneType, NotGiven, not_given
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
from ...types.senders import telegram_connect_params
from ...types.senders.telegram_connect_response import TelegramConnectResponse

__all__ = ["TelegramResource", "AsyncTelegramResource"]


class TelegramResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TelegramResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return TelegramResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TelegramResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return TelegramResourceWithStreamingResponse(self)

    def connect(
        self,
        sender_id: str,
        *,
        bot_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TelegramConnectResponse:
        """Connect a Telegram bot to a sender.

        Provide the bot token from @BotFather; Zavu
        validates it, registers the webhook, and routes the sender's Telegram messages
        through it.

        Args:
          bot_token: Bot token from @BotFather.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return self._post(
            path_template("/v1/senders/{sender_id}/telegram", sender_id=sender_id),
            body=maybe_transform({"bot_token": bot_token}, telegram_connect_params.TelegramConnectParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelegramConnectResponse,
        )

    def disconnect(
        self,
        sender_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Disconnect Telegram from a sender and remove the webhook.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/senders/{sender_id}/telegram", sender_id=sender_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncTelegramResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTelegramResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTelegramResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTelegramResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return AsyncTelegramResourceWithStreamingResponse(self)

    async def connect(
        self,
        sender_id: str,
        *,
        bot_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TelegramConnectResponse:
        """Connect a Telegram bot to a sender.

        Provide the bot token from @BotFather; Zavu
        validates it, registers the webhook, and routes the sender's Telegram messages
        through it.

        Args:
          bot_token: Bot token from @BotFather.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return await self._post(
            path_template("/v1/senders/{sender_id}/telegram", sender_id=sender_id),
            body=await async_maybe_transform({"bot_token": bot_token}, telegram_connect_params.TelegramConnectParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelegramConnectResponse,
        )

    async def disconnect(
        self,
        sender_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Disconnect Telegram from a sender and remove the webhook.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/senders/{sender_id}/telegram", sender_id=sender_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class TelegramResourceWithRawResponse:
    def __init__(self, telegram: TelegramResource) -> None:
        self._telegram = telegram

        self.connect = to_raw_response_wrapper(
            telegram.connect,
        )
        self.disconnect = to_raw_response_wrapper(
            telegram.disconnect,
        )


class AsyncTelegramResourceWithRawResponse:
    def __init__(self, telegram: AsyncTelegramResource) -> None:
        self._telegram = telegram

        self.connect = async_to_raw_response_wrapper(
            telegram.connect,
        )
        self.disconnect = async_to_raw_response_wrapper(
            telegram.disconnect,
        )


class TelegramResourceWithStreamingResponse:
    def __init__(self, telegram: TelegramResource) -> None:
        self._telegram = telegram

        self.connect = to_streamed_response_wrapper(
            telegram.connect,
        )
        self.disconnect = to_streamed_response_wrapper(
            telegram.disconnect,
        )


class AsyncTelegramResourceWithStreamingResponse:
    def __init__(self, telegram: AsyncTelegramResource) -> None:
        self._telegram = telegram

        self.connect = async_to_streamed_response_wrapper(
            telegram.connect,
        )
        self.disconnect = async_to_streamed_response_wrapper(
            telegram.disconnect,
        )
