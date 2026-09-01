"""HTTP routes for JPG to WebP conversion."""

from typing import Annotated

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from src.jpg_to_webp.services.conversion_service import ConversionService

router = APIRouter()

JPG_FILE = File(...)


def get_conversion_service() -> ConversionService:
    """Provide a ConversionService instance."""
    return ConversionService()


@router.post("/convert/jpg-to-webp")
async def convert_jpg_to_webp(
    file: Annotated[UploadFile, JPG_FILE],
    service: ConversionService = Depends(get_conversion_service),
):
    """Handle JPG to WebP conversion request."""
    if not file.filename.lower().endswith((".jpg", ".jpeg")):
        raise HTTPException(status_code=400, detail="Arquivo deve ser JPG")

    try:
        return service.convert_jpg_to_webp(
            file.file,
            options={},
        )
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
