"""Installer logic (skeleton).

Provides a minimal Installer class to encapsulate install operations.
"""
from typing import Optional


class Installer:
    def __init__(self, version: str, dest: Optional[str] = None):
        self.version = version
        self.dest = dest

    def prepare(self) -> None:
        """Prepare download/build steps."""
        pass

    def install(self) -> None:
        """Perform installation."""
        pass
