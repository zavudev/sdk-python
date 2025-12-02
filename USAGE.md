<!-- Start SDK Example Usage [usage] -->
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