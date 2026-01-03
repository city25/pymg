from pymg.core.installer import Installer


def test_installer_init():
    inst = Installer("3.11.3")
    assert inst.version == "3.11.3"
