import io

from src.xml_to_csv.converters.xml_to_csv import XmlToCsvConverter


def test_convert_valid_xml_to_csv():
    xml_content = (
        b"<records>"
        b"<record><name>Ana</name><age>30</age></record>"
        b"<record><name>Joao</name><age>25</age></record>"
        b"</records>"
    )
    file = io.BytesIO(xml_content)

    converter = XmlToCsvConverter()
    result = converter.convert(file)

    assert result["rows_processed"] == 2
    assert "name" in result["columns"]
