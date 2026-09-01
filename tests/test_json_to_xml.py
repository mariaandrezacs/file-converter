import io

from src.json_to_xml.converters.json_to_xml import JsonToXmlConverter


def test_convert_valid_json_to_xml():
    json_content = b'[{"name":"Ana","age":30},{"name":"Joao","age":25}]'
    file = io.BytesIO(json_content)

    converter = JsonToXmlConverter()
    result = converter.convert(file)

    assert result["rows_processed"] == 2
    assert "name" in result["columns"]
