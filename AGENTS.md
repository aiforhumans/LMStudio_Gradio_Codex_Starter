# Agent Guide for LM Studio + Gradio App

## How to run this project:
- Run `pip install -r requirements.txt`
- Run `python app.py` → Gradio UI will open in browser

## Project structure:
- `app.py` → main application entry point
- `api_client.py` → calls LM Studio API (running locally)
- `ui.py` → defines Gradio UI components

## Tests:
- Tests (optional) in `tests/` folder
- To run tests: `pytest tests/`

## Style:
- Follow PEP8 style
- Comment code to explain functions

## Agent instructions:
- When fixing bugs, always test running `python app.py`
- When adding features, document in code comments
