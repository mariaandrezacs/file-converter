"""HTTP routes for PNG to WebP conversion."""

from typing import Annotated

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from src.png_to_webp.services.conversion_service import ConversionService

router = APIRouter()

PNG_FILE = File(...)


def get_conversion_service() -> ConversionService:
    """Provide a ConversionService instance."""
    return ConversionService()


@router.post("/convert/png-to-webp")
async def convert_png_to_webp(
    file: Annotated[UploadFile, PNG_FILE],
    service: ConversionService = Depends(get_conversion_service),
):
    """Handle PNG to WebP conversion request."""
    if not file.filename.lower().endswith(".png"):
        raise HTTPException(status_code=400, detail="Arquivo deve ser PNG")

    try:
        return service.convert_png_to_webp(
            file.file,
            options={},
        )
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
