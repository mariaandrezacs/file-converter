"""HTML to Markdown converter implementation."""

from bs4 import BeautifulSoup

from src.core.converter import Converter


class HtmlToMarkdownConverter(Converter):
    """Convert HTML files into Markdown format."""

    def convert(self, file, **options) -> dict:
        """Perform HTML to Markdown conversion."""
        encoding = options.get("encoding", "utf-8")

        try:
            content = file.read().decode(encoding)
        except Exception as e:
            raise ValueError(f"Erro ao ler HTML: {str(e)}") from e

        if not content.strip():
            raise ValueError("O arquivo HTML está vazio")

        soup = BeautifulSoup(content, "html.parser")
        markdown_lines = [
            self._element_to_markdown(element) for element in soup.body or soup
        ]

        output_file = "output.md"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n\n".join(line for line in markdown_lines if line))

        return {
            "output_file": output_file,
            "rows_processed": len(markdown_lines),
            "columns": [],
        }

    def _element_to_markdown(self, element) -> str:
        """Convert an HTML element to Markdown."""
        name = element.name
        if hasattr(element, "get_text"):
            text = element.get_text(strip=True) or ""
        else:
            text = str(element).strip()

        if not text:
            return ""

        if name in ("h1", "h2", "h3", "h4", "h5", "h6"):
            level = int(name[1])
            return f"{'#' * level} {text}"

        if name == "p":
            return text

        if name == "a" and (href := element.get("href")):
            return f"[{text}]({href})"

        if name in ("ul", "ol"):
            lines = []
            for i, item in enumerate(element.find_all("li"), 1):
                prefix = f"{i}. " if name == "ol" else "- "
                lines.append(f"{prefix}{item.get_text(strip=True)}")
            return "\n".join(lines)

        return text
