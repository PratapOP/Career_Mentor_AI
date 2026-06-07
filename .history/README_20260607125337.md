# Career Mentor AI

**Career Mentor AI** is a lightweight full-stack prototype that demonstrates how a frontend, PHP backend, and a local Python inference service can work together to provide resume guidance and skill recommendations.

This repository includes:
- `frontend/` — simple HTML/CSS user interface
- `backend/` — PHP endpoint to sanitize form input and forward it to the local AI service
- `ai_engine/` — basic Flask inference service and a fine-tune placeholder script

---

## Features

- Resume and career goal input form
- Backend validation in PHP
- Local AI microservice endpoint for analysis
- JSON-based API communication between PHP and Python
- Simple responsive interface for testing locally

---

## Project structure

```text
Career_Mentor_AI/
├── frontend/
│   ├── index.html          # User interface for resume and career goal input
│   └── style.css           # Visual styling for the frontend
├── backend/
│   ├── process.php         # Handles form requests and returns JSON results
│   └── api_client.php      # Calls the local Python inference service
└── ai_engine/
    ├── dataset.json        # Example placeholder dataset for fine-tuning
    ├── fine_tune.py        # Placeholder script for fine-tuning logic
    └── inference.py        # Local Flask inference service
```

---

## Setup and running locally

### Prerequisites

- PHP 8.x installed and available in your PATH
- Python 3.10+ installed
- `pip` available for Python package installation

### Install Python dependencies

Open a terminal in the repository root and run:

```powershell
cd C:\Users\mksme\Desktop\Career_Mentor_AI
python -m pip install flask
```

### Start the Python inference service

From the repository root:

```powershell
python .\ai_engine\inference.py
```

This starts a local server on `http://127.0.0.1:5000`.

### Start the PHP web server

From the repository root:

```powershell
php -S 127.0.0.1:8000
```

### Open the frontend

Visit `http://127.0.0.1:8000/frontend/index.html` in your browser.

---

## Notes

- If the inference service is unavailable, the backend returns a friendly fallback response.
- `fine_tune.py` is a starter placeholder; it does not train a model by default.
- `dataset.json` contains example entries for how a training dataset might be structured.

---

## File responsibilities

- `frontend/index.html` — collects user input and displays results
- `frontend/style.css` — styles the interface
- `backend/process.php` — validates input and returns JSON
- `backend/api_client.php` — sends request to the Python service
- `ai_engine/inference.py` — serves local AI inference responses
- `ai_engine/fine_tune.py` — placeholder for custom fine-tuning workflow
- `ai_engine/dataset.json` — sample dataset format
