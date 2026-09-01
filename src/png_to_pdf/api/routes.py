"""HTTP routes for PNG to PDF conversion."""

from typing import Annotated

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from src.png_to_pdf.services.conversion_service import ConversionService

router = APIRouter()

PNG_FILE = File(...)


def get_conversion_service() -> ConversionService:
    """Provide a ConversionService instance."""
    return ConversionService()


@router.post("/convert/png-to-pdf")
async def convert_png_to_pdf(
    file: Annotated[UploadFile, PNG_FILE],
    service: ConversionService = Depends(get_conversion_service),
):
    """Handle PNG to PDF conversion request."""
    if not file.filename.lower().endswith(".png"):
        raise HTTPException(status_code=400, detail="Arquivo deve ser PNG")

    try:
        return service.convert_png_to_pdf(
            file.file,
            options={},
        )
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
