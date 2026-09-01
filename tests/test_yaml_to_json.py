import io

from src.yaml_to_json.converters.yaml_to_json import YamlToJsonConverter


def test_convert_valid_yaml_to_json():
    yaml_content = b"- name: Ana\n  age: 30\n- name: Joao\n  age: 25"
    file = io.BytesIO(yaml_content)

    converter = YamlToJsonConverter()
    result = converter.convert(file)

    assert result["rows_processed"] == 2
    assert "name" in result["columns"]
