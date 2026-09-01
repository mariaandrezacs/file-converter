"""XML to CSV converter implementation."""

from typing import Any

import defusedxml.ElementTree as ET
import pandas as pd

from src.core.converter import Converter


class XmlToCsvConverter(Converter):
    """Convert XML files into CSV format."""

    def convert(self, file, **options) -> dict:
        """Perform XML to CSV conversion."""
        delimiter = options.get("delimiter", ",")
        encoding = options.get("encoding", "utf-8")

        try:
            content = file.read().decode(encoding)
            root = ET.fromstring(content)
        except Exception as e:
            raise ValueError(f"Erro ao ler XML: {str(e)}") from e

        records = []
        for child in root:
            record = self._extract_record(child)
            if record:
                records.append(record)

        if not records:
            raise ValueError("Não foi possível extrair registros do XML")

        df = pd.DataFrame(records)

        if df.empty:
            raise ValueError("O arquivo XML não contém dados válidos")

        output_file = "output.csv"
        df.to_csv(output_file, sep=delimiter, index=False, encoding=encoding)

        return {
            "output_file": output_file,
            "rows_processed": len(df),
            "columns": list(df.columns),
        }

    def _extract_record(self, element: ET.Element) -> dict[str, Any] | None:
        """Extract a record from an XML element."""
        record: dict[str, Any] = {}
        for child in element:
            text = (child.text or "").strip()
            if text:
                record[child.tag] = text

        if not record:
            return None

        return record
