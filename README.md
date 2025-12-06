

# Python AI Chatbot Web App

A comprehensive, local chatbot web application built with Flask and Hugging Face Transformers. This project demonstrates how to run a pre-trained conversational model in a modern web interface. It is designed for experimentation, learning, and local use—not for production deployment.

---
<p align="center">
  <img src="https://github.com/user-attachments/assets/aed54aa0-9908-402c-b238-c598475b35cf" alt="demo" width="80%">
</p>
---

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration & Customization](#configuration--customization)
- [Model Information](#model-information)
- [Development & Testing](#development--testing)
- [Docker Usage](#docker-usage)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## Features
- Interactive chat interface powered by Flask and vanilla JavaScript
- Uses Hugging Face Transformers for natural language responses
- Dockerfile for easy containerization
- Simple, readable codebase for educational purposes
- Model caching for faster inference
- Customizable model selection (edit `chatbot.py`)
- Clean separation of backend and frontend logic

## Requirements
- Python 3.10+
- pip
- (Optional) Docker

## Installation

1. **Clone the repository**
	 ```bash
	 git clone https://github.com/eray-yuztyurk/python-ai-chatbot-web-app.git
	 cd python-ai-chatbot-huggingface-web-app
	 ```

2. **Create a virtual environment (recommended)**
	 ```bash
	 python3.10 -m venv venv
	 source venv/bin/activate
	 ```

3. **Install dependencies**
	 ```bash
	 pip install --upgrade pip
	 pip install -r requirements.txt
	 ```

## Usage

### Run the app locally
```bash
python main.py
```
Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000) to use the chatbot interface.

### Run with Docker
Build and run the app in a container:
```bash
docker build -t python-ai-chatbot-app .
docker run -p 5000:5000 python-ai-chatbot-app
```

## Project Structure

```
├── chatbot.py         # Loads the model, manages chat history, and generates responses
├── main.py            # Flask app entry point and route definitions
├── requirements.txt   # Python dependencies
├── Dockerfile         # Container configuration
├── static/            # Frontend static files (CSS, JS)
│   ├── styles.css
│   └── script.js
├── templates/         # HTML templates
│   └── index.html
└── ...
```

## Configuration & Customization

- **Change the model:**
	- By default, the app uses `facebook/blenderbot-400M-distill`.
	- To use a different Hugging Face model, edit the `model_name` variable in `chatbot.py`.
	- Make sure the model is compatible with the code (Seq2Seq or CausalLM).

- **Frontend customization:**
	- Edit `static/styles.css` for styles and `static/script.js` for client-side logic.
	- The chat interface is defined in `templates/index.html`.

- **Port configuration:**
	- The Flask app runs on port 5000 by default. Change it in `main.py` if needed.

## Model Information
- The app uses a pre-trained Blenderbot model from Hugging Face by default.
- The model is downloaded automatically on first run. This may take several minutes depending on your internet speed.
- You can change the model in `chatbot.py` if you wish to experiment with other conversational models.
- For smaller/faster models, see [Hugging Face Model Hub](https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads).

## Development & Testing

- **Code style:** Follows standard Python and Flask best practices.
- **Testing:**
	- Manual: Run the app and interact via the web UI.
	- Automated tests can be added as needed.
- **Hot reload:**
	- For development, run with `debug=True` in `main.py` for auto-reload on code changes.

## Docker Usage

1. **Build the Docker image:**
	 ```bash
	 docker build -t python-ai-chatbot-app .
	 ```
2. **Run the container:**
	 ```bash
	 docker run -p 5000:5000 python-ai-chatbot-app
	 ```
3. **Access the app:**
	 Open [http://localhost:5000](http://localhost:5000) in your browser.

## Troubleshooting

- **Model download is slow:**
	- The first run downloads the model weights. Please wait until the process completes.
- **Out of memory:**
	- Use a smaller model or ensure your machine has enough RAM.
- **Port issues:**
	- Make sure port 5000 is available or change it in `main.py` and Dockerfile.
- **CUDA/CPU issues:**
	- The app will use GPU if available, otherwise falls back to CPU.
- **Dependency errors:**
	- Ensure you are using Python 3.10+ and all dependencies are installed from `requirements.txt`.
- **Frontend not loading:**
	- Check browser console for errors and ensure static files are being served.

## Contributing

Pull requests and issues are welcome. Please:
- Keep code clean and well-documented
- Follow existing code style and structure
- Add comments/docstrings where appropriate

## License

This project is released under the MIT License.

---

**Disclaimer:** This project is for learning and experimentation only. Not intended for production use or handling sensitive data.
