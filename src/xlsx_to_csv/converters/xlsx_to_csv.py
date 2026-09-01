"""XLSX to CSV converter implementation."""

import pandas as pd

from src.core.converter import Converter


class XlsxToCsvConverter(Converter):
    """Convert XLSX files into CSV format."""

    def convert(self, file, **options) -> dict:
        """Perform XLSX to CSV conversion."""
        delimiter = options.get("delimiter", ",")
        encoding = options.get("encoding", "utf-8")

        try:
            df = pd.read_excel(file)
        except Exception as e:
            raise ValueError(f"Erro ao ler XLSX: {str(e)}") from e

        if df.empty:
            raise ValueError("O arquivo XLSX está vazio")

        output_file = "output.csv"
        df.to_csv(output_file, sep=delimiter, index=False, encoding=encoding)

        return {
            "output_file": output_file,
            "rows_processed": len(df),
            "columns": list(df.columns),
        }
