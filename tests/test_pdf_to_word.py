import io

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from src.pdf_to_word.converters.pdf_to_word import PdfToWordConverter


def test_convert_valid_pdf_to_word():
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    c.drawString(100, 700, "Ana")
    c.drawString(100, 680, "João")
    c.save()
    buffer.seek(0)

    converter = PdfToWordConverter()
    result = converter.convert(buffer)

    assert result["rows_processed"] == 1
