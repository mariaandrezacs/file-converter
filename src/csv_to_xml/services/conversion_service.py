"""Service responsible for orchestrating CSV to XML conversion."""

from src.csv_to_xml.converters.csv_to_xml import CsvToXmlConverter


class ConversionService:
    """Coordinate CSV to XML conversion operations."""

    def __init__(self):
        """Initialize conversion service."""
        self.converter = CsvToXmlConverter()

    def convert_csv_to_xml(self, file, options):
        """Convert a CSV file to XML format."""
        return self.converter.convert(file, **options)
