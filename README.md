# openapi

Developer-friendly & type-safe Python SDK specifically catered to leverage *openapi* API.

[![Built by Speakeasy](https://img.shields.io/badge/Built_by-SPEAKEASY-374151?style=for-the-badge&labelColor=f3f4f6)](https://www.speakeasy.com/?utm_source=openapi&utm_campaign=python)
[![License: MIT](https://img.shields.io/badge/LICENSE_//_MIT-3b5bdb?style=for-the-badge&labelColor=eff6ff)](https://opensource.org/licenses/MIT)


<br /><br />
> [!IMPORTANT]
> This SDK is not yet ready for production use. To complete setup please follow the steps outlined in your [workspace](https://app.speakeasy.com/org/crubing/zavu). Delete this section before > publishing to a package manager.

<!-- Start Summary [summary] -->
## Summary

Zavu Messaging API: Unified multi-channel messaging API for Zavu.

Supported channels:
- **SMS**: Simple text messages
- **WhatsApp**: Rich messaging with media, buttons, lists, and templates

Design goals:
- Simple `send()` entrypoint for developers
- Project-level authentication via Bearer token
- Support for all WhatsApp message types (text, image, video, audio, document, sticker, location, contact, buttons, list, reaction, template)
- If a non-text message type is sent, WhatsApp channel is used automatically
- 24-hour WhatsApp conversation window enforcement
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [openapi](#openapi)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!TIP]
> To finish publishing your SDK to PyPI you must [run your first generation action](https://www.speakeasy.com/docs/github-setup#step-by-step-guide).


> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with *uv*, *pip*, or *poetry* package managers.

### uv

*uv* is a fast Python package installer and resolver, designed as a drop-in replacement for pip and pip-tools. It's recommended for its speed and modern Python tooling capabilities.

```bash
uv add git+<UNSET>.git
```

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install git+<UNSET>.git
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add git+<UNSET>.git
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from zavu-sdk python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "zavu-sdk",
# ]
# ///

from zavu_sdk import Zavu

sdk = Zavu(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from zavu_sdk import Zavu


with Zavu(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as zavu:

    res = zavu.send_message(to="+56912345678", zavu_sender="sender_12345", text="Your verification code is 123456", content={
        "media_url": "https://example.com/image.jpg",
        "mime_type": "image/jpeg",
        "filename": "invoice.pdf",
        "template_variables": {
            "1": "John",
            "2": "ORD-12345",
        },
    }, idempotency_key="msg_01HZY4ZP7VQY2J3BRW7Z6G0QGE")

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from zavu_sdk import Zavu

async def main():

    async with Zavu(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ) as zavu:

        res = await zavu.send_message_async(to="+56912345678", zavu_sender="sender_12345", text="Your verification code is 123456", content={
            "media_url": "https://example.com/image.jpg",
            "mime_type": "image/jpeg",
            "filename": "invoice.pdf",
            "template_variables": {
                "1": "John",
                "2": "ORD-12345",
            },
        }, idempotency_key="msg_01HZY4ZP7VQY2J3BRW7Z6G0QGE")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name          | Type | Scheme      |
| ------------- | ---- | ----------- |
| `bearer_auth` | http | HTTP Bearer |

To authenticate with the API the `bearer_auth` parameter must be set when initializing the SDK client instance. For example:
```python
from zavu_sdk import Zavu


with Zavu(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as zavu:

    res = zavu.send_message(to="+56912345678", zavu_sender="sender_12345", text="Your verification code is 123456", content={
        "media_url": "https://example.com/image.jpg",
        "mime_type": "image/jpeg",
        "filename": "invoice.pdf",
        "template_variables": {
            "1": "John",
            "2": "ORD-12345",
        },
    }, idempotency_key="msg_01HZY4ZP7VQY2J3BRW7Z6G0QGE")

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [Zavu SDK](docs/sdks/zavu/README.md)

* [send_message](docs/sdks/zavu/README.md#send_message) - Send a message
* [list_messages](docs/sdks/zavu/README.md#list_messages) - List messages
* [get_message](docs/sdks/zavu/README.md#get_message) - Get message by ID
* [send_reaction](docs/sdks/zavu/README.md#send_reaction) - Send reaction to message
* [list_templates](docs/sdks/zavu/README.md#list_templates) - List templates
* [create_template](docs/sdks/zavu/README.md#create_template) - Create template
* [get_template](docs/sdks/zavu/README.md#get_template) - Get template
* [delete_template](docs/sdks/zavu/README.md#delete_template) - Delete template
* [list_senders](docs/sdks/zavu/README.md#list_senders) - List senders
* [create_sender](docs/sdks/zavu/README.md#create_sender) - Create sender
* [get_sender](docs/sdks/zavu/README.md#get_sender) - Get sender
* [update_sender](docs/sdks/zavu/README.md#update_sender) - Update sender
* [delete_sender](docs/sdks/zavu/README.md#delete_sender) - Delete sender
* [list_contacts](docs/sdks/zavu/README.md#list_contacts) - List contacts
* [get_contact](docs/sdks/zavu/README.md#get_contact) - Get contact
* [update_contact](docs/sdks/zavu/README.md#update_contact) - Update contact
* [get_contact_by_phone](docs/sdks/zavu/README.md#get_contact_by_phone) - Get contact by phone number
* [introspect_phone](docs/sdks/zavu/README.md#introspect_phone) - Introspect phone number

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from zavu_sdk import Zavu
from zavu_sdk.utils import BackoffStrategy, RetryConfig


with Zavu(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as zavu:

    res = zavu.send_message(to="+56912345678", zavu_sender="sender_12345", text="Your verification code is 123456", content={
        "media_url": "https://example.com/image.jpg",
        "mime_type": "image/jpeg",
        "filename": "invoice.pdf",
        "template_variables": {
            "1": "John",
            "2": "ORD-12345",
        },
    }, idempotency_key="msg_01HZY4ZP7VQY2J3BRW7Z6G0QGE",
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from zavu_sdk import Zavu
from zavu_sdk.utils import BackoffStrategy, RetryConfig


with Zavu(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as zavu:

    res = zavu.send_message(to="+56912345678", zavu_sender="sender_12345", text="Your verification code is 123456", content={
        "media_url": "https://example.com/image.jpg",
        "mime_type": "image/jpeg",
        "filename": "invoice.pdf",
        "template_variables": {
            "1": "John",
            "2": "ORD-12345",
        },
    }, idempotency_key="msg_01HZY4ZP7VQY2J3BRW7Z6G0QGE")

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`SDKError`](./src/zavu_sdk/errors/sdkerror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](#error-classes). |

### Example
```python
from zavu_sdk import Zavu, errors


with Zavu(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as zavu:
    res = None
    try:

        res = zavu.send_message(to="+56912345678", zavu_sender="sender_12345", text="Your verification code is 123456", content={
            "media_url": "https://example.com/image.jpg",
            "mime_type": "image/jpeg",
            "filename": "invoice.pdf",
            "template_variables": {
                "1": "John",
                "2": "ORD-12345",
            },
        }, idempotency_key="msg_01HZY4ZP7VQY2J3BRW7Z6G0QGE")

        # Handle response
        print(res)


    except errors.SDKError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

        # Depending on the method different errors may be thrown
        if isinstance(e, errors.Error):
            print(e.data.code)  # str
            print(e.data.message)  # str
            print(e.data.details)  # Optional[Dict[str, Any]]
```

### Error Classes
**Primary errors:**
* [`SDKError`](./src/zavu_sdk/errors/sdkerror.py): The base class for HTTP error responses.
  * [`Error`](./src/zavu_sdk/errors/error.py): Generic error.

<details><summary>Less common errors (5)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`SDKError`](./src/zavu_sdk/errors/sdkerror.py)**:
* [`ResponseValidationError`](./src/zavu_sdk/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from zavu_sdk import Zavu


with Zavu(
    server_url="https://api.zavu.dev",
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as zavu:

    res = zavu.send_message(to="+56912345678", zavu_sender="sender_12345", text="Your verification code is 123456", content={
        "media_url": "https://example.com/image.jpg",
        "mime_type": "image/jpeg",
        "filename": "invoice.pdf",
        "template_variables": {
            "1": "John",
            "2": "ORD-12345",
        },
    }, idempotency_key="msg_01HZY4ZP7VQY2J3BRW7Z6G0QGE")

    # Handle response
    print(res)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from zavu_sdk import Zavu
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Zavu(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from zavu_sdk import Zavu
from zavu_sdk.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Zavu(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `Zavu` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from zavu_sdk import Zavu
def main():

    with Zavu(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ) as zavu:
        # Rest of application here...


# Or when using async:
async def amain():

    async with Zavu(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ) as zavu:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from zavu_sdk import Zavu
import logging

logging.basicConfig(level=logging.DEBUG)
s = Zavu(debug_logger=logging.getLogger("zavu_sdk"))
```
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=openapi&utm_campaign=python)
