"""HTTP routes for JSON to XML conversion."""

from typing import Annotated

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from src.json_to_xml.services.conversion_service import ConversionService

router = APIRouter()

JSON_FILE = File(...)


def get_conversion_service() -> ConversionService:
    """Provide a ConversionService instance."""
    return ConversionService()


@router.post("/convert/json-to-xml")
async def convert_json_to_xml(
    file: Annotated[UploadFile, JSON_FILE],
    encoding: str = "utf-8",
    service: ConversionService = Depends(get_conversion_service),
):
    """Handle JSON to XML conversion request."""
    if not file.filename.lower().endswith(".json"):
        raise HTTPException(status_code=400, detail="Arquivo deve ser JSON")

    try:
        return service.convert_json_to_xml(
            file.file,
            options={
                "encoding": encoding,
            },
        )
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
