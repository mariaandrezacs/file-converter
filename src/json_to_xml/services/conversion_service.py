"""Service responsible for orchestrating JSON to XML conversion."""

from src.json_to_xml.converters.json_to_xml import JsonToXmlConverter


class ConversionService:
    """Coordinate JSON to XML conversion operations."""

    def __init__(self):
        """Initialize conversion service."""
        self.converter = JsonToXmlConverter()

    def convert_json_to_xml(self, file, options):
        """Convert a JSON file to XML format."""
        return self.converter.convert(file, **options)
