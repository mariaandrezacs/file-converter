import io

from src.json_to_xlsx.converters.json_to_xlsx import JsonToXlsxConverter


def test_convert_valid_json_to_xlsx():
    json_content = b'[{"name":"Ana","age":30},{"name":"Joao","age":25}]'
    file = io.BytesIO(json_content)

    converter = JsonToXlsxConverter()
    result = converter.convert(file)

    assert result["rows_processed"] == 2
    assert "name" in result["columns"]
