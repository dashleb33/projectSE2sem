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


def test_predict_main():
    '''
    Функция тестирует корректность работы нейронной сети
    '''
    respose_text = '''
    Katherine Mansfield, an outstanding English short-story writer of the 20th century,
    was born in New Zealand in 1888 and died in 1923.
    She is the author of a number of excellent short stories which deal with human nature and psychology.
    At the age of eighteen she decided to become a professional writer.
    Her first short stories appeared in Melbourne in 1907,
    but literary fame came to her in London after the publication of a collection
    of short stories called "In a German Pension".
    Katherine Mansfield took a great interest in Russian literature, particularly in the works of Chekhov.
    In fact, she considered herself to be a pupil of the great Russian writer.
    Rosemary Fell was not exactly beautiful. She was young, brilliant, extremely modern,
    well dressed and amazingly well read in the newest of the new books.
    Rosemary had been married two years, and her husband was very fond of her.
    They were rich, really rich, not just comfortably well-off, so if Rosemary wanted to shop,
    she would go to Paris as you and I would go to Bond Street.
    One winter afternoon she went into a small shop to look at a little box which the shopman had been keeping for her.
    He had shown it to nobody as yet so that she might be the first to see it.'''
    
    response = client.post('/summarization/', data={'assignment': respose_text}) 

    assert response.status_code == 200
    
    assert 'Katherine Mansfield was born in New Zealand in 1888 and died in 1923' in response.text    
