"""Service responsible for orchestrating XML to JSON conversion."""

from src.xml_to_json.converters.xml_to_json import XmlToJsonConverter


class ConversionService:
    """Coordinate XML to JSON conversion operations."""

    def __init__(self):
        """Initialize conversion service."""
        self.converter = XmlToJsonConverter()

    def convert_xml_to_json(self, file, options):
        """Convert a XML file to JSON format."""
        return self.converter.convert(file, **options)
