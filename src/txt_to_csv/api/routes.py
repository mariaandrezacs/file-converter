"""HTTP routes for TXT to CSV conversion."""

from typing import Annotated

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from src.txt_to_csv.services.conversion_service import ConversionService

router = APIRouter()

TXT_FILE = File(...)


def get_conversion_service() -> ConversionService:
    """Provide a ConversionService instance."""
    return ConversionService()


@router.post("/convert/txt-to-csv")
async def convert_txt_to_csv(
    file: Annotated[UploadFile, TXT_FILE],
    delimiter: str = "\t",
    encoding: str = "utf-8",
    has_header: bool = False,
    service: ConversionService = Depends(get_conversion_service),
):
    """Handle TXT to CSV conversion request."""
    if not file.filename.lower().endswith(".txt"):
        raise HTTPException(status_code=400, detail="Arquivo deve ser TXT")

    try:
        return service.convert_txt_to_csv(
            file.file,
            options={
                "delimiter": delimiter,
                "encoding": encoding,
                "has_header": has_header,
            },
        )
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
