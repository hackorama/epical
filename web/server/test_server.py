from fastapi.testclient import TestClient

from .server import app

client = TestClient(app)


def test_server():
    response = client.get("/health")
    assert response.status_code == 200
    assert "OK" in response.text


def test_log_upload():
    url = "/upload/logs"
    file = {
        "file": (
            "log.txt",
            open("./test/test.txt", "rb"),  # pylint: disable=consider-using-with
        )
    }
    response = client.post(url=url, files=file)
    assert response.status_code == 200
    assert "OK" in response.text


def test_screen_upload():
    url = "/upload/screen"
    file = {
        "file": (
            "epical.png",
            open("./test/test.png", "rb"),  # pylint: disable=consider-using-with
        )
    }
    response = client.post(url=url, files=file)
    assert response.status_code == 200
    assert "OK" in response.text


def test_photo_upload():
    url = "/upload/photo"
    file = {
        "file": (
            "epical.png",
            open("./test/test.png", "rb"),  # pylint: disable=consider-using-with
        )
    }
    response = client.post(url=url, files=file)
    assert response.status_code == 200
    assert "Settings" in response.text


def test_refresh_battery():
    url = "/refresh/battery"
    response = client.post(url=url)
    assert response.status_code == 200
    assert "Settings" in response.text


def test_remove_upgrade():
    url = "/remove/upgrade"
    response = client.post(url=url)
    assert response.status_code == 200
    assert "Settings" in response.text


def test_refresh_disable():
    url = "/refresh/disable"
    response = client.post(url=url)
    assert response.status_code == 200
    assert "Settings" in response.text
