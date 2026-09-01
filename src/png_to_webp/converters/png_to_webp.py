"""PNG to WebP converter implementation."""

from PIL import Image

from src.core.converter import Converter


class PngToWebpConverter(Converter):
    """Convert PNG files into WebP format."""

    def convert(self, file, **options) -> dict:
        """Perform PNG to WebP conversion."""
        try:
            image = Image.open(file)
        except Exception as e:
            raise ValueError(f"Erro ao ler PNG: {str(e)}") from e

        output_file = "output.webp"
        image.save(output_file, "WEBP")

        return {
            "output_file": output_file,
            "rows_processed": 1,
            "columns": [],
        }
