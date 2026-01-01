import os
import socket
import subprocess
import src
from src.core.base_worker import BaseWorker



class HealthWorker(BaseWorker):
    
    # ---------------- PUBLIC METHODS ---------------- #    
    def func_service_check(self, host: str, port: int):
        return self._check_service(host, port)
    
    def func_dependencies_check(self):
        return self._check_dependencies()
    
    def func_environment_check(self):
        return self._check_environment()
    
    def func_environment_autofix(self):
        return self._autofix_environment()
    
    def func_full_check(self, host:str, port:int):
        return {
            "service": self._check_service(host, port),
            "dependencies": self._check_dependencies(),
            "environment": self._check_environment()
        }
    
    # ---------------- HELPER METHODS ---------------- #
    def _check_service(self, host: str, port:int):
        with socket.create_connection((host, port), timeout=2):
            return {"ok": True}
    
    def _check_dependencies(self):
        return {
            "ollama_model": src.ollama.list_models(),
            "log_file_exists": os.path.exists(
                os.environ.get("LOG_FILE", "app.log")
            )
        }
    
    def _check_environment(self):
        return {
            "env_exists": os.path.exists("env_mvc"),
            "requirements_exists": os.path.exists("requirements.txt")
        }
    
    def _autofix_environment(self):
        subprocess.check_call(["pip", "install", "-r", "requirements.txt"])
        return {"ok": True}