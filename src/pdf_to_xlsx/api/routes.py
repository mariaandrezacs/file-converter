"""HTTP routes for PDF to XLSX conversion."""

from typing import Annotated

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from src.pdf_to_xlsx.services.conversion_service import ConversionService

router = APIRouter()

PDF_FILE = File(...)


def get_conversion_service() -> ConversionService:
    """Provide a ConversionService instance."""
    return ConversionService()


@router.post("/convert/pdf-to-xlsx")
async def convert_pdf_to_xlsx(
    file: Annotated[UploadFile, PDF_FILE],
    service: ConversionService = Depends(get_conversion_service),
):
    """Handle PDF to XLSX conversion request."""
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Arquivo deve ser PDF")

    try:
        return service.convert_pdf_to_xlsx(
            file.file,
            options={},
        )
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
