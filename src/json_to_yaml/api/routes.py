"""HTTP routes for JSON to YAML conversion."""

from typing import Annotated

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from src.json_to_yaml.services.conversion_service import ConversionService

router = APIRouter()

JSON_FILE = File(...)


def get_conversion_service() -> ConversionService:
    """Provide a ConversionService instance."""
    return ConversionService()


@router.post("/convert/json-to-yaml")
async def convert_json_to_yaml(
    file: Annotated[UploadFile, JSON_FILE],
    encoding: str = "utf-8",
    service: ConversionService = Depends(get_conversion_service),
):
    """Handle JSON to YAML conversion request."""
    if not file.filename.lower().endswith(".json"):
        raise HTTPException(status_code=400, detail="Arquivo deve ser JSON")

    try:
        return service.convert_json_to_yaml(
            file.file,
            options={
                "encoding": encoding,
            },
        )
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
