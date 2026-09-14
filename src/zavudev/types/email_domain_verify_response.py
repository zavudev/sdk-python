# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EmailDomainVerifyResponse", "Domain", "DomainDNSRecord"]


class DomainDNSRecord(BaseModel):
    name: str
    """Record host/name to create."""

    purpose: Literal["dkim", "spf", "dmarc", "mail_from"]
    """What the record is for."""

    required: bool
    """
    Whether the record is required to verify + send (DKIM) or recommended for
    deliverability.
    """

    type: str
    """DNS record type."""

    value: str
    """Record value."""

    priority: Optional[int] = None
    """Priority (MX records only)."""


class Domain(BaseModel):
    id: str

    dkim_status: str = FieldInfo(alias="dkimStatus")

    domain: str

    status: str
    """Overall verification status."""

    dns_records: Optional[List[DomainDNSRecord]] = FieldInfo(alias="dnsRecords", default=None)
    """DNS records to publish.

    Present when fetching a single domain or after adding one.
    """


class EmailDomainVerifyResponse(BaseModel):
    domain: Domain
