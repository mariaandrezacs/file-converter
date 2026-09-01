import io

from src.csv_to_xml.converters.csv_to_xml import CsvToXmlConverter


def test_convert_valid_csv_to_xml():
    csv_content = "name,age\nAna,30\nJoão,25"
    file = io.BytesIO(csv_content.encode("utf-8"))

    converter = CsvToXmlConverter()
    result = converter.convert(file)

    assert result["rows_processed"] == 2
    assert "name" in result["columns"]
