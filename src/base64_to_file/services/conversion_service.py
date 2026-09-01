"""Service responsible for orchestrating Base64 to File conversion."""

from src.base64_to_file.converters.base64_to_file import Base64ToFileConverter


class ConversionService:
    """Coordinate Base64 to File conversion operations."""

    def __init__(self):
        """Initialize conversion service."""
        self.converter = Base64ToFileConverter()

    def convert_base64_to_file(self, file, options):
        """Convert Base64 content to a file."""
        return self.converter.convert(file, **options)
