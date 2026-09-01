"""HTTP routes for Word to PDF conversion."""

from typing import Annotated

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from src.word_to_pdf.services.conversion_service import ConversionService

router = APIRouter()

WORD_FILE = File(...)


def get_conversion_service() -> ConversionService:
    """Provide a ConversionService instance."""
    return ConversionService()


@router.post("/convert/word-to-pdf")
async def convert_word_to_pdf(
    file: Annotated[UploadFile, WORD_FILE],
    service: ConversionService = Depends(get_conversion_service),
):
    """Handle Word to PDF conversion request."""
    if not file.filename.lower().endswith((".docx", ".doc")):
        raise HTTPException(status_code=400, detail="Arquivo deve ser Word")

    try:
        return service.convert_word_to_pdf(
            file.file,
            options={},
        )
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
