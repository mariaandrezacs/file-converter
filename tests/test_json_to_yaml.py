import io

from src.json_to_yaml.converters.json_to_yaml import JsonToYamlConverter


def test_convert_valid_json_to_yaml():
    json_content = b'[{"name":"Ana","age":30},{"name":"Joao","age":25}]'
    file = io.BytesIO(json_content)

    converter = JsonToYamlConverter()
    result = converter.convert(file)

    assert result["rows_processed"] == 2
    assert "name" in result["columns"]
