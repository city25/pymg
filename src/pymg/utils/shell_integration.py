"""Helpers to integrate with user shells (profile edits)."""
from pathlib import Path


def add_path_to_profile(path: str, shell: str = "bash") -> None:
    profile = Path.home() / ".bashrc"
    with profile.open("a", encoding="utf-8") as f:
        f.write(f"\n# pymg path\nexport PATH=\"{path}:$PATH\"\n")
