import io

from PIL import Image

from src.png_to_pdf.converters.png_to_pdf import PngToPdfConverter


def test_convert_valid_png_to_pdf():
    buffer = io.BytesIO()
    image = Image.new("RGBA", (100, 100), color=(0, 0, 255, 128))
    image.save(buffer, "PNG")
    buffer.seek(0)

    converter = PngToPdfConverter()
    result = converter.convert(buffer)

    assert result["rows_processed"] == 1
    assert result["output_file"] == "output.pdf"
