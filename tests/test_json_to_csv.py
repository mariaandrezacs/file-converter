import io

from src.json_to_csv.converters.json_to_csv import JsonToCsvConverter


def test_convert_valid_json():
    json_content = b'[{"name":"Ana","age":30},{"name":"Joao","age":25}]'
    file = io.BytesIO(json_content)

    converter = JsonToCsvConverter()
    result = converter.convert(file)

    assert result["rows_processed"] == 2
    assert "name" in result["columns"]
