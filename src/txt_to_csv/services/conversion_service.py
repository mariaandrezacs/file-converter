"""Service responsible for orchestrating TXT to CSV conversion."""

from src.txt_to_csv.converters.txt_to_csv import TxtToCsvConverter


class ConversionService:
    """Coordinate TXT to CSV conversion operations."""

    def __init__(self):
        """Initialize conversion service."""
        self.converter = TxtToCsvConverter()

    def convert_txt_to_csv(self, file, options):
        """Convert a TXT file to CSV format."""
        return self.converter.convert(file, **options)
