import io

from src.file_to_base64.converters.file_to_base64 import FileToBase64Converter


def test_convert_valid_file_to_base64():
    file = io.BytesIO(b"conteudo de teste")

    converter = FileToBase64Converter()
    result = converter.convert(file)

    assert result["rows_processed"] == 1
    assert "base64" in result
