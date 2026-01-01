from typing import List, Dict
from src.core.base_response import BaseResponse



class ResponseHealthService(BaseResponse):
    ok: bool
    


class ResponseHealthDependencies(BaseResponse):
    ollama_model: List[str]
    log_file_exists: bool



class ResponseHealthEnvironment(BaseResponse):
    env_exists: bool
    requirements_exists: bool
    


class ResponseHealthAutofix(BaseResponse):
    ok: bool



class ResponseHealthFull(BaseResponse):
    service: Dict
    dependencies: Dict
    environment: Dict