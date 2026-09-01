"""HTTP routes for WebP to PNG conversion."""

from typing import Annotated

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from src.webp_to_png.services.conversion_service import ConversionService

router = APIRouter()

WEBP_FILE = File(...)


def get_conversion_service() -> ConversionService:
    """Provide a ConversionService instance."""
    return ConversionService()


@router.post("/convert/webp-to-png")
async def convert_webp_to_png(
    file: Annotated[UploadFile, WEBP_FILE],
    service: ConversionService = Depends(get_conversion_service),
):
    """Handle WebP to PNG conversion request."""
    if not file.filename.lower().endswith(".webp"):
        raise HTTPException(status_code=400, detail="Arquivo deve ser WebP")

    try:
        return service.convert_webp_to_png(
            file.file,
            options={},
        )
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
