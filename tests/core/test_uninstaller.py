from pymg.core.uninstaller import Uninstaller


def test_uninstaller_init():
    u = Uninstaller("3.9.7")
    assert u.version == "3.9.7"
