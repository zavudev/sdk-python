# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.functions import trigger_create_params, trigger_update_params
from ...types.functions.trigger_list_response import TriggerListResponse
from ...types.functions.trigger_create_response import TriggerCreateResponse
from ...types.functions.trigger_update_response import TriggerUpdateResponse

__all__ = ["TriggersResource", "AsyncTriggersResource"]


class TriggersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TriggersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return TriggersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TriggersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return TriggersResourceWithStreamingResponse(self)

    def create(
        self,
        function_id: str,
        *,
        event_types: SequenceNotStr[str],
        sender_ids: SequenceNotStr[Optional[str]],
        cron: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggerCreateResponse:
        """
        Subscribe a function to one or more event types, optionally scoped to specific
        senders. Provide eventTypes and senderIds (use null in senderIds for all
        senders); a trigger is created for each event type and sender combination.

        The special event type `cron` runs the function on a schedule instead of a
        messaging event: include a `cron` field with a 5-field UTC cron expression
        (minimum granularity one minute). A cron trigger ignores the sender axis, and a
        function may hold several cron triggers with different expressions. The function
        receives an event with `type: "cron"` and `data.cron`.

        Args:
          event_types: Event types to subscribe to.

          sender_ids: Senders to scope the triggers to. Use null for all senders.

          cron: Required when eventTypes includes `cron`: a 5-field cron expression (minute hour
              day-of-month month day-of-week), evaluated in UTC.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return self._post(
            path_template("/v1/functions/{function_id}/triggers", function_id=function_id),
            body=maybe_transform(
                {
                    "event_types": event_types,
                    "sender_ids": sender_ids,
                    "cron": cron,
                },
                trigger_create_params.TriggerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerCreateResponse,
        )

    def update(
        self,
        trigger_id: str,
        *,
        active: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggerUpdateResponse:
        """
        Enable or disable a trigger

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not trigger_id:
            raise ValueError(f"Expected a non-empty value for `trigger_id` but received {trigger_id!r}")
        return self._patch(
            path_template("/v1/functions/triggers/{trigger_id}", trigger_id=trigger_id),
            body=maybe_transform({"active": active}, trigger_update_params.TriggerUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerUpdateResponse,
        )

    def list(
        self,
        function_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggerListResponse:
        """
        List function triggers

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return self._get(
            path_template("/v1/functions/{function_id}/triggers", function_id=function_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerListResponse,
        )

    def delete(
        self,
        trigger_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a trigger

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not trigger_id:
            raise ValueError(f"Expected a non-empty value for `trigger_id` but received {trigger_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/functions/triggers/{trigger_id}", trigger_id=trigger_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncTriggersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTriggersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTriggersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTriggersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return AsyncTriggersResourceWithStreamingResponse(self)

    async def create(
        self,
        function_id: str,
        *,
        event_types: SequenceNotStr[str],
        sender_ids: SequenceNotStr[Optional[str]],
        cron: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggerCreateResponse:
        """
        Subscribe a function to one or more event types, optionally scoped to specific
        senders. Provide eventTypes and senderIds (use null in senderIds for all
        senders); a trigger is created for each event type and sender combination.

        The special event type `cron` runs the function on a schedule instead of a
        messaging event: include a `cron` field with a 5-field UTC cron expression
        (minimum granularity one minute). A cron trigger ignores the sender axis, and a
        function may hold several cron triggers with different expressions. The function
        receives an event with `type: "cron"` and `data.cron`.

        Args:
          event_types: Event types to subscribe to.

          sender_ids: Senders to scope the triggers to. Use null for all senders.

          cron: Required when eventTypes includes `cron`: a 5-field cron expression (minute hour
              day-of-month month day-of-week), evaluated in UTC.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return await self._post(
            path_template("/v1/functions/{function_id}/triggers", function_id=function_id),
            body=await async_maybe_transform(
                {
                    "event_types": event_types,
                    "sender_ids": sender_ids,
                    "cron": cron,
                },
                trigger_create_params.TriggerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerCreateResponse,
        )

    async def update(
        self,
        trigger_id: str,
        *,
        active: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggerUpdateResponse:
        """
        Enable or disable a trigger

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not trigger_id:
            raise ValueError(f"Expected a non-empty value for `trigger_id` but received {trigger_id!r}")
        return await self._patch(
            path_template("/v1/functions/triggers/{trigger_id}", trigger_id=trigger_id),
            body=await async_maybe_transform({"active": active}, trigger_update_params.TriggerUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerUpdateResponse,
        )

    async def list(
        self,
        function_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggerListResponse:
        """
        List function triggers

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return await self._get(
            path_template("/v1/functions/{function_id}/triggers", function_id=function_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerListResponse,
        )

    async def delete(
        self,
        trigger_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a trigger

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not trigger_id:
            raise ValueError(f"Expected a non-empty value for `trigger_id` but received {trigger_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/functions/triggers/{trigger_id}", trigger_id=trigger_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class TriggersResourceWithRawResponse:
    def __init__(self, triggers: TriggersResource) -> None:
        self._triggers = triggers

        self.create = to_raw_response_wrapper(
            triggers.create,
        )
        self.update = to_raw_response_wrapper(
            triggers.update,
        )
        self.list = to_raw_response_wrapper(
            triggers.list,
        )
        self.delete = to_raw_response_wrapper(
            triggers.delete,
        )


class AsyncTriggersResourceWithRawResponse:
    def __init__(self, triggers: AsyncTriggersResource) -> None:
        self._triggers = triggers

        self.create = async_to_raw_response_wrapper(
            triggers.create,
        )
        self.update = async_to_raw_response_wrapper(
            triggers.update,
        )
        self.list = async_to_raw_response_wrapper(
            triggers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            triggers.delete,
        )


class TriggersResourceWithStreamingResponse:
    def __init__(self, triggers: TriggersResource) -> None:
        self._triggers = triggers

        self.create = to_streamed_response_wrapper(
            triggers.create,
        )
        self.update = to_streamed_response_wrapper(
            triggers.update,
        )
        self.list = to_streamed_response_wrapper(
            triggers.list,
        )
        self.delete = to_streamed_response_wrapper(
            triggers.delete,
        )


class AsyncTriggersResourceWithStreamingResponse:
    def __init__(self, triggers: AsyncTriggersResource) -> None:
        self._triggers = triggers

        self.create = async_to_streamed_response_wrapper(
            triggers.create,
        )
        self.update = async_to_streamed_response_wrapper(
            triggers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            triggers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            triggers.delete,
        )
