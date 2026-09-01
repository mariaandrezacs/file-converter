"""Service responsible for orchestrating XML to CSV conversion."""

from src.xml_to_csv.converters.xml_to_csv import XmlToCsvConverter


class ConversionService:
    """Coordinate XML to CSV conversion operations."""

    def __init__(self):
        """Initialize conversion service."""
        self.converter = XmlToCsvConverter()

    def convert_xml_to_csv(self, file, options):
        """Convert a XML file to CSV format."""
        return self.converter.convert(file, **options)
