"""Service responsible for orchestrating XML to XLSX conversion."""

from src.xml_to_xlsx.converters.xml_to_xlsx import XmlToXlsxConverter


class ConversionService:
    """Coordinate XML to XLSX conversion operations."""

    def __init__(self):
        """Initialize conversion service."""
        self.converter = XmlToXlsxConverter()

    def convert_xml_to_xlsx(self, file, options):
        """Convert a XML file to XLSX format."""
        return self.converter.convert(file, **options)
