"""Permission checks."""
import os


def check_permissions(paths: list[str]) -> dict:
    results = {}
    for p in paths:
        results[p] = os.access(p, os.W_OK)
    return results
