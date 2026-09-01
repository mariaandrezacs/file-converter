"""Markdown to HTML converter implementation."""

import markdown

from src.core.converter import Converter


class MarkdownToHtmlConverter(Converter):
    """Convert Markdown files into HTML format."""

    def convert(self, file, **options) -> dict:
        """Perform Markdown to HTML conversion."""
        encoding = options.get("encoding", "utf-8")

        try:
            content = file.read().decode(encoding)
        except Exception as e:
            raise ValueError(f"Erro ao ler Markdown: {str(e)}") from e

        if not content.strip():
            raise ValueError("O arquivo Markdown está vazio")

        html = markdown.markdown(content)

        output_file = "output.html"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(html)

        return {
            "output_file": output_file,
            "rows_processed": len(content.splitlines()),
            "columns": [],
        }
