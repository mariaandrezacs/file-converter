"""HTTP routes for Base64 to File conversion."""

from typing import Annotated

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile

from src.base64_to_file.services.conversion_service import ConversionService

router = APIRouter()

PLACEHOLDER_FILE = File(None)


def get_conversion_service() -> ConversionService:
    """Provide a ConversionService instance."""
    return ConversionService()


@router.post("/convert/base64-to-file")
async def convert_base64_to_file(
    content: Annotated[str, Form()],
    filename: Annotated[str, Form()],
    file: Annotated[UploadFile | None, PLACEHOLDER_FILE] = None,
    service: ConversionService = Depends(get_conversion_service),
):
    """Handle Base64 to File conversion request."""
    try:
        return service.convert_base64_to_file(
            file,
            options={
                "content": content,
                "filename": filename,
            },
        )
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
