"""JSON to XLSX converter implementation."""

import json

import pandas as pd

from src.core.converter import Converter


class JsonToXlsxConverter(Converter):
    """Convert JSON files into XLSX format."""

    def convert(self, file, **options) -> dict:
        """Perform JSON to XLSX conversion."""
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
            raise ValueError("Não foi possível gerar XLSX a partir do JSON")

        output_file = "output.xlsx"
        df.to_excel(output_file, index=False)

        return {
            "output_file": output_file,
            "rows_processed": len(df),
            "columns": list(df.columns),
        }
