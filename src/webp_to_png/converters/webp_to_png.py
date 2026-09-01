"""WebP to PNG converter implementation."""

from PIL import Image

from src.core.converter import Converter


class WebpToPngConverter(Converter):
    """Convert WebP files into PNG format."""

    def convert(self, file, **options) -> dict:
        """Perform WebP to PNG conversion."""
        try:
            image = Image.open(file)
        except Exception as e:
            raise ValueError(f"Erro ao ler WebP: {str(e)}") from e

        output_file = "output.png"
        image.save(output_file, "PNG")

        return {
            "output_file": output_file,
            "rows_processed": 1,
            "columns": [],
        }
