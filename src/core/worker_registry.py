from src.workers.worker_ollama import OllamaWorker
from src.workers.worker_rag import RagWorker
from src.workers.worker_health import HealthWorker
from src.workers.worker_log import LogWorker


class WorkerRegistry:
    ollama = OllamaWorker()
    rag = RagWorker()
    health = HealthWorker()
    log = LogWorker()