from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    '''
    Функция тестирует доступ к проекту в сети и получение ответа с главной страницы
    '''
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "summarization app. Use method /summarization"}


def test_summarization_get():
    '''
    Функция тестирует доступ к проекту в сети и получение ответа со страницы /summarization
    '''
    response = client.get("/summarization")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]


def test_handle_form():
    '''
    Функция тестирует доступ к проекту в сети и получение ответа при отправке данных формы
    '''
    response = client.post("/summarization", data={"assignment": "Sample text"})
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    