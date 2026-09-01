"""JPG to WebP converter implementation."""

from PIL import Image

from src.core.converter import Converter


class JpgToWebpConverter(Converter):
    """Convert JPG files into WebP format."""

    def convert(self, file, **options) -> dict:
        """Perform JPG to WebP conversion."""
        try:
            image = Image.open(file)
        except Exception as e:
            raise ValueError(f"Erro ao ler JPG: {str(e)}") from e

        if image.mode == "P":
            image = image.convert("RGB")

        output_file = "output.webp"
        image.save(output_file, "WEBP")

        return {
            "output_file": output_file,
            "rows_processed": 1,
            "columns": [],
        }
