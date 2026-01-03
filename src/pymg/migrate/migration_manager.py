"""Migration manager (stub)."""

class MigrationManager:
    def migrate(self, from_ver: str, to_ver: str, packages: list[str] | None = None):
        """Migrate packages from one interpreter to another."""
        return {
            "from": from_ver,
            "to": to_ver,
            "packages": packages or [],
        }
