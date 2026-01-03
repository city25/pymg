"""Base checker for diagnostics."""
from abc import ABC, abstractmethod


class Checker(ABC):
    @abstractmethod
    def check(self) -> dict:
        pass
