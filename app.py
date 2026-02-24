"""
app.py

This is the Flask entry point of the F1 Chatbot application.

Responsibilities:
- Initialize Flask app
- Initialize the LLM (via llm.py)
- Handle HTTP routes
- Accept user input from frontend
- Pass user input to f1_chatbot.process_query()
- Render HTML template with response

This file should NOT contain:
- ML prediction logic
- LLM prompt design
- Data processing
- Model loading
- Business logic

Think of this as the "web interface layer".
"""
# NOTE this code is not complete - it's just the structure for now. 
from flask import Flask, request, render_template
from llm import get_llm
from f1_chatbot import process_query

# Initialize Flask app
app = Flask(__name__)

# Initialize Gemini LLM
llm = get_llm()

@app.route("/", methods=["GET", "POST"])
def home():
    """
    Handle homepage rendering and form submission.

    On POST:
    - Retrieve user question
    - Call process_query(question, llm)
    - Return response to template

    On GET:
    - Render empty page
    """
    pass


if __name__ == "__main__":
    app.run(debug=True)
