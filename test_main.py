from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "summarization app. Use method /summarization"}


def test_translate_get():
    response = client.get("/summarization")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]


def test_handle_form():
    response = client.post("/summarization", data={"assignment": "Sample text"})
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    # assert "Sample text" in response.text
    # assert "result" in response.text