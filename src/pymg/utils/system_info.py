"""Detect OS and architecture info."""
import platform


def get_system_info() -> dict:
    return {
        "os": platform.system(),
        "arch": platform.machine(),
        "platform": platform.platform(),
    }
