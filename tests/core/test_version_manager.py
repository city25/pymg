from pymg.core.version_manager import VersionManager


def test_version_manager_current():
    vm = VersionManager()
    assert isinstance(vm.current(), str)
