import io

from src.markdown_to_html.converters.markdown_to_html import MarkdownToHtmlConverter


def test_convert_valid_markdown_to_html():
    markdown_content = "# Título\n\nParágrafo de teste.".encode()
    file = io.BytesIO(markdown_content)

    converter = MarkdownToHtmlConverter()
    result = converter.convert(file)

    assert result["rows_processed"] == 3
    assert result["output_file"] == "output.html"
