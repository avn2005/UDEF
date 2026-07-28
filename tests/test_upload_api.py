from io import BytesIO

from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_upload_endpoint_accepts_file():
    response = client.post(
        "/upload",
        files={"file": ("test.txt", BytesIO(b"hello world"), "text/plain")},
    )

    assert response.status_code == 200
    assert response.json()["filename"] == "test.txt"
    assert response.json()["size"] == 11
