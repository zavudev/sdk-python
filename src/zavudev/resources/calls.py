# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal

import httpx

from ..types import call_list_params, call_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.call_list_response import CallListResponse
from ..types.call_create_response import CallCreateResponse
from ..types.call_hangup_response import CallHangupResponse
from ..types.call_retrieve_response import CallRetrieveResponse

__all__ = ["CallsResource", "AsyncCallsResource"]


class CallsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CallsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return CallsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CallsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return CallsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        to: str,
        greeting: str | Omit = omit,
        language: str | Omit = omit,
        max_duration_minutes: int | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        sender_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallCreateResponse:
        """
        Place an outbound voice call answered by the voice agent configured on the
        sender. Zavu dials the recipient and runs the conversation through its managed
        voice pipeline (speech recognition, the agent's LLM, and speech synthesis, with
        real-time interruption handling).

        **Requirements:**

        - The Voice Agents feature must be enabled for your team (otherwise `403`).
        - An account that has verified nothing may only call the phone numbers the
          project has verified (`403` with code `destination_not_verified`, and
          `details.verifiedNumbers` lists them), and at most 5 calls a day (`429` with
          code `daily_limit_exceeded`). A number is verified from the dashboard's
          Sandbox screen by sending the pre-filled WhatsApp message from that phone; the
          same verification covers SMS and calls. Verify your identity, add a payment
          method, settle a deposit or subscribe to call any destination. That raises the
          ceiling to 50 calls a day on Free; paid plans have no daily call ceiling. Full
          reference: https://docs.zavu.dev/concepts/sending-limits
        - The sender's agent must have `voice.enabled` set to `true`.
        - Not available with test-mode API keys.

        **Billing:** Voice calls are billed per minute of connected time plus telephony,
        deducted from your prepaid balance. A short-duration estimate is reserved when
        the call is placed; you are charged for the actual duration when the call ends.

        Args:
          to: Recipient phone number in E.164 format.

          greeting: Overrides the agent's configured greeting for this call only.

          language: Language the agent speaks on this call only, as a BCP-47 tag (`en`, `es`,
              `es-ES`, `pt-BR`), or `auto` to detect the caller's language and follow it.
              Overrides the agent's configured language for speech recognition, the agent's
              replies, and the synthesized voice. If the agent uses a custom voice you
              supplied, that voice is kept and only the language changes. When omitted, the
              agent's configured language is used.

          max_duration_minutes: Overrides the agent's maximum call duration for this call only.

          metadata: Arbitrary metadata to associate with the call. Returned on the call object and
              included in voice webhooks.

          sender_id: Sender profile that places the call. Uses the project's default sender if
              omitted. The sender's agent must have voice enabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/calls",
            body=maybe_transform(
                {
                    "to": to,
                    "greeting": greeting,
                    "language": language,
                    "max_duration_minutes": max_duration_minutes,
                    "metadata": metadata,
                    "sender_id": sender_id,
                },
                call_create_params.CallCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallCreateResponse,
        )

    def retrieve(
        self,
        call_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallRetrieveResponse:
        """
        Retrieve a single voice call, including its full transcript once the
        conversation has produced turns.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_id:
            raise ValueError(f"Expected a non-empty value for `call_id` but received {call_id!r}")
        return self._get(
            path_template("/v1/calls/{call_id}", call_id=call_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallRetrieveResponse,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        direction: Literal["inbound", "outbound"] | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["queued", "ringing", "in_progress", "completed", "failed", "busy", "no_answer", "canceled"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursor[CallListResponse]:
        """List voice calls for this project, most recent first.

        Transcripts are omitted
        from the list; fetch a single call to get its transcript.

        Args:
          direction: Whether the call was placed by Zavu (outbound) or received from a caller
              (inbound).

          status: Lifecycle status of a voice call.

              - `queued`: outbound call created, not yet dialing.
              - `ringing`: dialing (outbound) or received and ringing (inbound).
              - `in_progress`: answered, the agent is connected.
              - `completed`: ended after a conversation.
              - `failed`: could not be completed.
              - `busy`: the line was busy.
              - `no_answer`: rang but was not answered.
              - `canceled`: canceled before it was answered.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/calls",
            page=SyncCursor[CallListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "direction": direction,
                        "limit": limit,
                        "status": status,
                    },
                    call_list_params.CallListParams,
                ),
            ),
            model=CallListResponse,
        )

    def hangup(
        self,
        call_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallHangupResponse:
        """End an active voice call.

        The call must still be ringing or in progress. Not
        available with test-mode API keys.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_id:
            raise ValueError(f"Expected a non-empty value for `call_id` but received {call_id!r}")
        return self._post(
            path_template("/v1/calls/{call_id}/hangup", call_id=call_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallHangupResponse,
        )


class AsyncCallsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCallsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCallsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCallsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return AsyncCallsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        to: str,
        greeting: str | Omit = omit,
        language: str | Omit = omit,
        max_duration_minutes: int | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        sender_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallCreateResponse:
        """
        Place an outbound voice call answered by the voice agent configured on the
        sender. Zavu dials the recipient and runs the conversation through its managed
        voice pipeline (speech recognition, the agent's LLM, and speech synthesis, with
        real-time interruption handling).

        **Requirements:**

        - The Voice Agents feature must be enabled for your team (otherwise `403`).
        - An account that has verified nothing may only call the phone numbers the
          project has verified (`403` with code `destination_not_verified`, and
          `details.verifiedNumbers` lists them), and at most 5 calls a day (`429` with
          code `daily_limit_exceeded`). A number is verified from the dashboard's
          Sandbox screen by sending the pre-filled WhatsApp message from that phone; the
          same verification covers SMS and calls. Verify your identity, add a payment
          method, settle a deposit or subscribe to call any destination. That raises the
          ceiling to 50 calls a day on Free; paid plans have no daily call ceiling. Full
          reference: https://docs.zavu.dev/concepts/sending-limits
        - The sender's agent must have `voice.enabled` set to `true`.
        - Not available with test-mode API keys.

        **Billing:** Voice calls are billed per minute of connected time plus telephony,
        deducted from your prepaid balance. A short-duration estimate is reserved when
        the call is placed; you are charged for the actual duration when the call ends.

        Args:
          to: Recipient phone number in E.164 format.

          greeting: Overrides the agent's configured greeting for this call only.

          language: Language the agent speaks on this call only, as a BCP-47 tag (`en`, `es`,
              `es-ES`, `pt-BR`), or `auto` to detect the caller's language and follow it.
              Overrides the agent's configured language for speech recognition, the agent's
              replies, and the synthesized voice. If the agent uses a custom voice you
              supplied, that voice is kept and only the language changes. When omitted, the
              agent's configured language is used.

          max_duration_minutes: Overrides the agent's maximum call duration for this call only.

          metadata: Arbitrary metadata to associate with the call. Returned on the call object and
              included in voice webhooks.

          sender_id: Sender profile that places the call. Uses the project's default sender if
              omitted. The sender's agent must have voice enabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/calls",
            body=await async_maybe_transform(
                {
                    "to": to,
                    "greeting": greeting,
                    "language": language,
                    "max_duration_minutes": max_duration_minutes,
                    "metadata": metadata,
                    "sender_id": sender_id,
                },
                call_create_params.CallCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallCreateResponse,
        )

    async def retrieve(
        self,
        call_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallRetrieveResponse:
        """
        Retrieve a single voice call, including its full transcript once the
        conversation has produced turns.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_id:
            raise ValueError(f"Expected a non-empty value for `call_id` but received {call_id!r}")
        return await self._get(
            path_template("/v1/calls/{call_id}", call_id=call_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallRetrieveResponse,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        direction: Literal["inbound", "outbound"] | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["queued", "ringing", "in_progress", "completed", "failed", "busy", "no_answer", "canceled"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CallListResponse, AsyncCursor[CallListResponse]]:
        """List voice calls for this project, most recent first.

        Transcripts are omitted
        from the list; fetch a single call to get its transcript.

        Args:
          direction: Whether the call was placed by Zavu (outbound) or received from a caller
              (inbound).

          status: Lifecycle status of a voice call.

              - `queued`: outbound call created, not yet dialing.
              - `ringing`: dialing (outbound) or received and ringing (inbound).
              - `in_progress`: answered, the agent is connected.
              - `completed`: ended after a conversation.
              - `failed`: could not be completed.
              - `busy`: the line was busy.
              - `no_answer`: rang but was not answered.
              - `canceled`: canceled before it was answered.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/calls",
            page=AsyncCursor[CallListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "direction": direction,
                        "limit": limit,
                        "status": status,
                    },
                    call_list_params.CallListParams,
                ),
            ),
            model=CallListResponse,
        )

    async def hangup(
        self,
        call_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallHangupResponse:
        """End an active voice call.

        The call must still be ringing or in progress. Not
        available with test-mode API keys.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_id:
            raise ValueError(f"Expected a non-empty value for `call_id` but received {call_id!r}")
        return await self._post(
            path_template("/v1/calls/{call_id}/hangup", call_id=call_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallHangupResponse,
        )


class CallsResourceWithRawResponse:
    def __init__(self, calls: CallsResource) -> None:
        self._calls = calls

        self.create = to_raw_response_wrapper(
            calls.create,
        )
        self.retrieve = to_raw_response_wrapper(
            calls.retrieve,
        )
        self.list = to_raw_response_wrapper(
            calls.list,
        )
        self.hangup = to_raw_response_wrapper(
            calls.hangup,
        )


class AsyncCallsResourceWithRawResponse:
    def __init__(self, calls: AsyncCallsResource) -> None:
        self._calls = calls

        self.create = async_to_raw_response_wrapper(
            calls.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            calls.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            calls.list,
        )
        self.hangup = async_to_raw_response_wrapper(
            calls.hangup,
        )


class CallsResourceWithStreamingResponse:
    def __init__(self, calls: CallsResource) -> None:
        self._calls = calls

        self.create = to_streamed_response_wrapper(
            calls.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            calls.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            calls.list,
        )
        self.hangup = to_streamed_response_wrapper(
            calls.hangup,
        )


class AsyncCallsResourceWithStreamingResponse:
    def __init__(self, calls: AsyncCallsResource) -> None:
        self._calls = calls

        self.create = async_to_streamed_response_wrapper(
            calls.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            calls.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            calls.list,
        )
        self.hangup = async_to_streamed_response_wrapper(
            calls.hangup,
        )
