"""Service responsible for orchestrating PDF to XLSX conversion."""

from src.pdf_to_xlsx.converters.pdf_to_xlsx import PdfToXlsxConverter


class ConversionService:
    """Coordinate PDF to XLSX conversion operations."""

    def __init__(self):
        """Initialize conversion service."""
        self.converter = PdfToXlsxConverter()

    def convert_pdf_to_xlsx(self, file, options):
        """Convert a PDF file to XLSX format."""
        return self.converter.convert(file, **options)
