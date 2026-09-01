import io

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from src.pdf_to_xlsx.converters.pdf_to_xlsx import PdfToXlsxConverter


def test_convert_valid_pdf_to_xlsx():
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    c.drawString(100, 700, "Ana,30")
    c.drawString(100, 680, "João,25")
    c.save()
    buffer.seek(0)

    converter = PdfToXlsxConverter()
    result = converter.convert(buffer)

    assert result["rows_processed"] == 2
