"""Service responsible for orchestrating XLSX to XML conversion."""

from src.xlsx_to_xml.converters.xlsx_to_xml import XlsxToXmlConverter


class ConversionService:
    """Coordinate XLSX to XML conversion operations."""

    def __init__(self):
        """Initialize conversion service."""
        self.converter = XlsxToXmlConverter()

    def convert_xlsx_to_xml(self, file, options):
        """Convert a XLSX file to XML format."""
        return self.converter.convert(file, **options)
