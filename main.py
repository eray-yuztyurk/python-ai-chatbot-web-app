

# import libraries
from chatbot import get_response
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json

# Initialize Flask app
app = Flask(__name__)

CORS(app)  # Enable CORS for all routes

# Define a route for the index page
@app.route('/')
def index():
    return render_template('index.html', send_button_text="Send")

@app.route('/chat', methods=['POST'])
def chat():
    user_prompt = request.json.get("message")
    conversation, model_response = get_response(user_prompt)

    return {"response": model_response}

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)