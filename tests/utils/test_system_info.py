from pymg.utils.system_info import get_system_info


def test_system_info():
    info = get_system_info()
    assert "os" in info and "arch" in info
