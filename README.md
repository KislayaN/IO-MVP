# IO-MVP

A lightweight AI Agent MVP built with Streamlit and Google's Gemini API. The goal of this project is to provide a clean starting point for building AI-powered applications with a simple frontend, secure environment variable management, and a modular architecture that can be extended later with tools, memory, RAG, and agent workflows.

## Tech Stack

* Python 3.10+
* Streamlit
* Google Gemini API
* python-dotenv
* uv Package Manager

## Project Structure

```text
IO-MVP/
│
├── .env                # Secret credentials (not pushed to GitHub)
├── .gitignore
├── .python-version
│
├── app.py              # Streamlit UI
├── main.py             # Application entry logic
├── test.py             # Testing and experimentation
│
├── requirements.txt
├── pyproject.toml
├── uv.lock
│
└── README.md
```

## Features

* Streamlit-based chat interface
* Gemini-powered responses
* Environment variable support through `.env`
* Simple MVP architecture
* GitHub-ready setup
* Easy to extend with additional tools and agents

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd IO-MVP
```

### Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
uv sync
```

## Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Never commit the `.env` file to GitHub.

## Required Packages

```bash
pip install streamlit
pip install google-generativeai
pip install python-dotenv
```

## Gemini Setup

```python
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)
```

## Running the Application

```bash
streamlit run app.py
```

The application will start locally and open automatically in your browser.

## Workflow

1. User enters a prompt through the Streamlit UI.
2. The application sends the prompt to Gemini.
3. Gemini generates a response.
4. The response is displayed in the interface.
5. Future tools and integrations can be plugged into the same architecture.

## Git Ignore

Recommended `.gitignore`:

```gitignore
.venv/
.env
__pycache__/
*.pyc
```

## Future Improvements

* Tool Calling
* Function Calling
* Memory Support
* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Multi-Agent Workflows
* Authentication
* Chat History Storage
* Docker Support
* Cloud Deployment

## Security Notes

* Never commit API keys.
* Store secrets only inside `.env`.
* Rotate any key that has ever been committed to Git history.
* Verify `.env` is listed in `.gitignore` before pushing.

## License

This project is intended for learning, experimentation, and rapid AI application prototyping.