# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import email_domain_create_params
from .._types import Body, Query, Headers, NoneType, NotGiven, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.email_domain_list_response import EmailDomainListResponse
from ..types.email_domain_create_response import EmailDomainCreateResponse
from ..types.email_domain_verify_response import EmailDomainVerifyResponse
from ..types.email_domain_retrieve_response import EmailDomainRetrieveResponse

__all__ = ["EmailDomainsResource", "AsyncEmailDomainsResource"]


class EmailDomainsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmailDomainsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return EmailDomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailDomainsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return EmailDomainsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        domain: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailDomainCreateResponse:
        """Add a domain to send email from.

        Returns the DNS records to publish (DKIM CNAMEs
        are required; SPF, DMARC, and MAIL FROM are recommended). Publish them at your
        DNS provider, then verify.

        Args:
          domain: Bare domain, e.g. example.com.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/email-domains",
            body=maybe_transform({"domain": domain}, email_domain_create_params.EmailDomainCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailDomainCreateResponse,
        )

    def retrieve(
        self,
        domain_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailDomainRetrieveResponse:
        """
        Fetch a domain with its DNS records and current status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        return self._get(
            path_template("/v1/email-domains/{domain_id}", domain_id=domain_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailDomainRetrieveResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailDomainListResponse:
        """List email domains"""
        return self._get(
            "/v1/email-domains",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailDomainListResponse,
        )

    def delete(
        self,
        domain_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove an email domain

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/email-domains/{domain_id}", domain_id=domain_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def verify(
        self,
        domain_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailDomainVerifyResponse:
        """
        Re-check the domain's published DNS records and refresh its status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        return self._post(
            path_template("/v1/email-domains/{domain_id}/verify", domain_id=domain_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailDomainVerifyResponse,
        )


class AsyncEmailDomainsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmailDomainsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zavudev/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmailDomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailDomainsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zavudev/sdk-python#with_streaming_response
        """
        return AsyncEmailDomainsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        domain: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailDomainCreateResponse:
        """Add a domain to send email from.

        Returns the DNS records to publish (DKIM CNAMEs
        are required; SPF, DMARC, and MAIL FROM are recommended). Publish them at your
        DNS provider, then verify.

        Args:
          domain: Bare domain, e.g. example.com.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/email-domains",
            body=await async_maybe_transform({"domain": domain}, email_domain_create_params.EmailDomainCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailDomainCreateResponse,
        )

    async def retrieve(
        self,
        domain_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailDomainRetrieveResponse:
        """
        Fetch a domain with its DNS records and current status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        return await self._get(
            path_template("/v1/email-domains/{domain_id}", domain_id=domain_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailDomainRetrieveResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailDomainListResponse:
        """List email domains"""
        return await self._get(
            "/v1/email-domains",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailDomainListResponse,
        )

    async def delete(
        self,
        domain_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove an email domain

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/email-domains/{domain_id}", domain_id=domain_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def verify(
        self,
        domain_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailDomainVerifyResponse:
        """
        Re-check the domain's published DNS records and refresh its status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        return await self._post(
            path_template("/v1/email-domains/{domain_id}/verify", domain_id=domain_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailDomainVerifyResponse,
        )


class EmailDomainsResourceWithRawResponse:
    def __init__(self, email_domains: EmailDomainsResource) -> None:
        self._email_domains = email_domains

        self.create = to_raw_response_wrapper(
            email_domains.create,
        )
        self.retrieve = to_raw_response_wrapper(
            email_domains.retrieve,
        )
        self.list = to_raw_response_wrapper(
            email_domains.list,
        )
        self.delete = to_raw_response_wrapper(
            email_domains.delete,
        )
        self.verify = to_raw_response_wrapper(
            email_domains.verify,
        )


class AsyncEmailDomainsResourceWithRawResponse:
    def __init__(self, email_domains: AsyncEmailDomainsResource) -> None:
        self._email_domains = email_domains

        self.create = async_to_raw_response_wrapper(
            email_domains.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            email_domains.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            email_domains.list,
        )
        self.delete = async_to_raw_response_wrapper(
            email_domains.delete,
        )
        self.verify = async_to_raw_response_wrapper(
            email_domains.verify,
        )


class EmailDomainsResourceWithStreamingResponse:
    def __init__(self, email_domains: EmailDomainsResource) -> None:
        self._email_domains = email_domains

        self.create = to_streamed_response_wrapper(
            email_domains.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            email_domains.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            email_domains.list,
        )
        self.delete = to_streamed_response_wrapper(
            email_domains.delete,
        )
        self.verify = to_streamed_response_wrapper(
            email_domains.verify,
        )


class AsyncEmailDomainsResourceWithStreamingResponse:
    def __init__(self, email_domains: AsyncEmailDomainsResource) -> None:
        self._email_domains = email_domains

        self.create = async_to_streamed_response_wrapper(
            email_domains.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            email_domains.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            email_domains.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            email_domains.delete,
        )
        self.verify = async_to_streamed_response_wrapper(
            email_domains.verify,
        )
