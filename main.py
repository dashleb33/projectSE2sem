from fastapi import FastAPI, Form, Request
from transformers import pipeline
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")# загружаем токенайзер

model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")# загружаем модель

templates = Jinja2Templates(directory="htmldirectory")

app = FastAPI()
summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)# собираем пайплайн


# Главная страница, говорит куда переходить дальше
@app.get("/")
def root():
    return {"message": "summarization app. Use method /summarization"}


#страница для работы с моделью
@app.get("/summarization", response_class=HTMLResponse)
def summarize(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


#Основая функция
@app.post("/summarization", response_class=HTMLResponse)
def handle_form(request: Request, assignment: str = Form(...)):
    text = summarizer(assignment, max_length=130, min_length=30, do_sample=False)
    return templates.TemplateResponse("home.html",
        {
            "request": request,
            "assignment": assignment, 
            "result": text[0]["summary_text"]
        })
