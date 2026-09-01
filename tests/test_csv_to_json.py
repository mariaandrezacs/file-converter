import io

from src.csv_to_json.converters.csv_to_json import CsvToJsonConverter


def test_convert_valid_csv_to_json():
    csv_content = "name,age\nAna,30\nJoão,25"
    file = io.BytesIO(csv_content.encode("utf-8"))

    converter = CsvToJsonConverter()
    result = converter.convert(file)

    assert result["rows_processed"] == 2
    assert "name" in result["columns"]
