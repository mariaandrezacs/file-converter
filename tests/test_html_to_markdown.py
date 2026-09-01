import io

from src.html_to_markdown.converters.html_to_markdown import HtmlToMarkdownConverter


def test_convert_valid_html_to_markdown():
    html_content = "<h1>Título</h1><p>Parágrafo de teste.</p>".encode()
    file = io.BytesIO(html_content)

    converter = HtmlToMarkdownConverter()
    result = converter.convert(file)

    assert result["rows_processed"] > 0
    assert result["output_file"] == "output.md"
