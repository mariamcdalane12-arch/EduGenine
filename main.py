from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from google import genai
from pydantic import BaseModel
import os

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


class Question(BaseModel):
    question: str


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
    request=request,
    name="index.html",
    context={}
)
   


@app.post("/ask")
def ask_gemini(data: Question):
    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=data.question
        )

        return {"answer": response.text}

    except Exception as e:
        error_message = str(e)

        if "429" in error_message:
            return {
                "answer": "Gemini API quota is currently exhausted. Please try again after the quota resets."
            }

        return {
            "answer": "Something went wrong. Please try again later."
        }
        