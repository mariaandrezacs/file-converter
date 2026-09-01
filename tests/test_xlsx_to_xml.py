import io

import pandas as pd

from src.xlsx_to_xml.converters.xlsx_to_xml import XlsxToXmlConverter


def test_convert_valid_xlsx_to_xml():
    buffer = io.BytesIO()
    df = pd.DataFrame({"name": ["Ana", "João"], "age": [30, 25]})
    df.to_excel(buffer, index=False, engine="openpyxl")
    buffer.seek(0)

    converter = XlsxToXmlConverter()
    result = converter.convert(buffer)

    assert result["rows_processed"] == 2
    assert "name" in result["columns"]
