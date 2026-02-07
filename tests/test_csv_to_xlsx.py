import io

from src.csv_to_xlsx.converters.csv_to_xlsx import CsvToXlsxConverter


def test_convert_valid_csv():
    csv_content = "name,age\nAna,30\nJoão,25"
    file = io.BytesIO(csv_content.encode("utf-8"))

    converter = CsvToXlsxConverter()
    result = converter.convert(file)

    assert result["rows_processed"] == 2
    assert "name" in result["columns"]
