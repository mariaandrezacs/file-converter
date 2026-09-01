"""WebP to JPG converter implementation."""

from PIL import Image

from src.core.converter import Converter


class WebpToJpgConverter(Converter):
    """Convert WebP files into JPG format."""

    def convert(self, file, **options) -> dict:
        """Perform WebP to JPG conversion."""
        try:
            image = Image.open(file)
        except Exception as e:
            raise ValueError(f"Erro ao ler WebP: {str(e)}") from e

        if image.mode in ("RGBA", "P"):
            image = image.convert("RGB")

        output_file = "output.jpg"
        image.save(output_file, "JPEG")

        return {
            "output_file": output_file,
            "rows_processed": 1,
            "columns": [],
        }
