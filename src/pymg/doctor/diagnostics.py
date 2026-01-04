"""Diagnostics runner for pymg."""

from pymg.doctor.network_checker import check_network
from pymg.doctor.permission_checker import check_permissions


class Diagnostics:
    def run_all(self) -> dict:
        return {
            "network": check_network(),
            "permissions": check_permissions(["/tmp"]),
        }
