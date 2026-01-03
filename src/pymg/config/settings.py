"""Default settings for pymg."""
from pathlib import Path

DEFAULTS = {
    "download": {
        "cache_dir": str(Path.home() / ".pymg" / "cache"),
        "mirror": "https://pypi.org/",
    },
    "install": {"default_packages": ["pip", "setuptools", "wheel"]},
}
