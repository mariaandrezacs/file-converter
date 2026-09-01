"""HTTP routes for File to Base64 conversion."""

from typing import Annotated

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from src.file_to_base64.services.conversion_service import ConversionService

router = APIRouter()

ANY_FILE = File(...)


def get_conversion_service() -> ConversionService:
    """Provide a ConversionService instance."""
    return ConversionService()


@router.post("/convert/file-to-base64")
async def convert_file_to_base64(
    file: Annotated[UploadFile, ANY_FILE],
    service: ConversionService = Depends(get_conversion_service),
):
    """Handle File to Base64 conversion request."""
    try:
        return service.convert_file_to_base64(
            file.file,
            options={},
        )
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
