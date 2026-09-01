"""Service responsible for orchestrating JSON to XLSX conversion."""

from src.json_to_xlsx.converters.json_to_xlsx import JsonToXlsxConverter


class ConversionService:
    """Coordinate JSON to XLSX conversion operations."""

    def __init__(self):
        """Initialize conversion service."""
        self.converter = JsonToXlsxConverter()

    def convert_json_to_xlsx(self, file, options):
        """Convert a JSON file to XLSX format."""
        return self.converter.convert(file, **options)
