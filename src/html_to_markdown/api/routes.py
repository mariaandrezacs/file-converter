"""HTTP routes for HTML to Markdown conversion."""

from typing import Annotated

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from src.html_to_markdown.services.conversion_service import ConversionService

router = APIRouter()

HTML_FILE = File(...)


def get_conversion_service() -> ConversionService:
    """Provide a ConversionService instance."""
    return ConversionService()


@router.post("/convert/html-to-markdown")
async def convert_html_to_markdown(
    file: Annotated[UploadFile, HTML_FILE],
    encoding: str = "utf-8",
    service: ConversionService = Depends(get_conversion_service),
):
    """Handle HTML to Markdown conversion request."""
    if not file.filename.lower().endswith((".html", ".htm")):
        raise HTTPException(status_code=400, detail="Arquivo deve ser HTML")

    try:
        return service.convert_html_to_markdown(
            file.file,
            options={
                "encoding": encoding,
            },
        )
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
