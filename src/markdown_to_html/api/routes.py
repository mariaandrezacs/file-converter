"""HTTP routes for Markdown to HTML conversion."""

from typing import Annotated

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from src.markdown_to_html.services.conversion_service import ConversionService

router = APIRouter()

MARKDOWN_FILE = File(...)


def get_conversion_service() -> ConversionService:
    """Provide a ConversionService instance."""
    return ConversionService()


@router.post("/convert/markdown-to-html")
async def convert_markdown_to_html(
    file: Annotated[UploadFile, MARKDOWN_FILE],
    encoding: str = "utf-8",
    service: ConversionService = Depends(get_conversion_service),
):
    """Handle Markdown to HTML conversion request."""
    if not file.filename.lower().endswith((".md", ".markdown")):
        raise HTTPException(status_code=400, detail="Arquivo deve ser Markdown")

    try:
        return service.convert_markdown_to_html(
            file.file,
            options={
                "encoding": encoding,
            },
        )
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
