# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .data_export import DataExport

__all__ = ["ExportRetrieveResponse"]


class ExportRetrieveResponse(BaseModel):
    export: DataExport
