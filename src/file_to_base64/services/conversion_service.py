"""Service responsible for orchestrating File to Base64 conversion."""

from src.file_to_base64.converters.file_to_base64 import FileToBase64Converter


class ConversionService:
    """Coordinate File to Base64 conversion operations."""

    def __init__(self):
        """Initialize conversion service."""
        self.converter = FileToBase64Converter()

    def convert_file_to_base64(self, file, options):
        """Convert a file to Base64 format."""
        return self.converter.convert(file, **options)
