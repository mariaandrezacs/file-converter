"""Service responsible for orchestrating Word to PDF conversion."""

from src.word_to_pdf.converters.word_to_pdf import WordToPdfConverter


class ConversionService:
    """Coordinate Word to PDF conversion operations."""

    def __init__(self):
        """Initialize conversion service."""
        self.converter = WordToPdfConverter()

    def convert_word_to_pdf(self, file, options):
        """Convert a Word file to PDF format."""
        return self.converter.convert(file, **options)
