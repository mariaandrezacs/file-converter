"""Service responsible for orchestrating JSON to YAML conversion."""

from src.json_to_yaml.converters.json_to_yaml import JsonToYamlConverter


class ConversionService:
    """Coordinate JSON to YAML conversion operations."""

    def __init__(self):
        """Initialize conversion service."""
        self.converter = JsonToYamlConverter()

    def convert_json_to_yaml(self, file, options):
        """Convert a JSON file to YAML format."""
        return self.converter.convert(file, **options)
