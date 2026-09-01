"""CSV to JSON converter implementation."""

import json

import pandas as pd

from src.core.converter import Converter


class CsvToJsonConverter(Converter):
    """Convert CSV files into JSON format."""

    def convert(self, file, **options) -> dict:
        """Perform CSV to JSON conversion."""
        delimiter = options.get("delimiter", ",")
        encoding = options.get("encoding", "utf-8")

        try:
            df = pd.read_csv(file, delimiter=delimiter, encoding=encoding)
        except Exception as e:
            raise ValueError(f"Erro ao ler CSV: {str(e)}") from e

        if df.empty:
            raise ValueError("O arquivo CSV está vazio")

        records = df.to_dict(orient="records")

        output_file = "output.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(records, f, ensure_ascii=False, indent=2)

        return {
            "output_file": output_file,
            "rows_processed": len(df),
            "columns": list(df.columns),
        }
