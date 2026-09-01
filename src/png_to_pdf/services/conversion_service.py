"""Service responsible for orchestrating PNG to PDF conversion."""

from src.png_to_pdf.converters.png_to_pdf import PngToPdfConverter


class ConversionService:
    """Coordinate PNG to PDF conversion operations."""

    def __init__(self):
        """Initialize conversion service."""
        self.converter = PngToPdfConverter()

    def convert_png_to_pdf(self, file, options):
        """Convert a PNG file to PDF format."""
        return self.converter.convert(file, **options)
