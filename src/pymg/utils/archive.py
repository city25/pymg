"""Archive (zip/tar) helpers."""
import shutil
from pathlib import Path


def extract_archive(archive_path: str, dest_dir: str) -> None:
    shutil.unpack_archive(archive_path, dest_dir)
