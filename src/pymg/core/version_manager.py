"""Version selection and querying utilities."""


class VersionManager:
    def use(self, version: str, scope: str = "temp") -> None:
        """Switch to a specific version. scope: temp/local/global"""
        pass

    def current(self) -> str:
        """Return currently active version."""
        return "system"

    def which(self, version: str) -> str:
        """Return path for given version."""
        return ""
