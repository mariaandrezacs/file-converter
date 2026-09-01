import io

from PIL import Image

from src.jpg_to_pdf.converters.jpg_to_pdf import JpgToPdfConverter


def test_convert_valid_jpg_to_pdf():
    buffer = io.BytesIO()
    image = Image.new("RGB", (100, 100), color="red")
    image.save(buffer, "JPEG")
    buffer.seek(0)

    converter = JpgToPdfConverter()
    result = converter.convert(buffer)

    assert result["rows_processed"] == 1
    assert result["output_file"] == "output.pdf"
