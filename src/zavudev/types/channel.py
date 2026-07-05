# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["Channel"]

Channel: TypeAlias = Literal[
    "auto", "sms", "sms_oneway", "whatsapp", "whatsapp_alt", "telegram", "email", "instagram", "messenger", "voice"
]
