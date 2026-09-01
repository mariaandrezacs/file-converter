"""JSON to YAML converter implementation."""

import json

import yaml

from src.core.converter import Converter


class JsonToYamlConverter(Converter):
    """Convert JSON files into YAML format."""

    def convert(self, file, **options) -> dict:
        """Perform JSON to YAML conversion."""
        encoding = options.get("encoding", "utf-8")

        try:
            content = file.read().decode(encoding)
            data = json.loads(content)
        except Exception as e:
            raise ValueError(f"Erro ao ler JSON: {str(e)}") from e

        if data is None or (isinstance(data, list) and not data):
            raise ValueError("O arquivo JSON está vazio")

        try:
            output_file = "output.yaml"
            with open(output_file, "w", encoding="utf-8") as f:
                yaml.safe_dump(
                    data,
                    f,
                    allow_unicode=True,
                    sort_keys=False,
                    default_flow_style=False,
                )
        except Exception as e:
            raise ValueError(f"Erro ao gerar YAML: {str(e)}") from e

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
