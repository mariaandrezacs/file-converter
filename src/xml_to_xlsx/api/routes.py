"""HTTP routes for XML to XLSX conversion."""

from typing import Annotated

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from src.xml_to_xlsx.services.conversion_service import ConversionService

router = APIRouter()

XML_FILE = File(...)


def get_conversion_service() -> ConversionService:
    """Provide a ConversionService instance."""
    return ConversionService()


@router.post("/convert/xml-to-xlsx")
async def convert_xml_to_xlsx(
    file: Annotated[UploadFile, XML_FILE],
    encoding: str = "utf-8",
    service: ConversionService = Depends(get_conversion_service),
):
    """Handle XML to XLSX conversion request."""
    if not file.filename.lower().endswith(".xml"):
        raise HTTPException(status_code=400, detail="Arquivo deve ser XML")

    try:
        return service.convert_xml_to_xlsx(
            file.file,
            options={
                "encoding": encoding,
            },
        )
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
