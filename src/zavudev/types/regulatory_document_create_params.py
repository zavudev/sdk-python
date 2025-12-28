# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RegulatoryDocumentCreateParams"]


class RegulatoryDocumentCreateParams(TypedDict, total=False):
    document_type: Required[
        Annotated[
            Literal[
                "passport",
                "national_id",
                "drivers_license",
                "utility_bill",
                "tax_id",
                "business_registration",
                "proof_of_address",
                "other",
            ],
            PropertyInfo(alias="documentType"),
        ]
    ]

    file_size: Required[Annotated[int, PropertyInfo(alias="fileSize")]]

    mime_type: Required[Annotated[str, PropertyInfo(alias="mimeType")]]

    name: Required[str]

    storage_id: Required[Annotated[str, PropertyInfo(alias="storageId")]]
    """Storage ID from the upload-url endpoint."""
