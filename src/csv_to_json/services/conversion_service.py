"""Service responsible for orchestrating CSV to JSON conversion."""

from src.csv_to_json.converters.csv_to_json import CsvToJsonConverter


class ConversionService:
    """Coordinate CSV to JSON conversion operations."""

    def __init__(self):
        """Initialize conversion service."""
        self.converter = CsvToJsonConverter()

    def convert_csv_to_json(self, file, options):
        """Convert a CSV file to JSON format."""
        return self.converter.convert(file, **options)
