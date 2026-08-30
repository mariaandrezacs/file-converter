"""Service responsible for orchestrating JSON to CSV conversion."""

from src.json_to_csv.converters.json_to_csv import JsonToCsvConverter


class ConversionService:
    """Coordinate JSON to CSV conversion operations."""

    def __init__(self):
        """Initialize conversion service."""
        self.converter = JsonToCsvConverter()

    def convert_json_to_csv(self, file, options):
        """Convert a JSON file to CSV format."""
        return self.converter.convert(file, **options)
