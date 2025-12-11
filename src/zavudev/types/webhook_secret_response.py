# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["WebhookSecretResponse"]


class WebhookSecretResponse(BaseModel):
    secret: str
    """The new webhook secret."""
