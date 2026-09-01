import io

from PIL import Image

from src.webp_to_jpg.converters.webp_to_jpg import WebpToJpgConverter


def test_convert_valid_webp_to_jpg():
    buffer = io.BytesIO()
    image = Image.new("RGB", (100, 100), color="green")
    image.save(buffer, "WEBP")
    buffer.seek(0)

    converter = WebpToJpgConverter()
    result = converter.convert(buffer)

    assert result["rows_processed"] == 1
    assert result["output_file"] == "output.jpg"
