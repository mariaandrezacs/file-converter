"""Service responsible for orchestrating file conversions."""

from src.csv_to_xlsx.converters.csv_to_xlsx import CsvToXlsxConverter


class ConversionService:
    """Coordinate file conversion operations."""

    def __init__(self):
        """Initialize conversion service."""
        self.converter = CsvToXlsxConverter()

    def convert_csv_to_xlsx(self, file, options):
        """Convert a CSV file to XLSX format."""
        return self.converter.convert(file, **options)
