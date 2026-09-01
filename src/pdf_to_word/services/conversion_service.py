"""Service responsible for orchestrating PDF to Word conversion."""

from src.pdf_to_word.converters.pdf_to_word import PdfToWordConverter


class ConversionService:
    """Coordinate PDF to Word conversion operations."""

    def __init__(self):
        """Initialize conversion service."""
        self.converter = PdfToWordConverter()

    def convert_pdf_to_word(self, file, options):
        """Convert a PDF file to Word format."""
        return self.converter.convert(file, **options)
