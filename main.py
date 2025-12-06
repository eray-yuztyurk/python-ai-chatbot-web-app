"""
Main application file for the Flask-based chatbot web app.

This module initializes the Flask server, defines the web routes, and handles
communication between the frontend and the chatbot backend logic.
"""

from chatbot import get_response
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS


app = Flask(__name__)


CORS(app)  # Enable CORS for all routes


@app.route('/')
def index():
    """
    Render the main chat interface page.
    Returns the HTML template for the chatbot UI.
    """
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    """
    Handle chat requests from the frontend.
    Receives a user message via POST, gets a response from the chatbot,
    and returns the model's reply as JSON.
    """
    user_prompt = request.json.get("message")
    conversation, model_response = get_response(user_prompt)
    return jsonify({"response": model_response})


if __name__ == "__main__":
    """
    Entry point for running the Flask development server.
    """
    app.run(host="127.0.0.1", port=5000, debug=True)