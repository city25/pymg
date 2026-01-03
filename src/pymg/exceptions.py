"""Custom exceptions for pymg."""


class PymgError(Exception):
    """Base exception for pymg."""


class InstallationError(PymgError):
    pass


class DownloadError(PymgError):
    pass
