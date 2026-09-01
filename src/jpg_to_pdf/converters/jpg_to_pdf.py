"""JPG to PDF converter implementation."""

from PIL import Image

from src.core.converter import Converter


class JpgToPdfConverter(Converter):
    """Convert JPG files into PDF format."""

    def convert(self, file, **options) -> dict:
        """Perform JPG to PDF conversion."""
        try:
            image = Image.open(file)
        except Exception as e:
            raise ValueError(f"Erro ao ler JPG: {str(e)}") from e

        if image.mode in ("RGBA", "P"):
            image = image.convert("RGB")

        output_file = "output.pdf"
        image.save(output_file, "PDF", resolution=100.0)

        return {
            "output_file": output_file,
            "rows_processed": 1,
            "columns": [],
        }
