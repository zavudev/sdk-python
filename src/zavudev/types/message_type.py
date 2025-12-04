# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["MessageType"]

MessageType: TypeAlias = Literal[
    "text",
    "image",
    "video",
    "audio",
    "document",
    "sticker",
    "location",
    "contact",
    "buttons",
    "list",
    "reaction",
    "template",
]
