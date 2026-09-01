"""File to Base64 converter implementation."""

import base64

from src.core.converter import Converter


class FileToBase64Converter(Converter):
    """Convert any file into a Base64 string."""

    def convert(self, file, **options) -> dict:
        """Perform File to Base64 conversion."""
        try:
            content = file.read()
        except Exception as e:
            raise ValueError(f"Erro ao ler arquivo: {str(e)}") from e

        if not content:
            raise ValueError("O arquivo está vazio")

        encoded = base64.b64encode(content).decode("ascii")

        return {
            "output_file": None,
            "base64": encoded,
            "rows_processed": 1,
            "columns": [],
        }
