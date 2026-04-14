# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import ZavudevError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        plan,
        urls,
        usage,
        balance,
        exports,
        senders,
        contacts,
        messages,
        addresses,
        templates,
        broadcasts,
        introspect,
        invitations,
        number_10dlc,
        sub_accounts,
        phone_numbers,
        regulatory_documents,
    )
    from .resources.plan import PlanResource, AsyncPlanResource
    from .resources.urls import URLsResource, AsyncURLsResource
    from .resources.usage import UsageResource, AsyncUsageResource
    from .resources.balance import BalanceResource, AsyncBalanceResource
    from .resources.exports import ExportsResource, AsyncExportsResource
    from .resources.messages import MessagesResource, AsyncMessagesResource
    from .resources.addresses import AddressesResource, AsyncAddressesResource
    from .resources.templates import TemplatesResource, AsyncTemplatesResource
    from .resources.introspect import IntrospectResource, AsyncIntrospectResource
    from .resources.invitations import InvitationsResource, AsyncInvitationsResource
    from .resources.phone_numbers import PhoneNumbersResource, AsyncPhoneNumbersResource
    from .resources.senders.senders import SendersResource, AsyncSendersResource
    from .resources.contacts.contacts import ContactsResource, AsyncContactsResource
    from .resources.regulatory_documents import RegulatoryDocumentsResource, AsyncRegulatoryDocumentsResource
    from .resources.broadcasts.broadcasts import BroadcastsResource, AsyncBroadcastsResource
    from .resources.number_10dlc.number_10dlc import Number10dlcResource, AsyncNumber10dlcResource
    from .resources.sub_accounts.sub_accounts import SubAccountsResource, AsyncSubAccountsResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Zavudev", "AsyncZavudev", "Client", "AsyncClient"]


class Zavudev(SyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Zavudev client instance.

        This automatically infers the `api_key` argument from the `ZAVUDEV_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("ZAVUDEV_API_KEY")
        if api_key is None:
            raise ZavudevError(
                "The api_key client option must be set either by passing api_key to the client or by setting the ZAVUDEV_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("ZAVUDEV_BASE_URL")
        if base_url is None:
            base_url = f"https://api.zavu.dev"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def messages(self) -> MessagesResource:
        from .resources.messages import MessagesResource

        return MessagesResource(self)

    @cached_property
    def templates(self) -> TemplatesResource:
        from .resources.templates import TemplatesResource

        return TemplatesResource(self)

    @cached_property
    def senders(self) -> SendersResource:
        from .resources.senders import SendersResource

        return SendersResource(self)

    @cached_property
    def contacts(self) -> ContactsResource:
        from .resources.contacts import ContactsResource

        return ContactsResource(self)

    @cached_property
    def broadcasts(self) -> BroadcastsResource:
        from .resources.broadcasts import BroadcastsResource

        return BroadcastsResource(self)

    @cached_property
    def introspect(self) -> IntrospectResource:
        from .resources.introspect import IntrospectResource

        return IntrospectResource(self)

    @cached_property
    def phone_numbers(self) -> PhoneNumbersResource:
        from .resources.phone_numbers import PhoneNumbersResource

        return PhoneNumbersResource(self)

    @cached_property
    def addresses(self) -> AddressesResource:
        from .resources.addresses import AddressesResource

        return AddressesResource(self)

    @cached_property
    def regulatory_documents(self) -> RegulatoryDocumentsResource:
        from .resources.regulatory_documents import RegulatoryDocumentsResource

        return RegulatoryDocumentsResource(self)

    @cached_property
    def invitations(self) -> InvitationsResource:
        from .resources.invitations import InvitationsResource

        return InvitationsResource(self)

    @cached_property
    def exports(self) -> ExportsResource:
        from .resources.exports import ExportsResource

        return ExportsResource(self)

    @cached_property
    def urls(self) -> URLsResource:
        from .resources.urls import URLsResource

        return URLsResource(self)

    @cached_property
    def balance(self) -> BalanceResource:
        from .resources.balance import BalanceResource

        return BalanceResource(self)

    @cached_property
    def plan(self) -> PlanResource:
        from .resources.plan import PlanResource

        return PlanResource(self)

    @cached_property
    def usage(self) -> UsageResource:
        from .resources.usage import UsageResource

        return UsageResource(self)

    @cached_property
    def sub_accounts(self) -> SubAccountsResource:
        from .resources.sub_accounts import SubAccountsResource

        return SubAccountsResource(self)

    @cached_property
    def number_10dlc(self) -> Number10dlcResource:
        from .resources.number_10dlc import Number10dlcResource

        return Number10dlcResource(self)

    @cached_property
    def with_raw_response(self) -> ZavudevWithRawResponse:
        return ZavudevWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ZavudevWithStreamedResponse:
        return ZavudevWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncZavudev(AsyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncZavudev client instance.

        This automatically infers the `api_key` argument from the `ZAVUDEV_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("ZAVUDEV_API_KEY")
        if api_key is None:
            raise ZavudevError(
                "The api_key client option must be set either by passing api_key to the client or by setting the ZAVUDEV_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("ZAVUDEV_BASE_URL")
        if base_url is None:
            base_url = f"https://api.zavu.dev"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def messages(self) -> AsyncMessagesResource:
        from .resources.messages import AsyncMessagesResource

        return AsyncMessagesResource(self)

    @cached_property
    def templates(self) -> AsyncTemplatesResource:
        from .resources.templates import AsyncTemplatesResource

        return AsyncTemplatesResource(self)

    @cached_property
    def senders(self) -> AsyncSendersResource:
        from .resources.senders import AsyncSendersResource

        return AsyncSendersResource(self)

    @cached_property
    def contacts(self) -> AsyncContactsResource:
        from .resources.contacts import AsyncContactsResource

        return AsyncContactsResource(self)

    @cached_property
    def broadcasts(self) -> AsyncBroadcastsResource:
        from .resources.broadcasts import AsyncBroadcastsResource

        return AsyncBroadcastsResource(self)

    @cached_property
    def introspect(self) -> AsyncIntrospectResource:
        from .resources.introspect import AsyncIntrospectResource

        return AsyncIntrospectResource(self)

    @cached_property
    def phone_numbers(self) -> AsyncPhoneNumbersResource:
        from .resources.phone_numbers import AsyncPhoneNumbersResource

        return AsyncPhoneNumbersResource(self)

    @cached_property
    def addresses(self) -> AsyncAddressesResource:
        from .resources.addresses import AsyncAddressesResource

        return AsyncAddressesResource(self)

    @cached_property
    def regulatory_documents(self) -> AsyncRegulatoryDocumentsResource:
        from .resources.regulatory_documents import AsyncRegulatoryDocumentsResource

        return AsyncRegulatoryDocumentsResource(self)

    @cached_property
    def invitations(self) -> AsyncInvitationsResource:
        from .resources.invitations import AsyncInvitationsResource

        return AsyncInvitationsResource(self)

    @cached_property
    def exports(self) -> AsyncExportsResource:
        from .resources.exports import AsyncExportsResource

        return AsyncExportsResource(self)

    @cached_property
    def urls(self) -> AsyncURLsResource:
        from .resources.urls import AsyncURLsResource

        return AsyncURLsResource(self)

    @cached_property
    def balance(self) -> AsyncBalanceResource:
        from .resources.balance import AsyncBalanceResource

        return AsyncBalanceResource(self)

    @cached_property
    def plan(self) -> AsyncPlanResource:
        from .resources.plan import AsyncPlanResource

        return AsyncPlanResource(self)

    @cached_property
    def usage(self) -> AsyncUsageResource:
        from .resources.usage import AsyncUsageResource

        return AsyncUsageResource(self)

    @cached_property
    def sub_accounts(self) -> AsyncSubAccountsResource:
        from .resources.sub_accounts import AsyncSubAccountsResource

        return AsyncSubAccountsResource(self)

    @cached_property
    def number_10dlc(self) -> AsyncNumber10dlcResource:
        from .resources.number_10dlc import AsyncNumber10dlcResource

        return AsyncNumber10dlcResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncZavudevWithRawResponse:
        return AsyncZavudevWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncZavudevWithStreamedResponse:
        return AsyncZavudevWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class ZavudevWithRawResponse:
    _client: Zavudev

    def __init__(self, client: Zavudev) -> None:
        self._client = client

    @cached_property
    def messages(self) -> messages.MessagesResourceWithRawResponse:
        from .resources.messages import MessagesResourceWithRawResponse

        return MessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def templates(self) -> templates.TemplatesResourceWithRawResponse:
        from .resources.templates import TemplatesResourceWithRawResponse

        return TemplatesResourceWithRawResponse(self._client.templates)

    @cached_property
    def senders(self) -> senders.SendersResourceWithRawResponse:
        from .resources.senders import SendersResourceWithRawResponse

        return SendersResourceWithRawResponse(self._client.senders)

    @cached_property
    def contacts(self) -> contacts.ContactsResourceWithRawResponse:
        from .resources.contacts import ContactsResourceWithRawResponse

        return ContactsResourceWithRawResponse(self._client.contacts)

    @cached_property
    def broadcasts(self) -> broadcasts.BroadcastsResourceWithRawResponse:
        from .resources.broadcasts import BroadcastsResourceWithRawResponse

        return BroadcastsResourceWithRawResponse(self._client.broadcasts)

    @cached_property
    def introspect(self) -> introspect.IntrospectResourceWithRawResponse:
        from .resources.introspect import IntrospectResourceWithRawResponse

        return IntrospectResourceWithRawResponse(self._client.introspect)

    @cached_property
    def phone_numbers(self) -> phone_numbers.PhoneNumbersResourceWithRawResponse:
        from .resources.phone_numbers import PhoneNumbersResourceWithRawResponse

        return PhoneNumbersResourceWithRawResponse(self._client.phone_numbers)

    @cached_property
    def addresses(self) -> addresses.AddressesResourceWithRawResponse:
        from .resources.addresses import AddressesResourceWithRawResponse

        return AddressesResourceWithRawResponse(self._client.addresses)

    @cached_property
    def regulatory_documents(self) -> regulatory_documents.RegulatoryDocumentsResourceWithRawResponse:
        from .resources.regulatory_documents import RegulatoryDocumentsResourceWithRawResponse

        return RegulatoryDocumentsResourceWithRawResponse(self._client.regulatory_documents)

    @cached_property
    def invitations(self) -> invitations.InvitationsResourceWithRawResponse:
        from .resources.invitations import InvitationsResourceWithRawResponse

        return InvitationsResourceWithRawResponse(self._client.invitations)

    @cached_property
    def exports(self) -> exports.ExportsResourceWithRawResponse:
        from .resources.exports import ExportsResourceWithRawResponse

        return ExportsResourceWithRawResponse(self._client.exports)

    @cached_property
    def urls(self) -> urls.URLsResourceWithRawResponse:
        from .resources.urls import URLsResourceWithRawResponse

        return URLsResourceWithRawResponse(self._client.urls)

    @cached_property
    def balance(self) -> balance.BalanceResourceWithRawResponse:
        from .resources.balance import BalanceResourceWithRawResponse

        return BalanceResourceWithRawResponse(self._client.balance)

    @cached_property
    def plan(self) -> plan.PlanResourceWithRawResponse:
        from .resources.plan import PlanResourceWithRawResponse

        return PlanResourceWithRawResponse(self._client.plan)

    @cached_property
    def usage(self) -> usage.UsageResourceWithRawResponse:
        from .resources.usage import UsageResourceWithRawResponse

        return UsageResourceWithRawResponse(self._client.usage)

    @cached_property
    def sub_accounts(self) -> sub_accounts.SubAccountsResourceWithRawResponse:
        from .resources.sub_accounts import SubAccountsResourceWithRawResponse

        return SubAccountsResourceWithRawResponse(self._client.sub_accounts)

    @cached_property
    def number_10dlc(self) -> number_10dlc.Number10dlcResourceWithRawResponse:
        from .resources.number_10dlc import Number10dlcResourceWithRawResponse

        return Number10dlcResourceWithRawResponse(self._client.number_10dlc)


class AsyncZavudevWithRawResponse:
    _client: AsyncZavudev

    def __init__(self, client: AsyncZavudev) -> None:
        self._client = client

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithRawResponse:
        from .resources.messages import AsyncMessagesResourceWithRawResponse

        return AsyncMessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def templates(self) -> templates.AsyncTemplatesResourceWithRawResponse:
        from .resources.templates import AsyncTemplatesResourceWithRawResponse

        return AsyncTemplatesResourceWithRawResponse(self._client.templates)

    @cached_property
    def senders(self) -> senders.AsyncSendersResourceWithRawResponse:
        from .resources.senders import AsyncSendersResourceWithRawResponse

        return AsyncSendersResourceWithRawResponse(self._client.senders)

    @cached_property
    def contacts(self) -> contacts.AsyncContactsResourceWithRawResponse:
        from .resources.contacts import AsyncContactsResourceWithRawResponse

        return AsyncContactsResourceWithRawResponse(self._client.contacts)

    @cached_property
    def broadcasts(self) -> broadcasts.AsyncBroadcastsResourceWithRawResponse:
        from .resources.broadcasts import AsyncBroadcastsResourceWithRawResponse

        return AsyncBroadcastsResourceWithRawResponse(self._client.broadcasts)

    @cached_property
    def introspect(self) -> introspect.AsyncIntrospectResourceWithRawResponse:
        from .resources.introspect import AsyncIntrospectResourceWithRawResponse

        return AsyncIntrospectResourceWithRawResponse(self._client.introspect)

    @cached_property
    def phone_numbers(self) -> phone_numbers.AsyncPhoneNumbersResourceWithRawResponse:
        from .resources.phone_numbers import AsyncPhoneNumbersResourceWithRawResponse

        return AsyncPhoneNumbersResourceWithRawResponse(self._client.phone_numbers)

    @cached_property
    def addresses(self) -> addresses.AsyncAddressesResourceWithRawResponse:
        from .resources.addresses import AsyncAddressesResourceWithRawResponse

        return AsyncAddressesResourceWithRawResponse(self._client.addresses)

    @cached_property
    def regulatory_documents(self) -> regulatory_documents.AsyncRegulatoryDocumentsResourceWithRawResponse:
        from .resources.regulatory_documents import AsyncRegulatoryDocumentsResourceWithRawResponse

        return AsyncRegulatoryDocumentsResourceWithRawResponse(self._client.regulatory_documents)

    @cached_property
    def invitations(self) -> invitations.AsyncInvitationsResourceWithRawResponse:
        from .resources.invitations import AsyncInvitationsResourceWithRawResponse

        return AsyncInvitationsResourceWithRawResponse(self._client.invitations)

    @cached_property
    def exports(self) -> exports.AsyncExportsResourceWithRawResponse:
        from .resources.exports import AsyncExportsResourceWithRawResponse

        return AsyncExportsResourceWithRawResponse(self._client.exports)

    @cached_property
    def urls(self) -> urls.AsyncURLsResourceWithRawResponse:
        from .resources.urls import AsyncURLsResourceWithRawResponse

        return AsyncURLsResourceWithRawResponse(self._client.urls)

    @cached_property
    def balance(self) -> balance.AsyncBalanceResourceWithRawResponse:
        from .resources.balance import AsyncBalanceResourceWithRawResponse

        return AsyncBalanceResourceWithRawResponse(self._client.balance)

    @cached_property
    def plan(self) -> plan.AsyncPlanResourceWithRawResponse:
        from .resources.plan import AsyncPlanResourceWithRawResponse

        return AsyncPlanResourceWithRawResponse(self._client.plan)

    @cached_property
    def usage(self) -> usage.AsyncUsageResourceWithRawResponse:
        from .resources.usage import AsyncUsageResourceWithRawResponse

        return AsyncUsageResourceWithRawResponse(self._client.usage)

    @cached_property
    def sub_accounts(self) -> sub_accounts.AsyncSubAccountsResourceWithRawResponse:
        from .resources.sub_accounts import AsyncSubAccountsResourceWithRawResponse

        return AsyncSubAccountsResourceWithRawResponse(self._client.sub_accounts)

    @cached_property
    def number_10dlc(self) -> number_10dlc.AsyncNumber10dlcResourceWithRawResponse:
        from .resources.number_10dlc import AsyncNumber10dlcResourceWithRawResponse

        return AsyncNumber10dlcResourceWithRawResponse(self._client.number_10dlc)


class ZavudevWithStreamedResponse:
    _client: Zavudev

    def __init__(self, client: Zavudev) -> None:
        self._client = client

    @cached_property
    def messages(self) -> messages.MessagesResourceWithStreamingResponse:
        from .resources.messages import MessagesResourceWithStreamingResponse

        return MessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def templates(self) -> templates.TemplatesResourceWithStreamingResponse:
        from .resources.templates import TemplatesResourceWithStreamingResponse

        return TemplatesResourceWithStreamingResponse(self._client.templates)

    @cached_property
    def senders(self) -> senders.SendersResourceWithStreamingResponse:
        from .resources.senders import SendersResourceWithStreamingResponse

        return SendersResourceWithStreamingResponse(self._client.senders)

    @cached_property
    def contacts(self) -> contacts.ContactsResourceWithStreamingResponse:
        from .resources.contacts import ContactsResourceWithStreamingResponse

        return ContactsResourceWithStreamingResponse(self._client.contacts)

    @cached_property
    def broadcasts(self) -> broadcasts.BroadcastsResourceWithStreamingResponse:
        from .resources.broadcasts import BroadcastsResourceWithStreamingResponse

        return BroadcastsResourceWithStreamingResponse(self._client.broadcasts)

    @cached_property
    def introspect(self) -> introspect.IntrospectResourceWithStreamingResponse:
        from .resources.introspect import IntrospectResourceWithStreamingResponse

        return IntrospectResourceWithStreamingResponse(self._client.introspect)

    @cached_property
    def phone_numbers(self) -> phone_numbers.PhoneNumbersResourceWithStreamingResponse:
        from .resources.phone_numbers import PhoneNumbersResourceWithStreamingResponse

        return PhoneNumbersResourceWithStreamingResponse(self._client.phone_numbers)

    @cached_property
    def addresses(self) -> addresses.AddressesResourceWithStreamingResponse:
        from .resources.addresses import AddressesResourceWithStreamingResponse

        return AddressesResourceWithStreamingResponse(self._client.addresses)

    @cached_property
    def regulatory_documents(self) -> regulatory_documents.RegulatoryDocumentsResourceWithStreamingResponse:
        from .resources.regulatory_documents import RegulatoryDocumentsResourceWithStreamingResponse

        return RegulatoryDocumentsResourceWithStreamingResponse(self._client.regulatory_documents)

    @cached_property
    def invitations(self) -> invitations.InvitationsResourceWithStreamingResponse:
        from .resources.invitations import InvitationsResourceWithStreamingResponse

        return InvitationsResourceWithStreamingResponse(self._client.invitations)

    @cached_property
    def exports(self) -> exports.ExportsResourceWithStreamingResponse:
        from .resources.exports import ExportsResourceWithStreamingResponse

        return ExportsResourceWithStreamingResponse(self._client.exports)

    @cached_property
    def urls(self) -> urls.URLsResourceWithStreamingResponse:
        from .resources.urls import URLsResourceWithStreamingResponse

        return URLsResourceWithStreamingResponse(self._client.urls)

    @cached_property
    def balance(self) -> balance.BalanceResourceWithStreamingResponse:
        from .resources.balance import BalanceResourceWithStreamingResponse

        return BalanceResourceWithStreamingResponse(self._client.balance)

    @cached_property
    def plan(self) -> plan.PlanResourceWithStreamingResponse:
        from .resources.plan import PlanResourceWithStreamingResponse

        return PlanResourceWithStreamingResponse(self._client.plan)

    @cached_property
    def usage(self) -> usage.UsageResourceWithStreamingResponse:
        from .resources.usage import UsageResourceWithStreamingResponse

        return UsageResourceWithStreamingResponse(self._client.usage)

    @cached_property
    def sub_accounts(self) -> sub_accounts.SubAccountsResourceWithStreamingResponse:
        from .resources.sub_accounts import SubAccountsResourceWithStreamingResponse

        return SubAccountsResourceWithStreamingResponse(self._client.sub_accounts)

    @cached_property
    def number_10dlc(self) -> number_10dlc.Number10dlcResourceWithStreamingResponse:
        from .resources.number_10dlc import Number10dlcResourceWithStreamingResponse

        return Number10dlcResourceWithStreamingResponse(self._client.number_10dlc)


class AsyncZavudevWithStreamedResponse:
    _client: AsyncZavudev

    def __init__(self, client: AsyncZavudev) -> None:
        self._client = client

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithStreamingResponse:
        from .resources.messages import AsyncMessagesResourceWithStreamingResponse

        return AsyncMessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def templates(self) -> templates.AsyncTemplatesResourceWithStreamingResponse:
        from .resources.templates import AsyncTemplatesResourceWithStreamingResponse

        return AsyncTemplatesResourceWithStreamingResponse(self._client.templates)

    @cached_property
    def senders(self) -> senders.AsyncSendersResourceWithStreamingResponse:
        from .resources.senders import AsyncSendersResourceWithStreamingResponse

        return AsyncSendersResourceWithStreamingResponse(self._client.senders)

    @cached_property
    def contacts(self) -> contacts.AsyncContactsResourceWithStreamingResponse:
        from .resources.contacts import AsyncContactsResourceWithStreamingResponse

        return AsyncContactsResourceWithStreamingResponse(self._client.contacts)

    @cached_property
    def broadcasts(self) -> broadcasts.AsyncBroadcastsResourceWithStreamingResponse:
        from .resources.broadcasts import AsyncBroadcastsResourceWithStreamingResponse

        return AsyncBroadcastsResourceWithStreamingResponse(self._client.broadcasts)

    @cached_property
    def introspect(self) -> introspect.AsyncIntrospectResourceWithStreamingResponse:
        from .resources.introspect import AsyncIntrospectResourceWithStreamingResponse

        return AsyncIntrospectResourceWithStreamingResponse(self._client.introspect)

    @cached_property
    def phone_numbers(self) -> phone_numbers.AsyncPhoneNumbersResourceWithStreamingResponse:
        from .resources.phone_numbers import AsyncPhoneNumbersResourceWithStreamingResponse

        return AsyncPhoneNumbersResourceWithStreamingResponse(self._client.phone_numbers)

    @cached_property
    def addresses(self) -> addresses.AsyncAddressesResourceWithStreamingResponse:
        from .resources.addresses import AsyncAddressesResourceWithStreamingResponse

        return AsyncAddressesResourceWithStreamingResponse(self._client.addresses)

    @cached_property
    def regulatory_documents(self) -> regulatory_documents.AsyncRegulatoryDocumentsResourceWithStreamingResponse:
        from .resources.regulatory_documents import AsyncRegulatoryDocumentsResourceWithStreamingResponse

        return AsyncRegulatoryDocumentsResourceWithStreamingResponse(self._client.regulatory_documents)

    @cached_property
    def invitations(self) -> invitations.AsyncInvitationsResourceWithStreamingResponse:
        from .resources.invitations import AsyncInvitationsResourceWithStreamingResponse

        return AsyncInvitationsResourceWithStreamingResponse(self._client.invitations)

    @cached_property
    def exports(self) -> exports.AsyncExportsResourceWithStreamingResponse:
        from .resources.exports import AsyncExportsResourceWithStreamingResponse

        return AsyncExportsResourceWithStreamingResponse(self._client.exports)

    @cached_property
    def urls(self) -> urls.AsyncURLsResourceWithStreamingResponse:
        from .resources.urls import AsyncURLsResourceWithStreamingResponse

        return AsyncURLsResourceWithStreamingResponse(self._client.urls)

    @cached_property
    def balance(self) -> balance.AsyncBalanceResourceWithStreamingResponse:
        from .resources.balance import AsyncBalanceResourceWithStreamingResponse

        return AsyncBalanceResourceWithStreamingResponse(self._client.balance)

    @cached_property
    def plan(self) -> plan.AsyncPlanResourceWithStreamingResponse:
        from .resources.plan import AsyncPlanResourceWithStreamingResponse

        return AsyncPlanResourceWithStreamingResponse(self._client.plan)

    @cached_property
    def usage(self) -> usage.AsyncUsageResourceWithStreamingResponse:
        from .resources.usage import AsyncUsageResourceWithStreamingResponse

        return AsyncUsageResourceWithStreamingResponse(self._client.usage)

    @cached_property
    def sub_accounts(self) -> sub_accounts.AsyncSubAccountsResourceWithStreamingResponse:
        from .resources.sub_accounts import AsyncSubAccountsResourceWithStreamingResponse

        return AsyncSubAccountsResourceWithStreamingResponse(self._client.sub_accounts)

    @cached_property
    def number_10dlc(self) -> number_10dlc.AsyncNumber10dlcResourceWithStreamingResponse:
        from .resources.number_10dlc import AsyncNumber10dlcResourceWithStreamingResponse

        return AsyncNumber10dlcResourceWithStreamingResponse(self._client.number_10dlc)


Client = Zavudev

AsyncClient = AsyncZavudev
