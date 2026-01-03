"""Simple config manager (stub)."""
import toml
from pathlib import Path


class ConfigManager:
    def __init__(self, path: str | None = None):
        self.path = Path(path) if path else Path.home() / ".pymg" / "config.toml"
        self.data = {}

    def load(self):
        if self.path.exists():
            self.data = toml.loads(self.path.read_text(encoding="utf-8"))
        return self.data

    def save(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(toml.dumps(self.data), encoding="utf-8")
