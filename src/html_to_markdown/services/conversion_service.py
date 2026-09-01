"""Service responsible for orchestrating HTML to Markdown conversion."""

from src.html_to_markdown.converters.html_to_markdown import HtmlToMarkdownConverter


class ConversionService:
    """Coordinate HTML to Markdown conversion operations."""

    def __init__(self):
        """Initialize conversion service."""
        self.converter = HtmlToMarkdownConverter()

    def convert_html_to_markdown(self, file, options):
        """Convert a HTML file to Markdown format."""
        return self.converter.convert(file, **options)
