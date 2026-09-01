"""Service responsible for orchestrating YAML to JSON conversion."""

from src.yaml_to_json.converters.yaml_to_json import YamlToJsonConverter


class ConversionService:
    """Coordinate YAML to JSON conversion operations."""

    def __init__(self):
        """Initialize conversion service."""
        self.converter = YamlToJsonConverter()

    def convert_yaml_to_json(self, file, options):
        """Convert a YAML file to JSON format."""
        return self.converter.convert(file, **options)
