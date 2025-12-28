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

- <code title="post /v1/senders">client.senders.<a href="./src/zavudev/resources/senders/senders.py">create</a>(\*\*<a href="src/zavudev/types/sender_create_params.py">params</a>) -> <a href="./src/zavudev/types/sender.py">Sender</a></code>
- <code title="get /v1/senders/{senderId}">client.senders.<a href="./src/zavudev/resources/senders/senders.py">retrieve</a>(sender_id) -> <a href="./src/zavudev/types/sender.py">Sender</a></code>
- <code title="patch /v1/senders/{senderId}">client.senders.<a href="./src/zavudev/resources/senders/senders.py">update</a>(sender_id, \*\*<a href="src/zavudev/types/sender_update_params.py">params</a>) -> <a href="./src/zavudev/types/sender.py">Sender</a></code>
- <code title="get /v1/senders">client.senders.<a href="./src/zavudev/resources/senders/senders.py">list</a>(\*\*<a href="src/zavudev/types/sender_list_params.py">params</a>) -> <a href="./src/zavudev/types/sender.py">SyncCursor[Sender]</a></code>
- <code title="delete /v1/senders/{senderId}">client.senders.<a href="./src/zavudev/resources/senders/senders.py">delete</a>(sender_id) -> None</code>
- <code title="get /v1/senders/{senderId}/profile">client.senders.<a href="./src/zavudev/resources/senders/senders.py">get_profile</a>(sender_id) -> <a href="./src/zavudev/types/whatsapp_business_profile_response.py">WhatsappBusinessProfileResponse</a></code>
- <code title="post /v1/senders/{senderId}/webhook/secret">client.senders.<a href="./src/zavudev/resources/senders/senders.py">regenerate_webhook_secret</a>(sender_id) -> <a href="./src/zavudev/types/webhook_secret_response.py">WebhookSecretResponse</a></code>
- <code title="patch /v1/senders/{senderId}/profile">client.senders.<a href="./src/zavudev/resources/senders/senders.py">update_profile</a>(sender_id, \*\*<a href="src/zavudev/types/sender_update_profile_params.py">params</a>) -> <a href="./src/zavudev/types/sender_update_profile_response.py">SenderUpdateProfileResponse</a></code>
- <code title="post /v1/senders/{senderId}/profile/picture">client.senders.<a href="./src/zavudev/resources/senders/senders.py">upload_profile_picture</a>(sender_id, \*\*<a href="src/zavudev/types/sender_upload_profile_picture_params.py">params</a>) -> <a href="./src/zavudev/types/sender_upload_profile_picture_response.py">SenderUploadProfilePictureResponse</a></code>

## Agent

Types:

```python
from zavudev.types.senders import (
    Agent,
    AgentExecution,
    AgentExecutionStatus,
    AgentProvider,
    AgentResponse,
    AgentStats,
)
```

Methods:

- <code title="post /v1/senders/{senderId}/agent">client.senders.agent.<a href="./src/zavudev/resources/senders/agent/agent.py">create</a>(sender_id, \*\*<a href="src/zavudev/types/senders/agent_create_params.py">params</a>) -> <a href="./src/zavudev/types/senders/agent_response.py">AgentResponse</a></code>
- <code title="get /v1/senders/{senderId}/agent">client.senders.agent.<a href="./src/zavudev/resources/senders/agent/agent.py">retrieve</a>(sender_id) -> <a href="./src/zavudev/types/senders/agent_response.py">AgentResponse</a></code>
- <code title="patch /v1/senders/{senderId}/agent">client.senders.agent.<a href="./src/zavudev/resources/senders/agent/agent.py">update</a>(sender_id, \*\*<a href="src/zavudev/types/senders/agent_update_params.py">params</a>) -> <a href="./src/zavudev/types/senders/agent_response.py">AgentResponse</a></code>
- <code title="delete /v1/senders/{senderId}/agent">client.senders.agent.<a href="./src/zavudev/resources/senders/agent/agent.py">delete</a>(sender_id) -> None</code>
- <code title="get /v1/senders/{senderId}/agent/stats">client.senders.agent.<a href="./src/zavudev/resources/senders/agent/agent.py">stats</a>(sender_id) -> <a href="./src/zavudev/types/senders/agent_stats.py">AgentStats</a></code>

### Executions

Methods:

- <code title="get /v1/senders/{senderId}/agent/executions">client.senders.agent.executions.<a href="./src/zavudev/resources/senders/agent/executions.py">list</a>(sender_id, \*\*<a href="src/zavudev/types/senders/agent/execution_list_params.py">params</a>) -> <a href="./src/zavudev/types/senders/agent_execution.py">SyncCursor[AgentExecution]</a></code>

### Flows

Types:

```python
from zavudev.types.senders.agent import (
    AgentFlow,
    FlowCreateResponse,
    FlowRetrieveResponse,
    FlowUpdateResponse,
    FlowDuplicateResponse,
)
```

Methods:

- <code title="post /v1/senders/{senderId}/agent/flows">client.senders.agent.flows.<a href="./src/zavudev/resources/senders/agent/flows.py">create</a>(sender_id, \*\*<a href="src/zavudev/types/senders/agent/flow_create_params.py">params</a>) -> <a href="./src/zavudev/types/senders/agent/flow_create_response.py">FlowCreateResponse</a></code>
- <code title="get /v1/senders/{senderId}/agent/flows/{flowId}">client.senders.agent.flows.<a href="./src/zavudev/resources/senders/agent/flows.py">retrieve</a>(flow_id, \*, sender_id) -> <a href="./src/zavudev/types/senders/agent/flow_retrieve_response.py">FlowRetrieveResponse</a></code>
- <code title="patch /v1/senders/{senderId}/agent/flows/{flowId}">client.senders.agent.flows.<a href="./src/zavudev/resources/senders/agent/flows.py">update</a>(flow_id, \*, sender_id, \*\*<a href="src/zavudev/types/senders/agent/flow_update_params.py">params</a>) -> <a href="./src/zavudev/types/senders/agent/flow_update_response.py">FlowUpdateResponse</a></code>
- <code title="get /v1/senders/{senderId}/agent/flows">client.senders.agent.flows.<a href="./src/zavudev/resources/senders/agent/flows.py">list</a>(sender_id, \*\*<a href="src/zavudev/types/senders/agent/flow_list_params.py">params</a>) -> <a href="./src/zavudev/types/senders/agent/agent_flow.py">SyncCursor[AgentFlow]</a></code>
- <code title="delete /v1/senders/{senderId}/agent/flows/{flowId}">client.senders.agent.flows.<a href="./src/zavudev/resources/senders/agent/flows.py">delete</a>(flow_id, \*, sender_id) -> None</code>
- <code title="post /v1/senders/{senderId}/agent/flows/{flowId}/duplicate">client.senders.agent.flows.<a href="./src/zavudev/resources/senders/agent/flows.py">duplicate</a>(flow_id, \*, sender_id, \*\*<a href="src/zavudev/types/senders/agent/flow_duplicate_params.py">params</a>) -> <a href="./src/zavudev/types/senders/agent/flow_duplicate_response.py">FlowDuplicateResponse</a></code>

### Tools

Types:

```python
from zavudev.types.senders.agent import (
    AgentTool,
    ToolCreateResponse,
    ToolRetrieveResponse,
    ToolUpdateResponse,
    ToolTestResponse,
)
```

Methods:

- <code title="post /v1/senders/{senderId}/agent/tools">client.senders.agent.tools.<a href="./src/zavudev/resources/senders/agent/tools.py">create</a>(sender_id, \*\*<a href="src/zavudev/types/senders/agent/tool_create_params.py">params</a>) -> <a href="./src/zavudev/types/senders/agent/tool_create_response.py">ToolCreateResponse</a></code>
- <code title="get /v1/senders/{senderId}/agent/tools/{toolId}">client.senders.agent.tools.<a href="./src/zavudev/resources/senders/agent/tools.py">retrieve</a>(tool_id, \*, sender_id) -> <a href="./src/zavudev/types/senders/agent/tool_retrieve_response.py">ToolRetrieveResponse</a></code>
- <code title="patch /v1/senders/{senderId}/agent/tools/{toolId}">client.senders.agent.tools.<a href="./src/zavudev/resources/senders/agent/tools.py">update</a>(tool_id, \*, sender_id, \*\*<a href="src/zavudev/types/senders/agent/tool_update_params.py">params</a>) -> <a href="./src/zavudev/types/senders/agent/tool_update_response.py">ToolUpdateResponse</a></code>
- <code title="get /v1/senders/{senderId}/agent/tools">client.senders.agent.tools.<a href="./src/zavudev/resources/senders/agent/tools.py">list</a>(sender_id, \*\*<a href="src/zavudev/types/senders/agent/tool_list_params.py">params</a>) -> <a href="./src/zavudev/types/senders/agent/agent_tool.py">SyncCursor[AgentTool]</a></code>
- <code title="delete /v1/senders/{senderId}/agent/tools/{toolId}">client.senders.agent.tools.<a href="./src/zavudev/resources/senders/agent/tools.py">delete</a>(tool_id, \*, sender_id) -> None</code>
- <code title="post /v1/senders/{senderId}/agent/tools/{toolId}/test">client.senders.agent.tools.<a href="./src/zavudev/resources/senders/agent/tools.py">test</a>(tool_id, \*, sender_id, \*\*<a href="src/zavudev/types/senders/agent/tool_test_params.py">params</a>) -> <a href="./src/zavudev/types/senders/agent/tool_test_response.py">ToolTestResponse</a></code>

### KnowledgeBases

Types:

```python
from zavudev.types.senders.agent import (
    AgentDocument,
    AgentKnowledgeBase,
    KnowledgeBaseCreateResponse,
    KnowledgeBaseRetrieveResponse,
    KnowledgeBaseUpdateResponse,
)
```

Methods:

- <code title="post /v1/senders/{senderId}/agent/knowledge-bases">client.senders.agent.knowledge_bases.<a href="./src/zavudev/resources/senders/agent/knowledge_bases/knowledge_bases.py">create</a>(sender_id, \*\*<a href="src/zavudev/types/senders/agent/knowledge_base_create_params.py">params</a>) -> <a href="./src/zavudev/types/senders/agent/knowledge_base_create_response.py">KnowledgeBaseCreateResponse</a></code>
- <code title="get /v1/senders/{senderId}/agent/knowledge-bases/{kbId}">client.senders.agent.knowledge_bases.<a href="./src/zavudev/resources/senders/agent/knowledge_bases/knowledge_bases.py">retrieve</a>(kb_id, \*, sender_id) -> <a href="./src/zavudev/types/senders/agent/knowledge_base_retrieve_response.py">KnowledgeBaseRetrieveResponse</a></code>
- <code title="patch /v1/senders/{senderId}/agent/knowledge-bases/{kbId}">client.senders.agent.knowledge_bases.<a href="./src/zavudev/resources/senders/agent/knowledge_bases/knowledge_bases.py">update</a>(kb_id, \*, sender_id, \*\*<a href="src/zavudev/types/senders/agent/knowledge_base_update_params.py">params</a>) -> <a href="./src/zavudev/types/senders/agent/knowledge_base_update_response.py">KnowledgeBaseUpdateResponse</a></code>
- <code title="get /v1/senders/{senderId}/agent/knowledge-bases">client.senders.agent.knowledge_bases.<a href="./src/zavudev/resources/senders/agent/knowledge_bases/knowledge_bases.py">list</a>(sender_id, \*\*<a href="src/zavudev/types/senders/agent/knowledge_base_list_params.py">params</a>) -> <a href="./src/zavudev/types/senders/agent/agent_knowledge_base.py">SyncCursor[AgentKnowledgeBase]</a></code>
- <code title="delete /v1/senders/{senderId}/agent/knowledge-bases/{kbId}">client.senders.agent.knowledge_bases.<a href="./src/zavudev/resources/senders/agent/knowledge_bases/knowledge_bases.py">delete</a>(kb_id, \*, sender_id) -> None</code>

#### Documents

Types:

```python
from zavudev.types.senders.agent.knowledge_bases import DocumentCreateResponse
```

Methods:

- <code title="post /v1/senders/{senderId}/agent/knowledge-bases/{kbId}/documents">client.senders.agent.knowledge_bases.documents.<a href="./src/zavudev/resources/senders/agent/knowledge_bases/documents.py">create</a>(kb_id, \*, sender_id, \*\*<a href="src/zavudev/types/senders/agent/knowledge_bases/document_create_params.py">params</a>) -> <a href="./src/zavudev/types/senders/agent/knowledge_bases/document_create_response.py">DocumentCreateResponse</a></code>
- <code title="get /v1/senders/{senderId}/agent/knowledge-bases/{kbId}/documents">client.senders.agent.knowledge_bases.documents.<a href="./src/zavudev/resources/senders/agent/knowledge_bases/documents.py">list</a>(kb_id, \*, sender_id, \*\*<a href="src/zavudev/types/senders/agent/knowledge_bases/document_list_params.py">params</a>) -> <a href="./src/zavudev/types/senders/agent/agent_document.py">SyncCursor[AgentDocument]</a></code>
- <code title="delete /v1/senders/{senderId}/agent/knowledge-bases/{kbId}/documents/{docId}">client.senders.agent.knowledge_bases.documents.<a href="./src/zavudev/resources/senders/agent/knowledge_bases/documents.py">delete</a>(doc_id, \*, sender_id, kb_id) -> None</code>

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
    BroadcastRescheduleResponse,
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
- <code title="patch /v1/broadcasts/{broadcastId}/schedule">client.broadcasts.<a href="./src/zavudev/resources/broadcasts/broadcasts.py">reschedule</a>(broadcast_id, \*\*<a href="src/zavudev/types/broadcast_reschedule_params.py">params</a>) -> <a href="./src/zavudev/types/broadcast_reschedule_response.py">BroadcastRescheduleResponse</a></code>
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
    Requirement,
    RequirementAcceptanceCriteria,
    RequirementFieldType,
    RequirementType,
    PhoneNumberRetrieveResponse,
    PhoneNumberUpdateResponse,
    PhoneNumberPurchaseResponse,
    PhoneNumberRequirementsResponse,
    PhoneNumberSearchAvailableResponse,
)
```

Methods:

- <code title="get /v1/phone-numbers/{phoneNumberId}">client.phone_numbers.<a href="./src/zavudev/resources/phone_numbers.py">retrieve</a>(phone_number_id) -> <a href="./src/zavudev/types/phone_number_retrieve_response.py">PhoneNumberRetrieveResponse</a></code>
- <code title="patch /v1/phone-numbers/{phoneNumberId}">client.phone_numbers.<a href="./src/zavudev/resources/phone_numbers.py">update</a>(phone_number_id, \*\*<a href="src/zavudev/types/phone_number_update_params.py">params</a>) -> <a href="./src/zavudev/types/phone_number_update_response.py">PhoneNumberUpdateResponse</a></code>
- <code title="get /v1/phone-numbers">client.phone_numbers.<a href="./src/zavudev/resources/phone_numbers.py">list</a>(\*\*<a href="src/zavudev/types/phone_number_list_params.py">params</a>) -> <a href="./src/zavudev/types/owned_phone_number.py">SyncCursor[OwnedPhoneNumber]</a></code>
- <code title="post /v1/phone-numbers">client.phone_numbers.<a href="./src/zavudev/resources/phone_numbers.py">purchase</a>(\*\*<a href="src/zavudev/types/phone_number_purchase_params.py">params</a>) -> <a href="./src/zavudev/types/phone_number_purchase_response.py">PhoneNumberPurchaseResponse</a></code>
- <code title="delete /v1/phone-numbers/{phoneNumberId}">client.phone_numbers.<a href="./src/zavudev/resources/phone_numbers.py">release</a>(phone_number_id) -> None</code>
- <code title="get /v1/phone-numbers/requirements">client.phone_numbers.<a href="./src/zavudev/resources/phone_numbers.py">requirements</a>(\*\*<a href="src/zavudev/types/phone_number_requirements_params.py">params</a>) -> <a href="./src/zavudev/types/phone_number_requirements_response.py">PhoneNumberRequirementsResponse</a></code>
- <code title="get /v1/phone-numbers/available">client.phone_numbers.<a href="./src/zavudev/resources/phone_numbers.py">search_available</a>(\*\*<a href="src/zavudev/types/phone_number_search_available_params.py">params</a>) -> <a href="./src/zavudev/types/phone_number_search_available_response.py">PhoneNumberSearchAvailableResponse</a></code>

# Addresses

Types:

```python
from zavudev.types import Address, AddressStatus, AddressCreateResponse, AddressRetrieveResponse
```

Methods:

- <code title="post /v1/addresses">client.addresses.<a href="./src/zavudev/resources/addresses.py">create</a>(\*\*<a href="src/zavudev/types/address_create_params.py">params</a>) -> <a href="./src/zavudev/types/address_create_response.py">AddressCreateResponse</a></code>
- <code title="get /v1/addresses/{addressId}">client.addresses.<a href="./src/zavudev/resources/addresses.py">retrieve</a>(address_id) -> <a href="./src/zavudev/types/address_retrieve_response.py">AddressRetrieveResponse</a></code>
- <code title="get /v1/addresses">client.addresses.<a href="./src/zavudev/resources/addresses.py">list</a>(\*\*<a href="src/zavudev/types/address_list_params.py">params</a>) -> <a href="./src/zavudev/types/address.py">SyncCursor[Address]</a></code>
- <code title="delete /v1/addresses/{addressId}">client.addresses.<a href="./src/zavudev/resources/addresses.py">delete</a>(address_id) -> None</code>

# RegulatoryDocuments

Types:

```python
from zavudev.types import (
    RegulatoryDocument,
    RegulatoryDocumentCreateResponse,
    RegulatoryDocumentRetrieveResponse,
    RegulatoryDocumentUploadURLResponse,
)
```

Methods:

- <code title="post /v1/documents">client.regulatory_documents.<a href="./src/zavudev/resources/regulatory_documents.py">create</a>(\*\*<a href="src/zavudev/types/regulatory_document_create_params.py">params</a>) -> <a href="./src/zavudev/types/regulatory_document_create_response.py">RegulatoryDocumentCreateResponse</a></code>
- <code title="get /v1/documents/{documentId}">client.regulatory_documents.<a href="./src/zavudev/resources/regulatory_documents.py">retrieve</a>(document_id) -> <a href="./src/zavudev/types/regulatory_document_retrieve_response.py">RegulatoryDocumentRetrieveResponse</a></code>
- <code title="get /v1/documents">client.regulatory_documents.<a href="./src/zavudev/resources/regulatory_documents.py">list</a>(\*\*<a href="src/zavudev/types/regulatory_document_list_params.py">params</a>) -> <a href="./src/zavudev/types/regulatory_document.py">SyncCursor[RegulatoryDocument]</a></code>
- <code title="delete /v1/documents/{documentId}">client.regulatory_documents.<a href="./src/zavudev/resources/regulatory_documents.py">delete</a>(document_id) -> None</code>
- <code title="post /v1/documents/upload-url">client.regulatory_documents.<a href="./src/zavudev/resources/regulatory_documents.py">upload_url</a>() -> <a href="./src/zavudev/types/regulatory_document_upload_url_response.py">RegulatoryDocumentUploadURLResponse</a></code>
