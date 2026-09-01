"""Service responsible for orchestrating XLSX to JSON conversion."""

from src.xlsx_to_json.converters.xlsx_to_json import XlsxToJsonConverter


class ConversionService:
    """Coordinate XLSX to JSON conversion operations."""

    def __init__(self):
        """Initialize conversion service."""
        self.converter = XlsxToJsonConverter()

    def convert_xlsx_to_json(self, file, options):
        """Convert a XLSX file to JSON format."""
        return self.converter.convert(file, **options)
