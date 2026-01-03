"""Executor for running commands using a specific Python version."""

from typing import Sequence


class Executor:
    def run(self, version: str, cmd: Sequence[str]):
        """Run command `cmd` using the interpreter for `version`."""
        return 0
