"""Base64 to File converter implementation."""

import base64

from src.core.converter import Converter


class Base64ToFileConverter(Converter):
    """Convert a Base64 string into a file."""

    def convert(self, file, **options) -> dict:
        """Perform Base64 to File conversion."""
        content = options.get("content")
        filename = options.get("filename", "output.bin")

        if not content:
            raise ValueError("Conteúdo Base64 é obrigatório")

        try:
            decoded = base64.b64decode(content)
        except Exception as e:
            raise ValueError(f"Erro ao decodificar Base64: {str(e)}") from e

        with open(filename, "wb") as f:
            f.write(decoded)

        return {
            "output_file": filename,
            "rows_processed": 1,
            "columns": [],
        }
