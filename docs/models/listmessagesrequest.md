# ListMessagesRequest


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `status`                                                     | [Optional[models.MessageStatus]](../models/messagestatus.md) | :heavy_minus_sign:                                           | N/A                                                          |
| `to`                                                         | *Optional[str]*                                              | :heavy_minus_sign:                                           | N/A                                                          |
| `channel`                                                    | [Optional[models.Channel]](../models/channel.md)             | :heavy_minus_sign:                                           | Delivery channel.                                            |
| `limit`                                                      | *Optional[int]*                                              | :heavy_minus_sign:                                           | N/A                                                          |
| `cursor`                                                     | *Optional[str]*                                              | :heavy_minus_sign:                                           | N/A                                                          |