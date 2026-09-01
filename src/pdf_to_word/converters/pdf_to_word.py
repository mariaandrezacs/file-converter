"""PDF to Word converter implementation."""

from docx import Document
from pypdf import PdfReader

from src.core.converter import Converter


class PdfToWordConverter(Converter):
    """Convert PDF files into Word format."""

    def convert(self, file, **options) -> dict:
        """Perform PDF to Word conversion."""
        try:
            reader = PdfReader(file)
        except Exception as e:
            raise ValueError(f"Erro ao ler PDF: {str(e)}") from e

        if not reader.pages:
            raise ValueError("O arquivo PDF está vazio")

        text = "\n".join(page.extract_text() or "" for page in reader.pages)
        if not text.strip():
            raise ValueError("O arquivo PDF não contém texto extraível")

        document = Document()
        for paragraph in text.split("\n"):
            document.add_paragraph(paragraph)

        output_file = "output.docx"
        document.save(output_file)

        return {
            "output_file": output_file,
            "rows_processed": len(reader.pages),
            "columns": [],
        }
