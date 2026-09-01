import io

from src.base64_to_file.converters.base64_to_file import Base64ToFileConverter


def test_convert_valid_base64_to_file():
    import base64

    content = base64.b64encode(b"conteudo de teste").decode("ascii")
    file = io.BytesIO()

    converter = Base64ToFileConverter()
    result = converter.convert(file, content=content, filename="output.bin")

    assert result["rows_processed"] == 1
    assert result["output_file"] == "output.bin"
