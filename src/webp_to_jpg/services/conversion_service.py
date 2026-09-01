"""Service responsible for orchestrating WebP to JPG conversion."""

from src.webp_to_jpg.converters.webp_to_jpg import WebpToJpgConverter


class ConversionService:
    """Coordinate WebP to JPG conversion operations."""

    def __init__(self):
        """Initialize conversion service."""
        self.converter = WebpToJpgConverter()

    def convert_webp_to_jpg(self, file, options):
        """Convert a WebP file to JPG format."""
        return self.converter.convert(file, **options)
