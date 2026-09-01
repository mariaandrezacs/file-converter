import io

from PIL import Image

from src.png_to_webp.converters.png_to_webp import PngToWebpConverter


def test_convert_valid_png_to_webp():
    buffer = io.BytesIO()
    image = Image.new("RGBA", (100, 100), color=(255, 0, 0, 128))
    image.save(buffer, "PNG")
    buffer.seek(0)

    converter = PngToWebpConverter()
    result = converter.convert(buffer)

    assert result["rows_processed"] == 1
    assert result["output_file"] == "output.webp"
