# EduGenie – Google Gemini Powered Learning Assistant

## Project Objective

EduGenie is an AI-powered learning assistant that helps students understand topics easily using Google Gemini.

## Technologies Used

- Python
- FastAPI
- Google Gemini API
- HTML
- CSS
- JavaScript
- Jinja2
- Uvicorn

## Main Features

### 1. Ask EduGenie
Students can enter a question and receive an AI-generated answer.

### 2. Explain
Explains a topic in simple words that are easy for students to understand.

### 3. Quiz
Generates 5 simple quiz questions with answers based on the given topic.

### 4. Summarize
Provides a short and simple summary of the given topic.

## Project Structure

EduGenie/
├── main.py
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css

## How It Works

1. The student enters a question or topic.
2. EduGenie sends the request to the FastAPI backend.
3. The backend sends the request to Google Gemini.
4. Gemini generates the response.
5. EduGenie displays the response on the webpage.

## How to Run

Open the project folder in VS Code.

Run:

uvicorn main:app --reload

Then open:

http://127.0.0.1:8000

## Future Improvements

- Add student login.
- Add chat history.
- Add voice input.
- Add more learning tools.
- Improve the user interface.