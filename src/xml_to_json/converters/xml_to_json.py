"""XML to JSON converter implementation."""

import json
from typing import Any

import defusedxml.ElementTree as ET

from src.core.converter import Converter


class XmlToJsonConverter(Converter):
    """Convert XML files into JSON format."""

    def convert(self, file, **options) -> dict:
        """Perform XML to JSON conversion."""
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

        output_file = "output.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(records, f, ensure_ascii=False, indent=2)

        columns = list(records[0].keys()) if records else []

        return {
            "output_file": output_file,
            "rows_processed": len(records),
            "columns": columns,
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
