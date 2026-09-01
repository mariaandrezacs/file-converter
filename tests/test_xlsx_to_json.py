import io

import pandas as pd

from src.xlsx_to_json.converters.xlsx_to_json import XlsxToJsonConverter


def test_convert_valid_xlsx_to_json():
    buffer = io.BytesIO()
    df = pd.DataFrame({"name": ["Ana", "João"], "age": [30, 25]})
    df.to_excel(buffer, index=False, engine="openpyxl")
    buffer.seek(0)

    converter = XlsxToJsonConverter()
    result = converter.convert(buffer)

    assert result["rows_processed"] == 2
    assert "name" in result["columns"]
