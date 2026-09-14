# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["IntrospectValidateEmailResponse", "Result", "Summary"]


class Result(BaseModel):
    domain: Optional[str] = None
    """Domain part of the address. Null when the syntax is invalid."""

    email: str
    """The address exactly as submitted."""

    normalized: Optional[str] = None
    """Lowercased, trimmed form of the address. Null when the syntax is invalid."""

    reasons: List[
        Literal[
            "invalid_syntax",
            "domain_not_found",
            "domain_no_mx",
            "disposable_domain",
            "role_address",
            "suppressed_hard_bounce",
            "suppressed_soft_bounce",
            "suppressed_complaint",
            "suppressed_manual",
            "suppressed_unsubscribe",
        ]
    ]
    """Signals behind the verdict. Empty for a clean `deliverable` address."""

    verdict: Literal["deliverable", "risky", "undeliverable"]
    """Validation verdict.

    - `deliverable`: nothing suggests the address will bounce.
    - `risky`: sendable, but a signal predicts elevated bounce/complaint odds (role
      address, disposable domain, MX-less domain, prior soft bounce).
    - `undeliverable`: will bounce or is blocked (invalid syntax, dead domain, or
      the address is on your suppression list after a hard bounce/complaint).
    """


class Summary(BaseModel):
    deliverable: int

    risky: int

    total: int

    undeliverable: int


class IntrospectValidateEmailResponse(BaseModel):
    results: List[Result]
    """One result per submitted address, in the same order."""

    summary: Summary
