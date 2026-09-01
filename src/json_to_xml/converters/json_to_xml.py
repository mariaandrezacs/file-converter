"""JSON to XML converter implementation."""

import json

import pandas as pd

from src.core.converter import Converter


class JsonToXmlConverter(Converter):
    """Convert JSON files into XML format."""

    def convert(self, file, **options) -> dict:
        """Perform JSON to XML conversion."""
        encoding = options.get("encoding", "utf-8")

        try:
            content = file.read().decode(encoding)
            data = json.loads(content)
        except Exception as e:
            raise ValueError(f"Erro ao ler JSON: {str(e)}") from e

        if data is None or (isinstance(data, list) and not data):
            raise ValueError("O arquivo JSON está vazio")

        try:
            df = pd.json_normalize(data)
        except Exception as e:
            raise ValueError(f"Erro ao normalizar JSON: {str(e)}") from e

        if df.empty:
            raise ValueError("Não foi possível gerar XML a partir do JSON")

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
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(xml_string)

        return {
            "output_file": output_file,
            "rows_processed": len(df),
            "columns": list(df.columns),
        }
