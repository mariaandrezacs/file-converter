import io

from PIL import Image

from src.jpg_to_webp.converters.jpg_to_webp import JpgToWebpConverter


def test_convert_valid_jpg_to_webp():
    buffer = io.BytesIO()
    image = Image.new("RGB", (100, 100), color="yellow")
    image.save(buffer, "JPEG")
    buffer.seek(0)

    converter = JpgToWebpConverter()
    result = converter.convert(buffer)

    assert result["rows_processed"] == 1
    assert result["output_file"] == "output.webp"
