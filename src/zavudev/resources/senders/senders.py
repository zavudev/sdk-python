# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ...types import (
    WhatsappBusinessProfileVertical,
    sender_list_params,
    sender_create_params,
    sender_update_params,
    sender_update_profile_params,
    sender_upload_profile_picture_params,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .agent.agent import (
    AgentResource,
    AsyncAgentResource,
    AgentResourceWithRawResponse,
    AsyncAgentResourceWithRawResponse,
    AgentResourceWithStreamingResponse,
    AsyncAgentResourceWithStreamingResponse,
)
from ...pagination import SyncCursor, AsyncCursor
from ..._base_client import AsyncPaginator, make_request_options
from ...types.sender import Sender
from ...types.webhook_event import WebhookEvent
from ...types.webhook_secret_response import WebhookSecretResponse
from ...types.sender_update_profile_response import SenderUpdateProfileResponse
from ...types.whatsapp_business_profile_response import WhatsappBusinessProfileResponse
from ...types.whatsapp_business_profile_vertical import WhatsappBusinessProfileVertical
from ...types.sender_upload_profile_picture_response import SenderUploadProfilePictureResponse

__all__ = ["SendersResource", "AsyncSendersResource"]


class SendersResource(SyncAPIResource):
    @cached_property
    def agent(self) -> AgentResource:
        return AgentResource(self._client)

    @cached_property
    def with_raw_response(self) -> SendersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return SendersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SendersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return SendersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        phone_number: str,
        set_as_default: bool | Omit = omit,
        webhook_events: List[WebhookEvent] | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Sender:
        """
        Create sender

        Args:
          webhook_events: Events to subscribe to.

          webhook_url: HTTPS URL for webhook events.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/senders",
            body=maybe_transform(
                {
                    "name": name,
                    "phone_number": phone_number,
                    "set_as_default": set_as_default,
                    "webhook_events": webhook_events,
                    "webhook_url": webhook_url,
                },
                sender_create_params.SenderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Sender,
        )

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
    ) -> Sender:
        """
        Get sender

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return self._get(
            f"/v1/senders/{sender_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Sender,
        )

    def update(
        self,
        sender_id: str,
        *,
        name: str | Omit = omit,
        set_as_default: bool | Omit = omit,
        webhook_active: bool | Omit = omit,
        webhook_events: List[WebhookEvent] | Omit = omit,
        webhook_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Sender:
        """
        Update sender

        Args:
          webhook_active: Whether the webhook is active.

          webhook_events: Events to subscribe to.

          webhook_url: HTTPS URL for webhook events. Set to null to remove webhook.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return self._patch(
            f"/v1/senders/{sender_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "set_as_default": set_as_default,
                    "webhook_active": webhook_active,
                    "webhook_events": webhook_events,
                    "webhook_url": webhook_url,
                },
                sender_update_params.SenderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Sender,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursor[Sender]:
        """
        List senders

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/senders",
            page=SyncCursor[Sender],
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
                    sender_list_params.SenderListParams,
                ),
            ),
            model=Sender,
        )

    def delete(
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
        Delete sender

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
            f"/v1/senders/{sender_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_profile(
        self,
        sender_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WhatsappBusinessProfileResponse:
        """Get the WhatsApp Business profile for a sender.

        The sender must have a WhatsApp
        Business Account connected.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return self._get(
            f"/v1/senders/{sender_id}/profile",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WhatsappBusinessProfileResponse,
        )

    def regenerate_webhook_secret(
        self,
        sender_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookSecretResponse:
        """Regenerate the webhook secret for a sender.

        The old secret will be invalidated
        immediately.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return self._post(
            f"/v1/senders/{sender_id}/webhook/secret",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookSecretResponse,
        )

    def update_profile(
        self,
        sender_id: str,
        *,
        about: str | Omit = omit,
        address: str | Omit = omit,
        description: str | Omit = omit,
        email: str | Omit = omit,
        vertical: WhatsappBusinessProfileVertical | Omit = omit,
        websites: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SenderUpdateProfileResponse:
        """Update the WhatsApp Business profile for a sender.

        The sender must have a
        WhatsApp Business Account connected.

        Args:
          about: Short description of the business (max 139 characters).

          address: Physical address of the business (max 256 characters).

          description: Extended description of the business (max 512 characters).

          email: Business email address.

          vertical: Business category for WhatsApp Business profile.

          websites: Business website URLs (maximum 2).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return self._patch(
            f"/v1/senders/{sender_id}/profile",
            body=maybe_transform(
                {
                    "about": about,
                    "address": address,
                    "description": description,
                    "email": email,
                    "vertical": vertical,
                    "websites": websites,
                },
                sender_update_profile_params.SenderUpdateProfileParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SenderUpdateProfileResponse,
        )

    def upload_profile_picture(
        self,
        sender_id: str,
        *,
        image_url: str,
        mime_type: Literal["image/jpeg", "image/png"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SenderUploadProfilePictureResponse:
        """Upload a new profile picture for the WhatsApp Business profile.

        The image will
        be uploaded to Meta and set as the profile picture.

        Args:
          image_url: URL of the image to upload.

          mime_type: MIME type of the image.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return self._post(
            f"/v1/senders/{sender_id}/profile/picture",
            body=maybe_transform(
                {
                    "image_url": image_url,
                    "mime_type": mime_type,
                },
                sender_upload_profile_picture_params.SenderUploadProfilePictureParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SenderUploadProfilePictureResponse,
        )


class AsyncSendersResource(AsyncAPIResource):
    @cached_property
    def agent(self) -> AsyncAgentResource:
        return AsyncAgentResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSendersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSendersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSendersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return AsyncSendersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        phone_number: str,
        set_as_default: bool | Omit = omit,
        webhook_events: List[WebhookEvent] | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Sender:
        """
        Create sender

        Args:
          webhook_events: Events to subscribe to.

          webhook_url: HTTPS URL for webhook events.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/senders",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "phone_number": phone_number,
                    "set_as_default": set_as_default,
                    "webhook_events": webhook_events,
                    "webhook_url": webhook_url,
                },
                sender_create_params.SenderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Sender,
        )

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
    ) -> Sender:
        """
        Get sender

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return await self._get(
            f"/v1/senders/{sender_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Sender,
        )

    async def update(
        self,
        sender_id: str,
        *,
        name: str | Omit = omit,
        set_as_default: bool | Omit = omit,
        webhook_active: bool | Omit = omit,
        webhook_events: List[WebhookEvent] | Omit = omit,
        webhook_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Sender:
        """
        Update sender

        Args:
          webhook_active: Whether the webhook is active.

          webhook_events: Events to subscribe to.

          webhook_url: HTTPS URL for webhook events. Set to null to remove webhook.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return await self._patch(
            f"/v1/senders/{sender_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "set_as_default": set_as_default,
                    "webhook_active": webhook_active,
                    "webhook_events": webhook_events,
                    "webhook_url": webhook_url,
                },
                sender_update_params.SenderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Sender,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Sender, AsyncCursor[Sender]]:
        """
        List senders

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/senders",
            page=AsyncCursor[Sender],
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
                    sender_list_params.SenderListParams,
                ),
            ),
            model=Sender,
        )

    async def delete(
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
        Delete sender

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
            f"/v1/senders/{sender_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_profile(
        self,
        sender_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WhatsappBusinessProfileResponse:
        """Get the WhatsApp Business profile for a sender.

        The sender must have a WhatsApp
        Business Account connected.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return await self._get(
            f"/v1/senders/{sender_id}/profile",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WhatsappBusinessProfileResponse,
        )

    async def regenerate_webhook_secret(
        self,
        sender_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookSecretResponse:
        """Regenerate the webhook secret for a sender.

        The old secret will be invalidated
        immediately.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return await self._post(
            f"/v1/senders/{sender_id}/webhook/secret",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookSecretResponse,
        )

    async def update_profile(
        self,
        sender_id: str,
        *,
        about: str | Omit = omit,
        address: str | Omit = omit,
        description: str | Omit = omit,
        email: str | Omit = omit,
        vertical: WhatsappBusinessProfileVertical | Omit = omit,
        websites: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SenderUpdateProfileResponse:
        """Update the WhatsApp Business profile for a sender.

        The sender must have a
        WhatsApp Business Account connected.

        Args:
          about: Short description of the business (max 139 characters).

          address: Physical address of the business (max 256 characters).

          description: Extended description of the business (max 512 characters).

          email: Business email address.

          vertical: Business category for WhatsApp Business profile.

          websites: Business website URLs (maximum 2).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return await self._patch(
            f"/v1/senders/{sender_id}/profile",
            body=await async_maybe_transform(
                {
                    "about": about,
                    "address": address,
                    "description": description,
                    "email": email,
                    "vertical": vertical,
                    "websites": websites,
                },
                sender_update_profile_params.SenderUpdateProfileParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SenderUpdateProfileResponse,
        )

    async def upload_profile_picture(
        self,
        sender_id: str,
        *,
        image_url: str,
        mime_type: Literal["image/jpeg", "image/png"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SenderUploadProfilePictureResponse:
        """Upload a new profile picture for the WhatsApp Business profile.

        The image will
        be uploaded to Meta and set as the profile picture.

        Args:
          image_url: URL of the image to upload.

          mime_type: MIME type of the image.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return await self._post(
            f"/v1/senders/{sender_id}/profile/picture",
            body=await async_maybe_transform(
                {
                    "image_url": image_url,
                    "mime_type": mime_type,
                },
                sender_upload_profile_picture_params.SenderUploadProfilePictureParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SenderUploadProfilePictureResponse,
        )


class SendersResourceWithRawResponse:
    def __init__(self, senders: SendersResource) -> None:
        self._senders = senders

        self.create = to_raw_response_wrapper(
            senders.create,
        )
        self.retrieve = to_raw_response_wrapper(
            senders.retrieve,
        )
        self.update = to_raw_response_wrapper(
            senders.update,
        )
        self.list = to_raw_response_wrapper(
            senders.list,
        )
        self.delete = to_raw_response_wrapper(
            senders.delete,
        )
        self.get_profile = to_raw_response_wrapper(
            senders.get_profile,
        )
        self.regenerate_webhook_secret = to_raw_response_wrapper(
            senders.regenerate_webhook_secret,
        )
        self.update_profile = to_raw_response_wrapper(
            senders.update_profile,
        )
        self.upload_profile_picture = to_raw_response_wrapper(
            senders.upload_profile_picture,
        )

    @cached_property
    def agent(self) -> AgentResourceWithRawResponse:
        return AgentResourceWithRawResponse(self._senders.agent)


class AsyncSendersResourceWithRawResponse:
    def __init__(self, senders: AsyncSendersResource) -> None:
        self._senders = senders

        self.create = async_to_raw_response_wrapper(
            senders.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            senders.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            senders.update,
        )
        self.list = async_to_raw_response_wrapper(
            senders.list,
        )
        self.delete = async_to_raw_response_wrapper(
            senders.delete,
        )
        self.get_profile = async_to_raw_response_wrapper(
            senders.get_profile,
        )
        self.regenerate_webhook_secret = async_to_raw_response_wrapper(
            senders.regenerate_webhook_secret,
        )
        self.update_profile = async_to_raw_response_wrapper(
            senders.update_profile,
        )
        self.upload_profile_picture = async_to_raw_response_wrapper(
            senders.upload_profile_picture,
        )

    @cached_property
    def agent(self) -> AsyncAgentResourceWithRawResponse:
        return AsyncAgentResourceWithRawResponse(self._senders.agent)


class SendersResourceWithStreamingResponse:
    def __init__(self, senders: SendersResource) -> None:
        self._senders = senders

        self.create = to_streamed_response_wrapper(
            senders.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            senders.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            senders.update,
        )
        self.list = to_streamed_response_wrapper(
            senders.list,
        )
        self.delete = to_streamed_response_wrapper(
            senders.delete,
        )
        self.get_profile = to_streamed_response_wrapper(
            senders.get_profile,
        )
        self.regenerate_webhook_secret = to_streamed_response_wrapper(
            senders.regenerate_webhook_secret,
        )
        self.update_profile = to_streamed_response_wrapper(
            senders.update_profile,
        )
        self.upload_profile_picture = to_streamed_response_wrapper(
            senders.upload_profile_picture,
        )

    @cached_property
    def agent(self) -> AgentResourceWithStreamingResponse:
        return AgentResourceWithStreamingResponse(self._senders.agent)


class AsyncSendersResourceWithStreamingResponse:
    def __init__(self, senders: AsyncSendersResource) -> None:
        self._senders = senders

        self.create = async_to_streamed_response_wrapper(
            senders.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            senders.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            senders.update,
        )
        self.list = async_to_streamed_response_wrapper(
            senders.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            senders.delete,
        )
        self.get_profile = async_to_streamed_response_wrapper(
            senders.get_profile,
        )
        self.regenerate_webhook_secret = async_to_streamed_response_wrapper(
            senders.regenerate_webhook_secret,
        )
        self.update_profile = async_to_streamed_response_wrapper(
            senders.update_profile,
        )
        self.upload_profile_picture = async_to_streamed_response_wrapper(
            senders.upload_profile_picture,
        )

    @cached_property
    def agent(self) -> AsyncAgentResourceWithStreamingResponse:
        return AsyncAgentResourceWithStreamingResponse(self._senders.agent)
