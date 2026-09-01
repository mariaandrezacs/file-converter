import io

from src.xml_to_xlsx.converters.xml_to_xlsx import XmlToXlsxConverter


def test_convert_valid_xml():
    xml_content = (
        b"<root>"
        b"<person><name>Ana</name><age>30</age></person>"
        b"<person><name>Joao</name><age>25</age></person>"
        b"</root>"
    )
    file = io.BytesIO(xml_content)

    converter = XmlToXlsxConverter()
    result = converter.convert(file)

    assert result["rows_processed"] == 2
    assert "name" in result["columns"]
