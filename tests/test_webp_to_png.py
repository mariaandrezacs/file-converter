import io

from PIL import Image

from src.webp_to_png.converters.webp_to_png import WebpToPngConverter


def test_convert_valid_webp_to_png():
    buffer = io.BytesIO()
    image = Image.new("RGBA", (100, 100), color=(0, 255, 0, 128))
    image.save(buffer, "WEBP")
    buffer.seek(0)

    converter = WebpToPngConverter()
    result = converter.convert(buffer)

    assert result["rows_processed"] == 1
    assert result["output_file"] == "output.png"
