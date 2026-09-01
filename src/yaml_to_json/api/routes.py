"""HTTP routes for YAML to JSON conversion."""

from typing import Annotated

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from src.yaml_to_json.services.conversion_service import ConversionService

router = APIRouter()

YAML_FILE = File(...)


def get_conversion_service() -> ConversionService:
    """Provide a ConversionService instance."""
    return ConversionService()


@router.post("/convert/yaml-to-json")
async def convert_yaml_to_json(
    file: Annotated[UploadFile, YAML_FILE],
    encoding: str = "utf-8",
    service: ConversionService = Depends(get_conversion_service),
):
    """Handle YAML to JSON conversion request."""
    if not file.filename.lower().endswith((".yaml", ".yml")):
        raise HTTPException(status_code=400, detail="Arquivo deve ser YAML")

    try:
        return service.convert_yaml_to_json(
            file.file,
            options={
                "encoding": encoding,
            },
        )
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
