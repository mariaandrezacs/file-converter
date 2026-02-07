"""CSV to XLSX converter implementation."""

import pandas as pd

from src.csv_to_xlsx.converters.base import Converter


class CsvToXlsxConverter(Converter):
    """Convert CSV files into XLSX format."""

    def convert(self, file, **options) -> dict:
        """Perform CSV to XLSX conversion."""
        delimiter = options.get("delimiter", ",")
        encoding = options.get("encoding", "utf-8")

        try:
            df = pd.read_csv(file, delimiter=delimiter, encoding=encoding)
        except Exception as e:
            raise ValueError(f"Erro ao ler CSV: {str(e)}") from e

        if df.empty:
            raise ValueError("O arquivo CSV está vazio")

        output_file = "output.xlsx"
        df.to_excel(output_file, index=False)

        return {
            "output_file": output_file,
            "rows_processed": len(df),
            "columns": list(df.columns),
        }
