"""HTTP routes for CSV to XLSX conversion."""

from typing import Annotated

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from src.csv_to_xlsx.services.conversion_service import ConversionService

router = APIRouter()

CSV_FILE = File(...)


def get_conversion_service() -> ConversionService:
    """Provide a ConversionService instance."""
    return ConversionService()


@router.post("/convert/csv-to-xlsx")
async def convert_csv_to_xlsx(
    file: Annotated[UploadFile, CSV_FILE],
    delimiter: str = ",",
    encoding: str = "utf-8",
    service: ConversionService = Depends(get_conversion_service),
):
    """Handle CSV to XLSX conversion request."""
    if not file.filename.lower().endswith(".csv"):
        raise HTTPException(status_code=400, detail="Arquivo deve ser CSV")

    try:
        return service.convert_csv_to_xlsx(
            file.file,
            options={
                "delimiter": delimiter,
                "encoding": encoding,
            },
        )
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
