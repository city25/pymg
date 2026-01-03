"""Simple network checker."""
import socket


def check_network(host: str = "8.8.8.8", port: int = 53, timeout: int = 3) -> dict:
    try:
        s = socket.create_connection((host, port), timeout=timeout)
        s.close()
        return {"ok": True}
    except Exception as e:
        return {"ok": False, "error": str(e)}
