"""Service responsible for orchestrating XLSX to CSV conversion."""

from src.xlsx_to_csv.converters.xlsx_to_csv import XlsxToCsvConverter


class ConversionService:
    """Coordinate XLSX to CSV conversion operations."""

    def __init__(self):
        """Initialize conversion service."""
        self.converter = XlsxToCsvConverter()

    def convert_xlsx_to_csv(self, file, options):
        """Convert a XLSX file to CSV format."""
        return self.converter.convert(file, **options)
