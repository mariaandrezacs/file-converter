"""Service responsible for orchestrating PNG to WebP conversion."""

from src.png_to_webp.converters.png_to_webp import PngToWebpConverter


class ConversionService:
    """Coordinate PNG to WebP conversion operations."""

    def __init__(self):
        """Initialize conversion service."""
        self.converter = PngToWebpConverter()

    def convert_png_to_webp(self, file, options):
        """Convert a PNG file to WebP format."""
        return self.converter.convert(file, **options)
