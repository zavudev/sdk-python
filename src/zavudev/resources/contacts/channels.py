# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ...types.contacts import channel_add_params, channel_update_params
from ...types.contacts.channel_add_response import ChannelAddResponse
from ...types.contacts.channel_update_response import ChannelUpdateResponse
from ...types.contacts.channel_set_primary_response import ChannelSetPrimaryResponse

__all__ = ["ChannelsResource", "AsyncChannelsResource"]


class ChannelsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChannelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return ChannelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChannelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return ChannelsResourceWithStreamingResponse(self)

    def update(
        self,
        channel_id: str,
        *,
        contact_id: str,
        label: Optional[str] | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        verified: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelUpdateResponse:
        """
        Update a contact's channel properties.

        Args:
          label: Optional label for the channel. Set to null to clear.

          verified: Whether the channel is verified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return self._patch(
            path_template(
                "/v1/contacts/{contact_id}/channels/{channel_id}", contact_id=contact_id, channel_id=channel_id
            ),
            body=maybe_transform(
                {
                    "label": label,
                    "metadata": metadata,
                    "verified": verified,
                },
                channel_update_params.ChannelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelUpdateResponse,
        )

    def add(
        self,
        contact_id: str,
        *,
        channel: Literal["sms", "whatsapp", "email", "telegram", "voice"],
        identifier: str,
        country_code: str | Omit = omit,
        is_primary: bool | Omit = omit,
        label: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelAddResponse:
        """
        Add a new communication channel to an existing contact.

        Args:
          channel: Channel type.

          identifier: Channel identifier (phone number in E.164 format or email address).

          country_code: ISO country code for phone numbers.

          is_primary: Whether this should be the primary channel for its type.

          label: Optional label for the channel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        return self._post(
            path_template("/v1/contacts/{contact_id}/channels", contact_id=contact_id),
            body=maybe_transform(
                {
                    "channel": channel,
                    "identifier": identifier,
                    "country_code": country_code,
                    "is_primary": is_primary,
                    "label": label,
                },
                channel_add_params.ChannelAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelAddResponse,
        )

    def remove(
        self,
        channel_id: str,
        *,
        contact_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Remove a communication channel from a contact.

        Cannot remove the last channel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/v1/contacts/{contact_id}/channels/{channel_id}", contact_id=contact_id, channel_id=channel_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def set_primary(
        self,
        channel_id: str,
        *,
        contact_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelSetPrimaryResponse:
        """
        Set a channel as the primary channel for its type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return self._post(
            path_template(
                "/v1/contacts/{contact_id}/channels/{channel_id}/primary", contact_id=contact_id, channel_id=channel_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelSetPrimaryResponse,
        )


class AsyncChannelsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChannelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChannelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChannelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return AsyncChannelsResourceWithStreamingResponse(self)

    async def update(
        self,
        channel_id: str,
        *,
        contact_id: str,
        label: Optional[str] | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        verified: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelUpdateResponse:
        """
        Update a contact's channel properties.

        Args:
          label: Optional label for the channel. Set to null to clear.

          verified: Whether the channel is verified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return await self._patch(
            path_template(
                "/v1/contacts/{contact_id}/channels/{channel_id}", contact_id=contact_id, channel_id=channel_id
            ),
            body=await async_maybe_transform(
                {
                    "label": label,
                    "metadata": metadata,
                    "verified": verified,
                },
                channel_update_params.ChannelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelUpdateResponse,
        )

    async def add(
        self,
        contact_id: str,
        *,
        channel: Literal["sms", "whatsapp", "email", "telegram", "voice"],
        identifier: str,
        country_code: str | Omit = omit,
        is_primary: bool | Omit = omit,
        label: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelAddResponse:
        """
        Add a new communication channel to an existing contact.

        Args:
          channel: Channel type.

          identifier: Channel identifier (phone number in E.164 format or email address).

          country_code: ISO country code for phone numbers.

          is_primary: Whether this should be the primary channel for its type.

          label: Optional label for the channel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        return await self._post(
            path_template("/v1/contacts/{contact_id}/channels", contact_id=contact_id),
            body=await async_maybe_transform(
                {
                    "channel": channel,
                    "identifier": identifier,
                    "country_code": country_code,
                    "is_primary": is_primary,
                    "label": label,
                },
                channel_add_params.ChannelAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelAddResponse,
        )

    async def remove(
        self,
        channel_id: str,
        *,
        contact_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Remove a communication channel from a contact.

        Cannot remove the last channel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/v1/contacts/{contact_id}/channels/{channel_id}", contact_id=contact_id, channel_id=channel_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def set_primary(
        self,
        channel_id: str,
        *,
        contact_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelSetPrimaryResponse:
        """
        Set a channel as the primary channel for its type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return await self._post(
            path_template(
                "/v1/contacts/{contact_id}/channels/{channel_id}/primary", contact_id=contact_id, channel_id=channel_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelSetPrimaryResponse,
        )


class ChannelsResourceWithRawResponse:
    def __init__(self, channels: ChannelsResource) -> None:
        self._channels = channels

        self.update = to_raw_response_wrapper(
            channels.update,
        )
        self.add = to_raw_response_wrapper(
            channels.add,
        )
        self.remove = to_raw_response_wrapper(
            channels.remove,
        )
        self.set_primary = to_raw_response_wrapper(
            channels.set_primary,
        )


class AsyncChannelsResourceWithRawResponse:
    def __init__(self, channels: AsyncChannelsResource) -> None:
        self._channels = channels

        self.update = async_to_raw_response_wrapper(
            channels.update,
        )
        self.add = async_to_raw_response_wrapper(
            channels.add,
        )
        self.remove = async_to_raw_response_wrapper(
            channels.remove,
        )
        self.set_primary = async_to_raw_response_wrapper(
            channels.set_primary,
        )


class ChannelsResourceWithStreamingResponse:
    def __init__(self, channels: ChannelsResource) -> None:
        self._channels = channels

        self.update = to_streamed_response_wrapper(
            channels.update,
        )
        self.add = to_streamed_response_wrapper(
            channels.add,
        )
        self.remove = to_streamed_response_wrapper(
            channels.remove,
        )
        self.set_primary = to_streamed_response_wrapper(
            channels.set_primary,
        )


class AsyncChannelsResourceWithStreamingResponse:
    def __init__(self, channels: AsyncChannelsResource) -> None:
        self._channels = channels

        self.update = async_to_streamed_response_wrapper(
            channels.update,
        )
        self.add = async_to_streamed_response_wrapper(
            channels.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            channels.remove,
        )
        self.set_primary = async_to_streamed_response_wrapper(
            channels.set_primary,
        )
