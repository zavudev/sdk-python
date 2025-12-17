# Messages

Types:

```python
from zavudev.types import (
    Channel,
    Message,
    MessageContent,
    MessageResponse,
    MessageStatus,
    MessageType,
)
```

Methods:

- <code title="get /v1/messages/{messageId}">client.messages.<a href="./src/zavudev/resources/messages.py">retrieve</a>(message_id) -> <a href="./src/zavudev/types/message_response.py">MessageResponse</a></code>
- <code title="get /v1/messages">client.messages.<a href="./src/zavudev/resources/messages.py">list</a>(\*\*<a href="src/zavudev/types/message_list_params.py">params</a>) -> <a href="./src/zavudev/types/message.py">SyncCursor[Message]</a></code>
- <code title="post /v1/messages/{messageId}/reactions">client.messages.<a href="./src/zavudev/resources/messages.py">react</a>(message_id, \*\*<a href="src/zavudev/types/message_react_params.py">params</a>) -> <a href="./src/zavudev/types/message_response.py">MessageResponse</a></code>
- <code title="post /v1/messages">client.messages.<a href="./src/zavudev/resources/messages.py">send</a>(\*\*<a href="src/zavudev/types/message_send_params.py">params</a>) -> <a href="./src/zavudev/types/message_response.py">MessageResponse</a></code>

# Templates

Types:

```python
from zavudev.types import Template, WhatsappCategory
```

Methods:

- <code title="post /v1/templates">client.templates.<a href="./src/zavudev/resources/templates.py">create</a>(\*\*<a href="src/zavudev/types/template_create_params.py">params</a>) -> <a href="./src/zavudev/types/template.py">Template</a></code>
- <code title="get /v1/templates/{templateId}">client.templates.<a href="./src/zavudev/resources/templates.py">retrieve</a>(template_id) -> <a href="./src/zavudev/types/template.py">Template</a></code>
- <code title="get /v1/templates">client.templates.<a href="./src/zavudev/resources/templates.py">list</a>(\*\*<a href="src/zavudev/types/template_list_params.py">params</a>) -> <a href="./src/zavudev/types/template.py">SyncCursor[Template]</a></code>
- <code title="delete /v1/templates/{templateId}">client.templates.<a href="./src/zavudev/resources/templates.py">delete</a>(template_id) -> None</code>
- <code title="post /v1/templates/{templateId}/submit">client.templates.<a href="./src/zavudev/resources/templates.py">submit</a>(template_id, \*\*<a href="src/zavudev/types/template_submit_params.py">params</a>) -> <a href="./src/zavudev/types/template.py">Template</a></code>

# Senders

Types:

```python
from zavudev.types import (
    Sender,
    SenderWebhook,
    WebhookEvent,
    WebhookSecretResponse,
    WhatsappBusinessProfile,
    WhatsappBusinessProfileResponse,
    WhatsappBusinessProfileVertical,
    SenderUpdateProfileResponse,
    SenderUploadProfilePictureResponse,
)
```

Methods:

- <code title="post /v1/senders">client.senders.<a href="./src/zavudev/resources/senders.py">create</a>(\*\*<a href="src/zavudev/types/sender_create_params.py">params</a>) -> <a href="./src/zavudev/types/sender.py">Sender</a></code>
- <code title="get /v1/senders/{senderId}">client.senders.<a href="./src/zavudev/resources/senders.py">retrieve</a>(sender_id) -> <a href="./src/zavudev/types/sender.py">Sender</a></code>
- <code title="patch /v1/senders/{senderId}">client.senders.<a href="./src/zavudev/resources/senders.py">update</a>(sender_id, \*\*<a href="src/zavudev/types/sender_update_params.py">params</a>) -> <a href="./src/zavudev/types/sender.py">Sender</a></code>
- <code title="get /v1/senders">client.senders.<a href="./src/zavudev/resources/senders.py">list</a>(\*\*<a href="src/zavudev/types/sender_list_params.py">params</a>) -> <a href="./src/zavudev/types/sender.py">SyncCursor[Sender]</a></code>
- <code title="delete /v1/senders/{senderId}">client.senders.<a href="./src/zavudev/resources/senders.py">delete</a>(sender_id) -> None</code>
- <code title="get /v1/senders/{senderId}/profile">client.senders.<a href="./src/zavudev/resources/senders.py">get_profile</a>(sender_id) -> <a href="./src/zavudev/types/whatsapp_business_profile_response.py">WhatsappBusinessProfileResponse</a></code>
- <code title="post /v1/senders/{senderId}/webhook/secret">client.senders.<a href="./src/zavudev/resources/senders.py">regenerate_webhook_secret</a>(sender_id) -> <a href="./src/zavudev/types/webhook_secret_response.py">WebhookSecretResponse</a></code>
- <code title="patch /v1/senders/{senderId}/profile">client.senders.<a href="./src/zavudev/resources/senders.py">update_profile</a>(sender_id, \*\*<a href="src/zavudev/types/sender_update_profile_params.py">params</a>) -> <a href="./src/zavudev/types/sender_update_profile_response.py">SenderUpdateProfileResponse</a></code>
- <code title="post /v1/senders/{senderId}/profile/picture">client.senders.<a href="./src/zavudev/resources/senders.py">upload_profile_picture</a>(sender_id, \*\*<a href="src/zavudev/types/sender_upload_profile_picture_params.py">params</a>) -> <a href="./src/zavudev/types/sender_upload_profile_picture_response.py">SenderUploadProfilePictureResponse</a></code>

# Contacts

Types:

```python
from zavudev.types import Contact
```

Methods:

- <code title="get /v1/contacts/{contactId}">client.contacts.<a href="./src/zavudev/resources/contacts.py">retrieve</a>(contact_id) -> <a href="./src/zavudev/types/contact.py">Contact</a></code>
- <code title="patch /v1/contacts/{contactId}">client.contacts.<a href="./src/zavudev/resources/contacts.py">update</a>(contact_id, \*\*<a href="src/zavudev/types/contact_update_params.py">params</a>) -> <a href="./src/zavudev/types/contact.py">Contact</a></code>
- <code title="get /v1/contacts">client.contacts.<a href="./src/zavudev/resources/contacts.py">list</a>(\*\*<a href="src/zavudev/types/contact_list_params.py">params</a>) -> <a href="./src/zavudev/types/contact.py">SyncCursor[Contact]</a></code>
- <code title="get /v1/contacts/phone/{phoneNumber}">client.contacts.<a href="./src/zavudev/resources/contacts.py">retrieve_by_phone</a>(phone_number) -> <a href="./src/zavudev/types/contact.py">Contact</a></code>

# Broadcasts

Types:

```python
from zavudev.types import (
    Broadcast,
    BroadcastChannel,
    BroadcastContact,
    BroadcastContactStatus,
    BroadcastContent,
    BroadcastMessageType,
    BroadcastProgress,
    BroadcastStatus,
    BroadcastCreateResponse,
    BroadcastRetrieveResponse,
    BroadcastUpdateResponse,
    BroadcastCancelResponse,
    BroadcastSendResponse,
)
```

Methods:

- <code title="post /v1/broadcasts">client.broadcasts.<a href="./src/zavudev/resources/broadcasts/broadcasts.py">create</a>(\*\*<a href="src/zavudev/types/broadcast_create_params.py">params</a>) -> <a href="./src/zavudev/types/broadcast_create_response.py">BroadcastCreateResponse</a></code>
- <code title="get /v1/broadcasts/{broadcastId}">client.broadcasts.<a href="./src/zavudev/resources/broadcasts/broadcasts.py">retrieve</a>(broadcast_id) -> <a href="./src/zavudev/types/broadcast_retrieve_response.py">BroadcastRetrieveResponse</a></code>
- <code title="patch /v1/broadcasts/{broadcastId}">client.broadcasts.<a href="./src/zavudev/resources/broadcasts/broadcasts.py">update</a>(broadcast_id, \*\*<a href="src/zavudev/types/broadcast_update_params.py">params</a>) -> <a href="./src/zavudev/types/broadcast_update_response.py">BroadcastUpdateResponse</a></code>
- <code title="get /v1/broadcasts">client.broadcasts.<a href="./src/zavudev/resources/broadcasts/broadcasts.py">list</a>(\*\*<a href="src/zavudev/types/broadcast_list_params.py">params</a>) -> <a href="./src/zavudev/types/broadcast.py">SyncCursor[Broadcast]</a></code>
- <code title="delete /v1/broadcasts/{broadcastId}">client.broadcasts.<a href="./src/zavudev/resources/broadcasts/broadcasts.py">delete</a>(broadcast_id) -> None</code>
- <code title="post /v1/broadcasts/{broadcastId}/cancel">client.broadcasts.<a href="./src/zavudev/resources/broadcasts/broadcasts.py">cancel</a>(broadcast_id) -> <a href="./src/zavudev/types/broadcast_cancel_response.py">BroadcastCancelResponse</a></code>
- <code title="get /v1/broadcasts/{broadcastId}/progress">client.broadcasts.<a href="./src/zavudev/resources/broadcasts/broadcasts.py">progress</a>(broadcast_id) -> <a href="./src/zavudev/types/broadcast_progress.py">BroadcastProgress</a></code>
- <code title="post /v1/broadcasts/{broadcastId}/send">client.broadcasts.<a href="./src/zavudev/resources/broadcasts/broadcasts.py">send</a>(broadcast_id, \*\*<a href="src/zavudev/types/broadcast_send_params.py">params</a>) -> <a href="./src/zavudev/types/broadcast_send_response.py">BroadcastSendResponse</a></code>

## Contacts

Types:

```python
from zavudev.types.broadcasts import ContactAddResponse
```

Methods:

- <code title="get /v1/broadcasts/{broadcastId}/contacts">client.broadcasts.contacts.<a href="./src/zavudev/resources/broadcasts/contacts.py">list</a>(broadcast_id, \*\*<a href="src/zavudev/types/broadcasts/contact_list_params.py">params</a>) -> <a href="./src/zavudev/types/broadcast_contact.py">SyncCursor[BroadcastContact]</a></code>
- <code title="post /v1/broadcasts/{broadcastId}/contacts">client.broadcasts.contacts.<a href="./src/zavudev/resources/broadcasts/contacts.py">add</a>(broadcast_id, \*\*<a href="src/zavudev/types/broadcasts/contact_add_params.py">params</a>) -> <a href="./src/zavudev/types/broadcasts/contact_add_response.py">ContactAddResponse</a></code>
- <code title="delete /v1/broadcasts/{broadcastId}/contacts/{contactId}">client.broadcasts.contacts.<a href="./src/zavudev/resources/broadcasts/contacts.py">remove</a>(contact_id, \*, broadcast_id) -> None</code>

# Introspect

Types:

```python
from zavudev.types import LineType, IntrospectValidatePhoneResponse
```

Methods:

- <code title="post /v1/introspect/phone">client.introspect.<a href="./src/zavudev/resources/introspect.py">validate_phone</a>(\*\*<a href="src/zavudev/types/introspect_validate_phone_params.py">params</a>) -> <a href="./src/zavudev/types/introspect_validate_phone_response.py">IntrospectValidatePhoneResponse</a></code>

# PhoneNumbers

Types:

```python
from zavudev.types import (
    AvailablePhoneNumber,
    OwnedPhoneNumber,
    OwnedPhoneNumberPricing,
    PhoneNumberCapabilities,
    PhoneNumberPricing,
    PhoneNumberStatus,
    PhoneNumberType,
    PhoneNumberRetrieveResponse,
    PhoneNumberUpdateResponse,
    PhoneNumberPurchaseResponse,
    PhoneNumberSearchAvailableResponse,
)
```

Methods:

- <code title="get /v1/phone-numbers/{phoneNumberId}">client.phone_numbers.<a href="./src/zavudev/resources/phone_numbers.py">retrieve</a>(phone_number_id) -> <a href="./src/zavudev/types/phone_number_retrieve_response.py">PhoneNumberRetrieveResponse</a></code>
- <code title="patch /v1/phone-numbers/{phoneNumberId}">client.phone_numbers.<a href="./src/zavudev/resources/phone_numbers.py">update</a>(phone_number_id, \*\*<a href="src/zavudev/types/phone_number_update_params.py">params</a>) -> <a href="./src/zavudev/types/phone_number_update_response.py">PhoneNumberUpdateResponse</a></code>
- <code title="get /v1/phone-numbers">client.phone_numbers.<a href="./src/zavudev/resources/phone_numbers.py">list</a>(\*\*<a href="src/zavudev/types/phone_number_list_params.py">params</a>) -> <a href="./src/zavudev/types/owned_phone_number.py">SyncCursor[OwnedPhoneNumber]</a></code>
- <code title="post /v1/phone-numbers">client.phone_numbers.<a href="./src/zavudev/resources/phone_numbers.py">purchase</a>(\*\*<a href="src/zavudev/types/phone_number_purchase_params.py">params</a>) -> <a href="./src/zavudev/types/phone_number_purchase_response.py">PhoneNumberPurchaseResponse</a></code>
- <code title="delete /v1/phone-numbers/{phoneNumberId}">client.phone_numbers.<a href="./src/zavudev/resources/phone_numbers.py">release</a>(phone_number_id) -> None</code>
- <code title="get /v1/phone-numbers/available">client.phone_numbers.<a href="./src/zavudev/resources/phone_numbers.py">search_available</a>(\*\*<a href="src/zavudev/types/phone_number_search_available_params.py">params</a>) -> <a href="./src/zavudev/types/phone_number_search_available_response.py">PhoneNumberSearchAvailableResponse</a></code>
