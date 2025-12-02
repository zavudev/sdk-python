# Zavu SDK

## Overview

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


### Available Operations

* [send_message](#send_message) - Send a message
* [list_messages](#list_messages) - List messages
* [get_message](#get_message) - Get message by ID
* [send_reaction](#send_reaction) - Send reaction to message
* [list_templates](#list_templates) - List templates
* [create_template](#create_template) - Create template
* [get_template](#get_template) - Get template
* [delete_template](#delete_template) - Delete template
* [list_senders](#list_senders) - List senders
* [create_sender](#create_sender) - Create sender
* [get_sender](#get_sender) - Get sender
* [update_sender](#update_sender) - Update sender
* [delete_sender](#delete_sender) - Delete sender
* [list_contacts](#list_contacts) - List contacts
* [get_contact](#get_contact) - Get contact
* [update_contact](#update_contact) - Update contact
* [get_contact_by_phone](#get_contact_by_phone) - Get contact by phone number
* [introspect_phone](#introspect_phone) - Introspect phone number

## send_message

Send a message to a recipient via SMS or WhatsApp.

**Channel selection:**
- If `channel` is omitted and `messageType` is `text`, defaults to SMS
- If `messageType` is anything other than `text`, WhatsApp is used automatically

**WhatsApp 24-hour window:**
- Free-form messages (non-template) require an open 24h window
- Window opens when the user messages you first
- Use template messages to initiate conversations outside the window

### Example Usage

<!-- UsageSnippet language="python" operationID="sendMessage" method="post" path="/v1/messages" -->
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

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        | Example                                                                            |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `to`                                                                               | *str*                                                                              | :heavy_check_mark:                                                                 | Recipient phone number in E.164 format.                                            | +56912345678                                                                       |
| `zavu_sender`                                                                      | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | Optional sender profile ID. If omitted, the project's default sender will be used. | sender_12345                                                                       |
| `channel`                                                                          | [Optional[models.Channel]](../../models/channel.md)                                | :heavy_minus_sign:                                                                 | Delivery channel.                                                                  |                                                                                    |
| `message_type`                                                                     | [Optional[models.MessageType]](../../models/messagetype.md)                        | :heavy_minus_sign:                                                                 | Type of message. Non-text types are WhatsApp only.                                 |                                                                                    |
| `text`                                                                             | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | Text body for text messages or caption for media messages.                         | Your verification code is 123456.                                                  |
| `content`                                                                          | [Optional[models.MessageContent]](../../models/messagecontent.md)                  | :heavy_minus_sign:                                                                 | Content for non-text message types (WhatsApp only).                                |                                                                                    |
| `idempotency_key`                                                                  | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | Optional idempotency key to avoid duplicate sends.                                 | msg_01HZY4ZP7VQY2J3BRW7Z6G0QGE                                                     |
| `metadata`                                                                         | Dict[str, *str*]                                                                   | :heavy_minus_sign:                                                                 | Arbitrary metadata to associate with the message.                                  |                                                                                    |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |                                                                                    |

### Response

**[models.MessageResponse](../../models/messageresponse.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.Error            | 400, 401, 404, 409, 429 | application/json        |
| errors.Error            | 500                     | application/json        |
| errors.SDKDefaultError  | 4XX, 5XX                | \*/\*                   |

## list_messages

List messages previously sent by this project.

### Example Usage

<!-- UsageSnippet language="python" operationID="listMessages" method="get" path="/v1/messages" -->
```python
from zavu_sdk import Zavu


with Zavu(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as zavu:

    res = zavu.list_messages(limit=50)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `status`                                                            | [Optional[models.MessageStatus]](../../models/messagestatus.md)     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `to`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `channel`                                                           | [Optional[models.Channel]](../../models/channel.md)                 | :heavy_minus_sign:                                                  | Delivery channel.                                                   |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListMessagesResponse](../../models/listmessagesresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.Error           | 401                    | application/json       |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## get_message

Get message by ID

### Example Usage

<!-- UsageSnippet language="python" operationID="getMessage" method="get" path="/v1/messages/{messageId}" -->
```python
from zavu_sdk import Zavu


with Zavu(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as zavu:

    res = zavu.get_message(message_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `message_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.MessageResponse](../../models/messageresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.Error           | 401, 404               | application/json       |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## send_reaction

Send an emoji reaction to an existing WhatsApp message. Reactions are only supported for WhatsApp messages.

### Example Usage

<!-- UsageSnippet language="python" operationID="sendReaction" method="post" path="/v1/messages/{messageId}/reactions" -->
```python
from zavu_sdk import Zavu


with Zavu(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as zavu:

    res = zavu.send_reaction(message_id="<id>", emoji="👍", zavu_sender="sender_12345")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        | Example                                                                            |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `message_id`                                                                       | *str*                                                                              | :heavy_check_mark:                                                                 | N/A                                                                                |                                                                                    |
| `emoji`                                                                            | *str*                                                                              | :heavy_check_mark:                                                                 | Single emoji character to react with.                                              | 👍                                                                                 |
| `zavu_sender`                                                                      | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | Optional sender profile ID. If omitted, the project's default sender will be used. | sender_12345                                                                       |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |                                                                                    |

### Response

**[models.MessageResponse](../../models/messageresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.Error           | 400, 401, 404          | application/json       |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## list_templates

List WhatsApp message templates for this project.

### Example Usage

<!-- UsageSnippet language="python" operationID="listTemplates" method="get" path="/v1/templates" -->
```python
from zavu_sdk import Zavu


with Zavu(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as zavu:

    res = zavu.list_templates()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListTemplatesResponse](../../models/listtemplatesresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.Error           | 401                    | application/json       |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## create_template

Create a WhatsApp message template. Note: Templates must be approved by Meta before use.

### Example Usage

<!-- UsageSnippet language="python" operationID="createTemplate" method="post" path="/v1/templates" -->
```python
from zavu_sdk import Zavu


with Zavu(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as zavu:

    res = zavu.create_template(name="order_confirmation", body="Hi {{1}}, your order {{2}} has been confirmed and will ship within 24 hours.", language="en", whatsapp_category="UTILITY", variables=[
        "customer_name",
        "order_id",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `name`                                                                | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `body`                                                                | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `language`                                                            | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `whatsapp_category`                                                   | [Optional[models.WhatsAppCategory]](../../models/whatsappcategory.md) | :heavy_minus_sign:                                                    | WhatsApp template category.                                           |
| `variables`                                                           | List[*str*]                                                           | :heavy_minus_sign:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.Template](../../models/template.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.Error           | 400, 401               | application/json       |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## get_template

Get template

### Example Usage

<!-- UsageSnippet language="python" operationID="getTemplate" method="get" path="/v1/templates/{templateId}" -->
```python
from zavu_sdk import Zavu


with Zavu(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as zavu:

    res = zavu.get_template(template_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `template_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Template](../../models/template.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.Error           | 401, 404               | application/json       |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## delete_template

Delete template

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteTemplate" method="delete" path="/v1/templates/{templateId}" -->
```python
from zavu_sdk import Zavu


with Zavu(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as zavu:

    zavu.delete_template(template_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `template_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.Error           | 401, 404               | application/json       |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## list_senders

List senders

### Example Usage

<!-- UsageSnippet language="python" operationID="listSenders" method="get" path="/v1/senders" -->
```python
from zavu_sdk import Zavu


with Zavu(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as zavu:

    res = zavu.list_senders()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListSendersResponse](../../models/listsendersresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.Error           | 401                    | application/json       |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## create_sender

Create sender

### Example Usage

<!-- UsageSnippet language="python" operationID="createSender" method="post" path="/v1/senders" -->
```python
from zavu_sdk import Zavu


with Zavu(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as zavu:

    res = zavu.create_sender(name="<value>", phone_number="1-697-351-3400 x33934", set_as_default=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `phone_number`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `set_as_default`                                                    | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Sender](../../models/sender.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.Error           | 400, 401               | application/json       |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## get_sender

Get sender

### Example Usage

<!-- UsageSnippet language="python" operationID="getSender" method="get" path="/v1/senders/{senderId}" -->
```python
from zavu_sdk import Zavu


with Zavu(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as zavu:

    res = zavu.get_sender(sender_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `sender_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Sender](../../models/sender.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.Error           | 401, 404               | application/json       |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## update_sender

Update sender

### Example Usage

<!-- UsageSnippet language="python" operationID="updateSender" method="patch" path="/v1/senders/{senderId}" -->
```python
from zavu_sdk import Zavu


with Zavu(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as zavu:

    res = zavu.update_sender(sender_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `sender_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `name`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `set_as_default`                                                    | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Sender](../../models/sender.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.Error           | 400, 401, 404          | application/json       |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## delete_sender

Delete sender

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteSender" method="delete" path="/v1/senders/{senderId}" -->
```python
from zavu_sdk import Zavu


with Zavu(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as zavu:

    zavu.delete_sender(sender_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `sender_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.Error           | 400, 401, 404          | application/json       |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## list_contacts

List contacts

### Example Usage

<!-- UsageSnippet language="python" operationID="listContacts" method="get" path="/v1/contacts" -->
```python
from zavu_sdk import Zavu


with Zavu(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as zavu:

    res = zavu.list_contacts(limit=50)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `phone_number`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListContactsResponse](../../models/listcontactsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.Error           | 401                    | application/json       |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## get_contact

Get contact

### Example Usage

<!-- UsageSnippet language="python" operationID="getContact" method="get" path="/v1/contacts/{contactId}" -->
```python
from zavu_sdk import Zavu


with Zavu(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as zavu:

    res = zavu.get_contact(contact_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `contact_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Contact](../../models/contact.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.Error           | 401, 404               | application/json       |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## update_contact

Update contact

### Example Usage

<!-- UsageSnippet language="python" operationID="updateContact" method="patch" path="/v1/contacts/{contactId}" -->
```python
from zavu_sdk import Zavu


with Zavu(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as zavu:

    res = zavu.update_contact(contact_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `contact_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `metadata`                                                          | Dict[str, *str*]                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Contact](../../models/contact.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.Error           | 400, 401, 404          | application/json       |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## get_contact_by_phone

Get contact by phone number

### Example Usage

<!-- UsageSnippet language="python" operationID="getContactByPhone" method="get" path="/v1/contacts/phone/{phoneNumber}" -->
```python
from zavu_sdk import Zavu


with Zavu(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as zavu:

    res = zavu.get_contact_by_phone(phone_number="397-335-4175 x077")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `phone_number`                                                      | *str*                                                               | :heavy_check_mark:                                                  | E.164 phone number.                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Contact](../../models/contact.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.Error           | 401, 404               | application/json       |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## introspect_phone

Validate a phone number and check if a WhatsApp conversation window is open.

### Example Usage

<!-- UsageSnippet language="python" operationID="introspectPhone" method="post" path="/v1/introspect/phone" -->
```python
from zavu_sdk import Zavu


with Zavu(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as zavu:

    res = zavu.introspect_phone(phone_number="+56912345678")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `phone_number`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | +56912345678                                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.PhoneIntrospectionResponse](../../models/phoneintrospectionresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.Error           | 400, 401               | application/json       |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |