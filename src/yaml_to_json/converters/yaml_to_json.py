"""YAML to JSON converter implementation."""

import json

import yaml

from src.core.converter import Converter


class YamlToJsonConverter(Converter):
    """Convert YAML files into JSON format."""

    def convert(self, file, **options) -> dict:
        """Perform YAML to JSON conversion."""
        encoding = options.get("encoding", "utf-8")

        try:
            content = file.read().decode(encoding)
            data = yaml.safe_load(content)
        except Exception as e:
            raise ValueError(f"Erro ao ler YAML: {str(e)}") from e

        if data is None:
            raise ValueError("O arquivo YAML está vazio")

        output_file = "output.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        if isinstance(data, list):
            rows = len(data)
            columns = list(data[0].keys()) if data and isinstance(data[0], dict) else []
        elif isinstance(data, dict):
            rows = 1
            columns = list(data.keys())
        else:
            rows = 1
            columns = []

        return {
            "output_file": output_file,
            "rows_processed": rows,
            "columns": columns,
        }
