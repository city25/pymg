import pytest


@pytest.fixture()
def temp_dir(tmp_path):
    return tmp_path
