"""Service responsible for orchestrating JPG to PDF conversion."""

from src.jpg_to_pdf.converters.jpg_to_pdf import JpgToPdfConverter


class ConversionService:
    """Coordinate JPG to PDF conversion operations."""

    def __init__(self):
        """Initialize conversion service."""
        self.converter = JpgToPdfConverter()

    def convert_jpg_to_pdf(self, file, options):
        """Convert a JPG file to PDF format."""
        return self.converter.convert(file, **options)
