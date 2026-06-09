from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

MODEL_ID = "Qwen/Qwen2.5-1.5B-Instruct"

MODEL_DIR = BASE_DIR / "models"

ADAPTER_DIR = MODEL_DIR / "final_adapter_weights"

UPLOAD_DIR = BASE_DIR / "uploads"

MAX_CONTENT_LENGTH = 10 * 1024 * 1024

HOST = "127.0.0.1"

PORT = 5000

DEBUG = False

GENERATION_CONFIG = {
    "max_new_tokens": 512,
    "temperature": 0.3,
    "top_p": 0.9,
    "do_sample": True
}