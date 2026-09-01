import io

from src.txt_to_csv.converters.txt_to_csv import TxtToCsvConverter


def test_convert_valid_txt_to_csv():
    txt_content = "name\tage\nAna\t30\nJoao\t25"
    file = io.BytesIO(txt_content.encode("utf-8"))

    converter = TxtToCsvConverter()
    result = converter.convert(file, has_header=True)

    assert result["rows_processed"] == 2
    assert "name" in result["columns"]
