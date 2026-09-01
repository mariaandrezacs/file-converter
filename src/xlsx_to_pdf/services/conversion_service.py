"""Service responsible for orchestrating XLSX to PDF conversion."""

from src.xlsx_to_pdf.converters.xlsx_to_pdf import XlsxToPdfConverter


class ConversionService:
    """Coordinate XLSX to PDF conversion operations."""

    def __init__(self):
        """Initialize conversion service."""
        self.converter = XlsxToPdfConverter()

    def convert_xlsx_to_pdf(self, file, options):
        """Convert a XLSX file to PDF format."""
        return self.converter.convert(file, **options)
