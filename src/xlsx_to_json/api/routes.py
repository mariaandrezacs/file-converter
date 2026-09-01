"""HTTP routes for XLSX to JSON conversion."""

from typing import Annotated

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from src.xlsx_to_json.services.conversion_service import ConversionService

router = APIRouter()

XLSX_FILE = File(...)


def get_conversion_service() -> ConversionService:
    """Provide a ConversionService instance."""
    return ConversionService()


@router.post("/convert/xlsx-to-json")
async def convert_xlsx_to_json(
    file: Annotated[UploadFile, XLSX_FILE],
    service: ConversionService = Depends(get_conversion_service),
):
    """Handle XLSX to JSON conversion request."""
    if not file.filename.lower().endswith(".xlsx"):
        raise HTTPException(status_code=400, detail="Arquivo deve ser XLSX")

    try:
        return service.convert_xlsx_to_json(
            file.file,
            options={},
        )
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
