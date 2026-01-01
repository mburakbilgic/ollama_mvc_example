""" 
src package intiliazer
Acts as a global config & shared resources module.
"""

import os
import requests
import json
from typing import Optional, Dict
import logging
from logging.handlers import RotatingFileHandler

# ------------------------ #
# ENV / CONFIG             #
# ------------------------ #

PRIMARY_LLM = os.environ.get(
    "LLM_MODEL",
    "steamdj/llama3.1-cpu-only"
)

FALLBACK_LLM = os.environ.get(
    "LLM_FALLBACK",
    "qwen2.5:0.5b-instruct"
)

EMBED_MODEL = os.environ.get(
    "EMBED_MODEL",
    "nomic-embed-text"
)

OLLAMA_URL = os.environ.get(
    "OLLAMA_URL",
    "http://127.0.0.1:11434"
)

APP_NAME = os.environ.get("APP_NAME", "mvc_example")
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO").upper()
LOG_FILE = os.environ.get("LOG_FILE", "app.log")
KB_PATH = os.environ.get("KB_PATH", "src/data/knowledge_base.md")
KB_FORMAT = os.environ.get("KB_FORMAT", "md").lower()

# ------------------------ #
# Logger                   #
# ------------------------ #

logger = logging.getLogger(APP_NAME)
logger.setLevel(LOG_LEVEL)

_formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")

# Console Handler
_console_handler = logging.StreamHandler()
_console_handler.setFormatter(_formatter)

# File handler (rotating)
_file_handler = RotatingFileHandler(
    filename="app.log",
    maxBytes= 5 * 1024 * 1024, # (5MB)
    backupCount=3,
    encoding="utf-8"
)
_file_handler.setFormatter(_formatter)

# Prevent duplication of streaming (console_handler) and rotating (file_handler)
if not logger.handlers:
    logger.addHandler(_console_handler)
    logger.addHandler(_file_handler)



# ------------------------ #
# OLLAMA CLIENT            #
# ------------------------ #
class OllamaClient:
    """
    Shared Ollama HTTP Client
    Used for all workers/controllers 
    """
    
    def __init__(self, base_url:str, timeout: int=300):
        self.base_url = base_url
        self.timeout = timeout

    def _post(self, path:str, payload: Dict, stream: bool = False):
        r = requests.post(
            f"{self.base_url}{path}",
            json=payload,
            stream=stream,
            timeout=self.timeout
        )
        r.raise_for_status()
        return r
    
    def list_models(self):
        r = requests.get(f"{self.base_url}/api/tags", timeout=30)
        r.raise_for_status()
        return [m["name"] for m in r.json().get("models", [])]
    
    def generate(self, model:str, prompt:str, temperature: float=0.2, system: Optional[str] = None):
        payload = {
            "model": model,
            "prompt": f"<sytem>{system}</system>" if system else prompt,
            "options": {"temperature": temperature},
            "stream": False # İstek bazlı bir servis oluşturduğumuz için bu ifade False, ama websocket veya socket tanımlı olsaydı sürekli açık kalması için True diyecektik
        }
        r = self._post("/api/generate", payload)
        return r.json().get("response", "")
    
    def embed(self, model:str, text:str):
        r = self._post("/api/embeddings", {
                                           "model": model,
                                           "prompt": text})
        return r.json()["embedding"]
    
ollama = OllamaClient(OLLAMA_URL)

# ------------------------------ #
# STARTUP VALIDATION (Safe-Note) #
# ------------------------------ #

try:
    models = ollama.list_models()
    logger.info(f"Ollama connected. Available models | {models}")
except Exception as e:
    logger.warning(f"Ollama not reachable | {e}")