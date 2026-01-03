from pymg.utils.downloader import download


def test_download_stub(tmp_path):
    path = str(tmp_path / "f")
    assert download("http://example.com", path) == path
