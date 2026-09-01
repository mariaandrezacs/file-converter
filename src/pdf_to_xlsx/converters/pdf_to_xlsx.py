"""PDF to XLSX converter implementation."""

import pandas as pd
from pypdf import PdfReader

from src.core.converter import Converter


class PdfToXlsxConverter(Converter):
    """Convert PDF files into XLSX format."""

    def convert(self, file, **options) -> dict:
        """Perform PDF to XLSX conversion."""
        try:
            reader = PdfReader(file)
        except Exception as e:
            raise ValueError(f"Erro ao ler PDF: {str(e)}") from e

        if not reader.pages:
            raise ValueError("O arquivo PDF está vazio")

        lines = []
        for page in reader.pages:
            text = page.extract_text() or ""
            for line in text.splitlines():
                line = line.strip()
                if line:
                    lines.append(line)

        if not lines:
            raise ValueError("O arquivo PDF não contém texto extraível")

        records = []
        for line in lines:
            if "," in line:
                records.append(line.split(","))
            elif ";" in line:
                records.append(line.split(";"))
            elif "\t" in line:
                records.append(line.split("\t"))
            else:
                records.append([line])

        max_cols = max(len(r) for r in records)
        columns = [f"col{i}" for i in range(max_cols)]
        df = pd.DataFrame(records, columns=columns)

        output_file = "output.xlsx"
        df.to_excel(output_file, index=False)

        return {
            "output_file": output_file,
            "rows_processed": len(df),
            "columns": list(df.columns),
        }
