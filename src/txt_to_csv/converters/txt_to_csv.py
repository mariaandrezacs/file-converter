"""TXT to CSV converter implementation."""

import csv
import io

import pandas as pd

from src.core.converter import Converter


class TxtToCsvConverter(Converter):
    """Convert TXT files into CSV format."""

    def convert(self, file, **options) -> dict:
        """Perform TXT to CSV conversion."""
        delimiter = options.get("delimiter", "\t")
        encoding = options.get("encoding", "utf-8")
        has_header = options.get("has_header", False)

        try:
            content = file.read().decode(encoding)
        except Exception as e:
            raise ValueError(f"Erro ao ler TXT: {str(e)}") from e

        reader = csv.reader(io.StringIO(content), delimiter=delimiter)
        rows = list(reader)

        if not rows or not any(rows):
            raise ValueError("O arquivo TXT está vazio")

        if has_header:
            header = rows[0]
            data = rows[1:]
        else:
            header = [f"col{i}" for i in range(len(rows[0]))]
            data = rows

        df = pd.DataFrame(data, columns=header)

        output_file = "output.csv"
        df.to_csv(output_file, index=False, encoding=encoding)

        return {
            "output_file": output_file,
            "rows_processed": len(df),
            "columns": list(df.columns),
        }
