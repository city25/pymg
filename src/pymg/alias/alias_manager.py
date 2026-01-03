"""Alias manager (stub)."""

class AliasManager:
    def __init__(self):
        self.aliases = {}

    def create(self, name: str, version: str):
        self.aliases[name] = version

    def remove(self, name: str):
        self.aliases.pop(name, None)

    def list(self):
        return dict(self.aliases)
