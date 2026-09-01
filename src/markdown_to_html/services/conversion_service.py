"""Service responsible for orchestrating Markdown to HTML conversion."""

from src.markdown_to_html.converters.markdown_to_html import MarkdownToHtmlConverter


class ConversionService:
    """Coordinate Markdown to HTML conversion operations."""

    def __init__(self):
        """Initialize conversion service."""
        self.converter = MarkdownToHtmlConverter()

    def convert_markdown_to_html(self, file, options):
        """Convert a Markdown file to HTML format."""
        return self.converter.convert(file, **options)
