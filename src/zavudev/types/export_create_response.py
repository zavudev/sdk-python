# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .data_export import DataExport

__all__ = ["ExportCreateResponse"]


class ExportCreateResponse(BaseModel):
    export: DataExport
