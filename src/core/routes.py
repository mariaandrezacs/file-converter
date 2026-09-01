"""Shared HTTP routes for the file converter system."""

from pathlib import Path

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

router = APIRouter()

OUTPUT_DIR = Path(".")


@router.get("/download/{filename}")
async def download_file(filename: str):
    """Download a previously generated output file."""
    if not filename or ".." in filename or "/" in filename or "\\" in filename:
        raise HTTPException(status_code=400, detail="Nome de arquivo inválido")

    file_path = OUTPUT_DIR / filename
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="Arquivo não encontrado")

    return FileResponse(
        file_path,
        filename=filename,
        media_type="application/octet-stream",
    )
