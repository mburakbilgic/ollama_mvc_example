from fastapi import APIRouter
import src
from src.views.view_ollama import (
    resp_model_list,
    resp_model_result,
    resp_error
)
from src.core.worker_registry import WorkerRegistry

router = APIRouter(prefix="/ollama", tags = ["ollama"])
worker = WorkerRegistry.ollama

# ---- __init__.py altında olan ve worker_main.py altında olan bütün kodları yazabilirsiniz ---- #

@router.get("/models")
async def list_models():
    try:
        result = worker.func_list_models()
        return resp_model_list(result["data"])
    except Exception as e:
        src.logger.error(str(e))
        return resp_error(str(e))

@router.get("/pull/{model_name}")
async def pull_model(model_name:str):
    try:
        result = worker.func_pull_models(model_name)
        return resp_model_result(model_name, result["data"])
    except Exception as e:
        src.logger.error(str(e))
        return resp_error(str(e))