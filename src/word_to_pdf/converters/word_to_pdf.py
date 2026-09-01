"""Word to PDF converter implementation."""

from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from src.core.converter import Converter


class WordToPdfConverter(Converter):
    """Convert Word files into PDF format."""

    def convert(self, file, **options) -> dict:
        """Perform Word to PDF conversion."""
        try:
            document = Document(file)
        except Exception as e:
            raise ValueError(f"Erro ao ler Word: {str(e)}") from e

        paragraphs = [p.text for p in document.paragraphs if p.text.strip()]
        if not paragraphs:
            raise ValueError("O arquivo Word está vazio")

        output_file = "output.pdf"
        c = canvas.Canvas(output_file, pagesize=letter)
        width, height = letter
        margin = 72
        y = height - margin
        line_height = 14

        c.setFont("Helvetica", 12)
        for paragraph in paragraphs:
            for line in paragraph.splitlines():
                if y < margin:
                    c.showPage()
                    c.setFont("Helvetica", 12)
                    y = height - margin
                c.drawString(margin, y, line)
                y -= line_height

            y -= line_height

        c.save()

        return {
            "output_file": output_file,
            "rows_processed": len(paragraphs),
            "columns": [],
        }
