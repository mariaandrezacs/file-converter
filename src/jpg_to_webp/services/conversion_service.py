"""Service responsible for orchestrating JPG to WebP conversion."""

from src.jpg_to_webp.converters.jpg_to_webp import JpgToWebpConverter


class ConversionService:
    """Coordinate JPG to WebP conversion operations."""

    def __init__(self):
        """Initialize conversion service."""
        self.converter = JpgToWebpConverter()

    def convert_jpg_to_webp(self, file, options):
        """Convert a JPG file to WebP format."""
        return self.converter.convert(file, **options)
