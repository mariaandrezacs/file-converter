"""Base abstractions for file converters."""

from abc import ABC, abstractmethod
from typing import BinaryIO


class Converter(ABC):
    """Abstract base class for file converters."""

    @abstractmethod
    def convert(self, file: BinaryIO, **options) -> dict:
        """Recebe um arquivo e retorna o resultado da conversão."""
