"""CSV to XML converter implementation."""

import pandas as pd

from src.core.converter import Converter


class CsvToXmlConverter(Converter):
    """Convert CSV files into XML format."""

    def convert(self, file, **options) -> dict:
        """Perform CSV to XML conversion."""
        delimiter = options.get("delimiter", ",")
        encoding = options.get("encoding", "utf-8")

        try:
            df = pd.read_csv(file, delimiter=delimiter, encoding=encoding)
        except Exception as e:
            raise ValueError(f"Erro ao ler CSV: {str(e)}") from e

        if df.empty:
            raise ValueError("O arquivo CSV está vazio")

        try:
            xml_string = df.to_xml(
                root_name="records",
                row_name="record",
                encoding="utf-8",
                xml_declaration=True,
                pretty_print=True,
                parser="etree",
            )
        except Exception as e:
            raise ValueError(f"Erro ao gerar XML: {str(e)}") from e

        output_file = "output.xml"
        with open(output_file, "w", encoding=encoding) as f:
            f.write(xml_string)

        return {
            "output_file": output_file,
            "rows_processed": len(df),
            "columns": list(df.columns),
        }
