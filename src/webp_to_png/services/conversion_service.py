"""Service responsible for orchestrating WebP to PNG conversion."""

from src.webp_to_png.converters.webp_to_png import WebpToPngConverter


class ConversionService:
    """Coordinate WebP to PNG conversion operations."""

    def __init__(self):
        """Initialize conversion service."""
        self.converter = WebpToPngConverter()

    def convert_webp_to_png(self, file, options):
        """Convert a WebP file to PNG format."""
        return self.converter.convert(file, **options)
